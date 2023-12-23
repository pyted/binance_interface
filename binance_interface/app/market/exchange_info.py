import time
from binance_interface.app import code
from binance_interface.app.market._base import MarketBase

__all__ = ['ExchangeInfo']


# 交易规则与交易对信息
class ExchangeInfo(MarketBase):
    '''
    现货
        https://binance-docs.github.io/apidocs/spot/cn/#e7746f7d60
    U本位合约
        https://binance-docs.github.io/apidocs/futures/cn/#0f3f2d5ee7
    币本位合约
        https://binance-docs.github.io/apidocs/delivery/cn/#185368440e
    '''

    # 通过缓存获取交易规则与交易对
    # Weight: 现货10 合约1 使用缓存0
    def get_exchangeInfos(
            self,
            expire_seconds: int = 60 * 5
    ) -> dict:
        '''
        :param expire_seconds: 缓存时间（秒）


        使用的缓存数据格式：
            self._exchangeInfo_cache = [
                {
                    'code':<状态码>,
                    'data':<exchangeInfo数据>,
                    'msg':<提示信息>,
                },
                <上次更新的毫秒时间戳>
            ]
        '''
        if (
                # 无缓存数据
                not hasattr(self, '_exchangeInfo_caches')
                or
                # 缓存数据过期
                getattr(self, '_exchangeInfo_caches')[1] - time.time() * 1000 >= expire_seconds
        ):
            # 更新数据并设置时间戳
            setattr(self, '_exchangeInfo_caches', [self.marketAPI.get_exchangeInfo(), time.time() * 1000])
        # 返回缓存数据
        return getattr(self, '_exchangeInfo_caches')[0]

    # 获取一个产品的交易规则与交易对
    # Weight: 现货10 合约1 使用缓存0
    def get_exchangeInfo(
            self,
            symbol: str,
            expire_seconds: int = 60 * 5,
    ) -> dict:
        '''
        :param symbol: 产品
        :param expire_seconds: 缓存时间（秒）
        '''
        exchangeInfos_result = self.get_exchangeInfos(expire_seconds)
        # [ERROR RETURN] 异常交易规则与交易
        if exchangeInfos_result['code'] != 200:
            return exchangeInfos_result
        # 寻找symbol的信息
        for symbol_data in exchangeInfos_result['data']['symbols']:
            if symbol_data['symbol'] == symbol:
                symbol_data = symbol_data
                break
        else:
            symbol_data = None
        # [ERROR RETURN] 没有找到symbol的交易规则与交易对信息
        if symbol_data == None:
            result = {
                'code': code.EXCHANGE_INFO_ERROR[0],
                'data': exchangeInfos_result['data'],
                'msg': f'Symbol not found symbol={symbol}'
            }
            return result
        # 将filters中的列表转换为字典，里面可能包含下单价格与数量精度
        symbol_data['filter'] = {}
        for filter_data in symbol_data['filters']:
            symbol_data['filter'][
                filter_data['filterType']
            ] = filter_data
        # [RETURN]
        result = {
            'code': 200,
            'data': symbol_data,
            'msg': '',
        }
        return result

    # 获取可以交易的产品列表
    # Weight: 现货10 合约1 使用缓存0
    def get_symbols_trading_on(
            self,
            expire_seconds: int = 60 * 5
    ) -> dict:
        '''
        :param expire_seconds: 缓存时间（秒）
        '''
        exchangeInfos_result = self.get_exchangeInfos(expire_seconds)
        # [ERROR RETURN] 异常交易规则与交易
        if exchangeInfos_result['code'] != 200:
            return exchangeInfos_result
        # 正在交易的产品名称 status == 'TRADING'
        if self.instType == 'CM':  # 币本位合约交易的状态名称特殊
            status_name = 'contractStatus'
        else:
            status_name = 'status'
        symbols = [
            data['symbol']
            for data in exchangeInfos_result['data']['symbols']
            if data[status_name] == 'TRADING'
        ]
        # [RETURN]
        result = {
            'code': 200,
            'data': symbols,
            'msg': ''
        }
        return result

    # 获取不可交易的产品列表
    # Weight: 现货10 合约1 使用缓存0
    def get_symbols_trading_off(
            self,
            expire_seconds: int = 60 * 5
    ) -> dict:
        '''
        :param expire_seconds: 缓存时间（秒）
        '''

        exchangeInfos_result = self.get_exchangeInfos(expire_seconds)
        # [ERROR RETURN] 异常交易规则与交易
        if exchangeInfos_result['code'] != 200:
            return exchangeInfos_result
        # 不可交易的产品名称 status != 'TRADING'
        if self.instType == 'CM':  # 币本位合约交易的状态名称特殊
            status_name = 'contractStatus'
        else:
            status_name = 'status'

        symbols = [
            data['symbol']
            for data in exchangeInfos_result['data']['symbols']
            if data[status_name] != 'TRADING'
        ]
        # [RETURN]
        result = {
            'code': 200,
            'data': symbols,
            'msg': ''
        }
        return result

    # 获取全部的产品列表
    # Weight: 现货10 合约1 使用缓存0
    def get_symbols_all(
            self,
            expire_seconds: int = 60 * 5
    ) -> dict:
        '''
        :param expire_seconds: 缓存时间（秒）
        '''

        exchangeInfos_result = self.get_exchangeInfos(expire_seconds)
        # [ERROR RETURN] 异常交易规则与交易
        if exchangeInfos_result['code'] != 200:
            return exchangeInfos_result
        symbols = [
            data['symbol']
            for data in exchangeInfos_result['data']['symbols']
        ]
        # [RETURN]
        result = {
            'code': 200,
            'data': symbols,
            'msg': ''
        }
        return result
