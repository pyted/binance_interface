import random
import datetime
import time
import numpy as np
import pendulum
from typing import Literal, Union
from paux import filter as _filter
from paux import log as _log
from paux import date as _date
from paux import thread as _thread
from candlelite.calculate import interval as _interval
from candlelite.crypto.binace_lite import BinanceLite
from binance_interface.app import code
from binance_interface.app.market import Market
from binance_interface.app import exception
from binance_interface.app.candle_server.rule import CandleRule


class CandleServer():
    def __init__(self, instType: Literal['SPOT', 'UM', 'CM'], rule=CandleRule, proxies={}, proxy_host: str = None):
        # 规则
        self.rule = rule
        # # 每日下载历史K线的时间 -> 维护self.rule.DOWNLOAD_TIME
        # if self.rule.DOWNLOAD_TIME.lower() == 'auto':
        #     minutes = int(_interval.get_interval(self.rule.BAR) / 60000 * 2)
        #     minutes = int(np.clip(minutes, 10, 1439))
        #     download_time = (pendulum.time(0, 0, 0) + datetime.timedelta(minutes=minutes)).strftime('%H:%M:%S')
        #     self.rule.DOWNLOAD_TIME = download_time
        # 产品类型
        self.instType = instType.upper()
        # 行情客户端
        self.market = Market(instType=instType, key=self.rule.KEY, secret=self.rule.SECRET, timezone=self.rule.TIMEZONE,
                             proxies=proxies, proxy_host=proxy_host)
        # 产品过滤器 用于candle_map的更新
        self.filter = _filter.Filter()
        # BinanceLite
        self.binanceLite = BinanceLite()
        self.binanceLite.CANDLE_DATE_BASE_DIR = self.rule.CANDLE_DIR
        self.binanceLite.CANDLE_FILE_BASE_DIR = self.rule.CACHE_DIR
        self.binanceLite.TIMEZONE = self.rule.TIMEZONE
        # 日志
        self.log = _log.Log(
            log_dirpath=self.rule.LOG_DIRPATH,
            file_level=self.rule.LOG_FILE_LEVEL,
            console_level=self.rule.LOG_CONSOLE_LEVEL,
        )
        self.lite = self.binanceLite
        self._run_candle_map_thread = None
        self.__close_run_candle_map_signal = False
        self._download_daily_thread = None
        self.__close_download_daily_thread = False

    # 获取过滤后的产品名称
    def get_symbols_filtered(
            self,
            type='trading_on'  #
    ) -> dict:
        '''
        :param type:
            trading_on:     正在交易的
            trading_off:    不在交易的
            trading_all:    全部
        过滤内容：
            1. rule.SYMBOLS_FILTER
            2. rule.SYMBOLS_CONTAINS
            3. rule.SYMBOL_ENDSWITH
            4. CandleServer.filter
        '''
        # 验证self.symbols
        if not (
                self.rule.SYMBOLS == 'all' or
                isinstance(self.rule.SYMBOLS, list)
        ):
            msg = 'rule.SYMBOLS must be "all" or list type'
            raise exception.RuleException(msg)
        if type not in ['trading_on', 'trading_off', 'trading_all']:
            msg = 'type must in ["trading_on","trading_off","trading_all"].'
            raise exception.ParamException(msg)
        # 产品为全部 self.rule.SYMBOLS = 'all'
        if isinstance(self.rule.SYMBOLS, str) and self.rule.SYMBOLS.lower() == 'all':
            if type == 'trading_on':
                symbols_trading_result = self.market.get_symbols_trading_on(
                    expire_seconds=60 * 60,  # 使用的缓存过期时间
                )
            elif type == 'trading_off':
                symbols_trading_result = self.market.get_symbols_trading_off(
                    expire_seconds=60 * 60,  # 使用的缓存过期时间
                )
            else:
                symbols_trading_result = self.market.get_symbols_all(
                    expire_seconds=60 * 60,  # 使用的缓存过期时间
                )
            if symbols_trading_result['code'] != 200:
                return symbols_trading_result
            symbols = symbols_trading_result['data']
        # 产品类型为列表
        else:
            symbols = self.rule.SYMBOLS
        # 第一次过滤 使用rule中的条件 -> symbols_filtered1
        # SYMBOLS_FILTER
        # SYMBOL_CONTAINS
        # SYMBOL_ENDSWITH
        symbols_filtered1 = []
        for symbol in symbols:
            symbol: str
            if self.rule.SYMBOLS_FILTER and symbol in self.rule.SYMBOLS_FILTER:
                continue
            if self.rule.SYMBOL_CONTAINS and not self.rule.SYMBOL_CONTAINS in symbol:
                continue
            if self.rule.SYMBOL_ENDSWITH and not symbol.endswith(self.rule.SYMBOL_ENDSWITH):
                continue
            symbols_filtered1.append(symbol)
        # 仅当trading-on是否进行第二次过滤
        if type == 'trading_on':
            # 第二次过滤 self.filter 过滤数据不足，请求错误的symbol -> symbols_filtered2
            symbols_filtered2 = []
            for symbol in symbols_filtered1:
                symbol: str
                if self.filter.check(symbol):  # True 不过滤
                    symbols_filtered2.append(symbol)
            result = {'code': 200, 'data': symbols_filtered2, 'msg': ''}
        else:
            result = {'code': 200, 'data': symbols_filtered1, 'msg': ''}
        return result

    # 按照日期下载历史K线
    def download_candles_by_date(
            self,
            start: Union[str, int, float, datetime.date],
            end: Union[str, int, float, datetime.date, None] = None,
            type: str = 'trading_on',
            replace=False,
    ):
        '''
        :param start: 起始日期
        :param end: 终止日期
            None 使用昨日日期
        :param type: 产品交易类型
            trading_on      正在交易的产品
            trading_off     不可交易的产品
            trading_all     全部产品
        :param replace: 是否替换本地文件
        '''
        # 计算每天下载数据的延时 delay
        # 现货交易
        if self.instType.upper() == 'SPOT':
            # 下载一天的数据需要花费权重2 总权重1200 单次延时为 2 / (1200 * SERVER_WEIGHT)
            delay = 60 * 2 / (1200 * self.rule.SERVER_WEIGHT)
        else:
            # 下载一天的数据需要花费权重10 总权重2400 单次延时为 10 / (2400 * SERVER_WEIGHT)
            delay = 60 * 10 / (2400 * self.rule.SERVER_WEIGHT)
        delay = round(delay, 4)
        # 执行下载使用的临时过滤器，过滤数据异常的产品
        self._download_filter = _filter.Filter()
        # 日期终点
        if not end:
            end = pendulum.yesterday(tz=self.rule.TIMEZONE)
        # 需要下载的日期序列
        date_range = _date.get_range_dates(start=start, end=end, timezone=self.rule.TIMEZONE)
        # 反转日期序列，用于加速
        date_range = sorted(date_range, reverse=True)
        # 按照日期下载
        for date in date_range:
            self.__download_candles_by_date(
                date=date,
                type=type,
                replace=replace,
            )

            if delay > 0:
                time.sleep(delay)
        # 删除临时过滤器
        del self._download_filter

    # 下载某一天多产品历史K线数据
    def __download_candles_by_date(
            self,
            date: Union[str, int, float, datetime.date],
            type='trading_on',
            replace=False,
    ):
        '''
        :param date: 日期
        :param type: 产品交易类型
            trading_on      正在交易的产品
            trading_off     不可交易的产品
            trading_all     全部产品
        :param replace: 是否替换本地文件
        '''
        # 日期字符串，用于控制台打印
        if self.rule.TIMEZONE == 'America/New_York':
            date_str = _date.to_fmt(date, self.rule.TIMEZONE, '%d/%m/%Y')
        else:
            date_str = _date.to_fmt(date, self.rule.TIMEZONE, '%Y-%m-%d')
        # 获取产品列表
        get_symbols_filtered_result = self.get_symbols_filtered(type=type, )
        # **[ERROR RAISE]** 产品列表有误
        if get_symbols_filtered_result['code'] != 200:
            msg = '[get_symbols_filtered] code={code} msg={msg}'.format(
                msg=get_symbols_filtered_result['msg'],
                code=get_symbols_filtered_result['code'],
            )
            self.log.error(msg)
            raise exception.CodeException(msg)
        symbols = get_symbols_filtered_result['data']
        # 过滤下载异常的产品(仅当下载正在运行交易的产品，进行过滤）
        if type == 'trading_on':
            symbols = [symbol for symbol in symbols if self._download_filter.check(symbol)]
        # 产品逐个下载
        download_detail = {
            'all': len(symbols),  # 总数
            'skip': 0,  # 跳过的个数
            'suc': 0,  # 成功的个数
            'warn': 0,  # 警告的个数
            'error': 0,  # 失败的个数
        }
        for symbol in symbols:
            # 不替换且存在数据
            if not replace and self.binanceLite.check_candle_date_path(
                    instType=self.instType,
                    symbol=symbol,
                    start=date,
                    end=date,
                    bar=self.rule.BAR,
            )['code']:
                download_detail['skip'] += 1
                continue
            # 发送请求的时间戳 用于权重延时
            request_time = time.time()
            # 按照日期下载数据
            get_history_candle_by_date_result = self.market.get_history_candle_by_date(
                symbol=symbol,
                date=date,
                bar=self.rule.BAR,
                valid_interval=True,
                valid_start=True,
                valid_end=True
            )
            # 下载状态码 this_code
            this_code = get_history_candle_by_date_result['code']
            # 下载异常
            if this_code != 200:
                msg = '[get_history_candle_by_date] code={code} symbol={symbol} date={date} bar={bar} msg={msg}'.format(
                    code=this_code,
                    symbol=symbol,
                    date=date_str,
                    bar=self.rule.BAR,
                    msg=get_history_candle_by_date_result['msg']
                )
                # info 长度问题与起始错误，数据不足，过滤
                if this_code in [code.CANDLE_LENGTH_ERROR[0], code.CANDLE_START_ERROR[0]]:
                    self._download_filter.set(name=symbol, filter_minute=1440)
                    self.log.warn(msg)
                    download_detail['warn'] += 1
                # error 数据间隔错误 或者 终止时间 过滤
                elif this_code in [code.CANDLE_INTERVAL_ERROR[0], code.CANDLE_END_ERROR[0]]:
                    self._download_filter.set(name=symbol, filter_minute=1440)
                    self.log.error(msg)
                    download_detail['error'] += 1
                # error 其他状态码错误 不过滤
                else:
                    self.log.error(msg)
            # 历史K线数据合规 保存
            else:
                candle = get_history_candle_by_date_result['data']
                self.binanceLite.save_candle_by_date(
                    candle=candle,
                    instType=self.instType,
                    symbol=symbol,
                    start=date,
                    end=date,
                    bar=self.rule.BAR,
                )
                msg = 'DOWNLOAD {symbol:<10} {bar:<3} {date}'.format(
                    symbol=symbol,
                    bar=self.rule.BAR,
                    date=date_str,
                )
                self.log.info(msg)
                download_detail['suc'] += 1
            # 延时
            finish_time = time.time()  # 结束的时间戳
            request_seconds = (finish_time - request_time)  # 请求花费的时间戳
            # 现货交易
            if self.instType.upper() == 'SPOT':
                # 下载一天的数据需要花费权重2 总权重1200 单次延时为 2 / (1200 * SERVER_WEIGHT)
                delay = 60 * 2 / (1200 * self.rule.SERVER_WEIGHT) - request_seconds
                # delay = 2 / (1200 * self.rule.SERVER_WEIGHT)
            else:
                # 下载一天的数据需要花费权重10 总权重2400 单次延时为 10 / (2400 * SERVER_WEIGHT)
                delay = 60 * 10 / (2400 * self.rule.SERVER_WEIGHT) - request_seconds
                # delay = 10 / (2400 * self.rule.SERVER_WEIGHT)
            delay = round(delay, 4)
            if delay > 0:
                time.sleep(delay)
            # pass
        msg = 'COMPLETE DOWNLOAD {date} (ALL:{all} SKIP:{skip} SUC:{suc} WARN:{warn} ERROR:{error})'.format(
            date=date_str,
            **download_detail,
        )
        self.log.info(msg)

    def prepare_candle_map(self):
        # 历史K线最新毫秒时间戳 -> latest_ts
        latest_ts_result = self.market.get_history_candle_latest_ts(bar=self.rule.BAR)
        # **[ERROR RAISE]** 获取失败
        if latest_ts_result['code'] != 200:
            msg = '[get_history_candle_latest] code={code} msg={msg}'.format(
                code=latest_ts_result['code'],
                msg=latest_ts_result['msg'],
            )
            raise exception.CodeException(msg)
        latest_ts = latest_ts_result['data']
        # start_ts
        start_ts = float(latest_ts - _interval.get_interval(bar=self.rule.BAR) * (self.rule.LENGTH - 1))
        # 本地date数据的起始日期start_date与终止日期end_date
        start_date = _date.to_datetime(date=start_ts, timezone=self.rule.TIMEZONE).date()
        end_date = pendulum.yesterday(tz=self.rule.TIMEZONE).date()
        # 产品 -> symbols
        get_symbols_filtered_result = self.get_symbols_filtered()
        # **[ERROR RAISE]** 获取失败
        if get_symbols_filtered_result['code'] != 200:
            msg = '[get_symbols_filtered] code={code} msg={msg}'.format(
                msg=get_symbols_filtered_result['msg'],
                code=get_symbols_filtered_result['code'],
            )
            self.log.error(msg)
            raise exception.CodeException(msg)
        symbols = get_symbols_filtered_result['data']
        # candle_map
        candle_map = {}
        # 逐个产品遍历
        for symbol in symbols:
            # 是否有缓存
            if self.binanceLite.check_candle_file_path(
                    instType=self.instType,
                    symbol=symbol,
                    bar=self.rule.BAR,
            )['code']:
                # 尝试读取缓存
                try:
                    # 缓存数据
                    candle_cache = self.binanceLite.load_candle_by_file(
                        instType=self.instType,
                        symbol=symbol,
                        path=None,
                        bar=self.rule.BAR,
                        valid_interval=True,
                    )
                    # 按照时间截取
                    candle_cache_transformed = candle_cache[
                        (candle_cache[:, 0] >= start_ts) & (candle_cache[:, 0] <= latest_ts)
                        ]
                    # 如果截取后数据不为空，使用缓存
                    if candle_cache_transformed.shape[0] > 0:
                        candle_map[symbol] = candle_cache_transformed
                        continue
                # 有缓存但读取失败 -> 继续尝试从date数据中读取
                except:
                    msg = f'[load_candle_by_file] symbol={symbol}'
                    self.log.error(msg)
            # 无缓存或者缓存文件读取失败
            # 是否有date数据
            if self.binanceLite.check_candle_date_path(
                    instType=self.instType,
                    symbol=symbol,
                    start=start_date,
                    end=end_date,
                    bar=self.rule.BAR,
            )['code']:
                # 尝试读取date数据
                try:
                    # date数据
                    candle_date = self.binanceLite.load_candle_by_date(
                        instType=self.instType,
                        symbol=symbol,
                        start=start_date,
                        end=end_date,
                        bar=self.rule.BAR,
                        valid_interval=True,
                        valid_start=True,
                        valid_end=True,
                    )
                    # 时间截取
                    candle_date_transformed = candle_date[
                        (candle_date[:, 0] >= start_ts) & (candle_date[:, 0] <= latest_ts)
                        ]
                    # 如果截取后数据不为空，使用此数据
                    if candle_date_transformed.shape[0] > 0:
                        candle_map[symbol] = candle_date_transformed
                        continue
                # 有date数据但是读取失败
                except:
                    msg = '[load_candle_by_date] symbol={symbol} start_date={start_date} end_date={end_date}'.format(
                        symbol=symbol,
                        start_date=str(start_date),
                        end_date=str(end_date),
                    )
                    self.log.error(msg)
        # 连续两次将candle_map更新到最新
        for i in range(2):
            candle_map = self.update_candle(candle_map)
        return candle_map

    def update_candle(self, candle_map=None):
        # 优先级 candle_map >> self.candle_map
        if candle_map == None:
            if hasattr(self, 'candle_map'):
                candle_map = self.candle_map
            # [ERROR RAISE] 没有candle_map和self.candle_map
            else:
                msg = 'candle_map and self.candle_map can not be empty together'
                raise exception.ParamException(msg)
        # 历史K线最新毫秒时间戳 -> latest_ts
        latest_ts_result = self.market.get_history_candle_latest_ts(bar=self.rule.BAR)
        if latest_ts_result['code'] != 200:
            msg = '[get_history_candle_latest_ts] code={code} msg={msg}'.format(
                code=latest_ts_result['code'],
                msg=latest_ts_result['msg'],
            )
            raise exception.CodeException(msg)
        latest_ts = latest_ts_result['data']
        # 获取过滤后的产品 -> symbols
        get_symbols_filtered_result = self.get_symbols_filtered()
        if get_symbols_filtered_result['code'] != 200:
            msg = '[get_symbols_filtered] code={code} msg={msg}'.format(
                msg=get_symbols_filtered_result['msg'],
                code=get_symbols_filtered_result['code'],
            )
            self.log.error(msg)
            raise exception.CodeException(msg)
        symbols = get_symbols_filtered_result['data']
        # 逐个产品遍历
        for symbol in symbols:
            candle = candle_map[symbol] if symbol in candle_map.keys() else None
            if isinstance(candle, np.ndarray) and candle.shape[0] > 0 and candle[-1, 0] == latest_ts:
                continue
            update_history_candle_result = self.market.update_history_candle(
                symbol=symbol,
                length=self.rule.LENGTH,
                candle=candle,
                end=latest_ts,
                bar=self.rule.BAR,
                valid_interval=True,
            )
            this_code = update_history_candle_result['code']
            if this_code != 200:
                if this_code == code.CANDLE_END_ERROR:
                    # 允许更新后的candle与最新时间相差1个时间粒度
                    try:
                        if latest_ts - candle[-1, 0] <= _interval.get_interval(self.rule.BAR):
                            continue
                    except:
                        pass
                msg = '[update_history_candle] code={code} symbol={symbol} msg={msg}'.format(
                    symbol=symbol,
                    code=this_code,
                    msg=update_history_candle_result['msg']
                )
                if this_code == code.CANDLE_LENGTH_ERROR[0]:
                    self.filter.set(name=symbol, filter_minute=60 + random.randint(1, 10))
                    self.log.warn(msg)
                elif this_code == code.CANDLE_INTERVAL_ERROR[0]:
                    self.filter.set(name=symbol, filter_minute=1440 + random.randint(1, 10))
                    self.log.error(msg)
                else:
                    self.log.error(msg)
                if symbol in candle_map.keys():
                    del candle_map[symbol]
            else:
                candle_map[symbol] = update_history_candle_result['data']
        return candle_map

    # 多线程更新candle_map
    @_thread.thread_wrapper
    def thread_update_candle_map(self):
        while True:
            # 退出条件
            if self.__close_run_candle_map_signal == True:
                break
            # 更新数据
            try:
                if not hasattr(self, 'candle_map'):
                    self.candle_map = {}
                candle_map = self.update_candle(candle_map=self.candle_map)
                self.candle_map = candle_map
            except:
                msg = '[thread: update_candle]'
                self.log.error(msg)
            else:
                # 如果需要保存缓存
                if self.rule.CACHE_DELAY_SECONDS:
                    # 按时保存缓存
                    try:
                        # 没有上次缓存时间或者超过CACHE_DELAY_SECONDS
                        if (
                                (not hasattr(self, '__last_cache_candle_time'))
                                or
                                (time.time() - getattr(self,
                                                       '__last_cache_candle_time') >= self.rule.CACHE_DELAY_SECONDS)
                        ):
                            self.binanceLite.save_candle_map_by_file(
                                candle_map=self.candle_map,
                                instType=self.instType,
                                symbols=[],
                                replace=True,
                                bar=self.rule.BAR,
                            )
                            setattr(self, '__last_cache_candle_time', time.time())
                            msg = 'DOWNLOAD CANDLE CACHE'
                            self.log.info(msg)
                    except:
                        msg = '[thread: save_candle_map_by_file]'
                        self.log.error(msg)
                # 如果需要每天下载date数据
                if self.rule.DOWNLOAD_TIME and pendulum.now(self.rule.TIMEZONE).time().strftime(
                        '%H:%M:%S') >= self.rule.DOWNLOAD_TIME:
                    try:
                        # 没有上次下载日期或者距离上次下载日期超过1天
                        if (
                                (not hasattr(self, '__last_download_candle_date'))
                                or
                                ((pendulum.now(tz=self.rule.TIMEZONE).date() - getattr(self,
                                                                                       '__last_download_candle_date')).days >= 1)
                        ):
                            self.binanceLite.save_candle_map_by_date(
                                candle_map=self.candle_map,
                                instType=self.instType,
                                symbols=[],
                                replace=False,
                                start=pendulum.yesterday(tz=self.rule.TIMEZONE),
                                end=pendulum.yesterday(tz=self.rule.TIMEZONE),
                                bar=self.rule.BAR,
                            )
                            setattr(self, '__last_download_candle_date', pendulum.now(tz=self.rule.TIMEZONE).date())
                            msg = 'DOWNLOAD CANDLE BY DATE'
                            self.log.info(msg)
                    except:
                        msg = '[thread: save_candle_map_by_date]'
                        self.log.error(msg)
            finally:
                time.sleep(self.rule.UPDATE_INTERVAL_SECONDS)
        self.__close_run_candle_map_signal = False

    # 运行服务
    def run_candle_map(self):
        # 有正在运行的run线程
        if self._run_candle_map_thread and self._run_candle_map_thread.isAlive():
            msg = 'Server run thread is running. Cannot run repeatedly.'
            print(msg)
            return None
        # 补充date数据
        if self.rule.LOCAL_CANDLE_DAYS:
            self.download_candles_by_date(
                start=pendulum.now(tz=self.rule.TIMEZONE) - datetime.timedelta(days=self.rule.LOCAL_CANDLE_DAYS),
                end=pendulum.yesterday(tz=self.rule.TIMEZONE),
            )
        # 准备candle_map
        self.candle_map = self.prepare_candle_map()
        msg = 'COMPLETE PREPARE candle_map'
        self.log.info(msg)
        # 多线程更新candle_map
        t = self.thread_update_candle_map()
        self._run_candle_map_thread = t
        time.sleep(1)

    def close_run_candle_map(self):
        if self._run_candle_map_thread:
            self.__close_run_candle_map_signal = True
        else:
            msg = 'run_candle_map is not running'
            print(msg)

    def close_download_daily(self):
        if self._download_daily_thread:
            self.__close_download_daily_thread = True
        else:
            msg = 'download_daily is not running'
            print(msg)

    # 每天定时下载以天为单位的历史数据
    @_thread.thread_wrapper
    def _download_daily(
            self,
            start: Union[str, int, float, datetime.date, None] = None,
            replace: bool = False,
            type='trading_on',
    ):
        # 下载补充数据
        yesterday = pendulum.yesterday(tz=self.rule.TIMEZONE)
        last_day = yesterday
        # 如果有start 下载start ~ yesterday的数据
        if start == None:
            start = yesterday
        # v1.0.7 防止下载start~yesterday的时间过长，中间的数据缺失
        while True:
            self.download_candles_by_date(start=start, end=yesterday, replace=replace, type=type)
            if pendulum.yesterday(tz=self.rule.TIMEZONE) == yesterday:
                break
            else:
                yesterday = pendulum.yesterday(tz=self.rule.TIMEZONE)

        while True:
            if self.__close_download_daily_thread == True:
                break
            time.sleep(0.5)
            # 下载的时间条件
            if not pendulum.now(tz=self.rule.TIMEZONE).time().strftime('%H:%M:%S') >= self.rule.DOWNLOAD_TIME:
                continue
            # 下载的日期条件
            yesterday = pendulum.yesterday(tz=self.rule.TIMEZONE)
            if (yesterday - last_day).days > 0:
                self.download_candles_by_date(
                    start=yesterday,
                    end=yesterday,
                    type=type,
                )
                last_day = yesterday
        self.__close_download_daily_thread = False

    def download_daily(self,
                       start: Union[str, int, float, datetime.date, None] = None,
                       replace: bool = False,
                       type='trading_on',
                       ):
        '''
        :param start: 起始日期
            start != None 补充下载start ~ yesterday 的历史K线数据
        :param replace: 是否替换本地数据
        :param type: 产品交易类型
            trading_on      正在交易的产品
            trading_off     不可交易的产品
            trading_all     全部产品
        '''
        if self._download_daily_thread and self._download_daily_thread.isAlive():
            msg = 'Server download daily thread is running. Cannot run repeatedly.'
            print(msg)
            return None
        t = self._download_daily(start=start, replace=replace, type=type)
        self._download_daily_thread = t
        time.sleep(1)

    # 获得candle的最新时间与当前时间查小于security_seconds的k线数据
    def get_candle_security(self, symbol: str, security_seconds=60 * 3) -> np.ndarray:
        '''
        :param symbol: 产品
        :param security_seconds: 与当前时间戳相差多少以内判定为安全
        '''
        # 不存在
        if symbol not in self.candle_map.keys():
            return np.array([])
        candle = self.candle_map[symbol]
        # 是否与此时时间相差超过了security_seconds
        if (time.time() * 1000 - candle[-1, 0]) >= security_seconds * 1000:
            return np.array([])
        return candle
