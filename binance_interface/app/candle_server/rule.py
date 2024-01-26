from typing import Union
from candlelite.crypto.binace_lite import (
    BINANCE_TIMEZONE,  # 历史K线默认时区
    BINANCE_CANDLE_DATE_BASE_DIR,  # 历史K线以日期为单位的默认存储路径
    BINANCE_DEFAULT_BAR,  # 历史K线默认时间粒度
)


class CandleRule():
    # 服务占用权重上限的比例 现货交易权重上限1200 合约交易权重上限2400
    SERVER_WEIGHT = 0.75
    # 收集的产品 all表示全部正在交易的产品
    SYMBOLS: Union[str, list] = 'all'
    # 过滤的产品
    SYMBOLS_FILTER: list = []
    # 产品名称中需要包含的内容
    SYMBOL_CONTAINS = ''
    # 产品名称必须以何内容结尾
    SYMBOL_ENDSWITH = ''
    # candle_map 更新时间间隔（秒）
    UPDATE_INTERVAL_SECONDS: int = 3
    # candle_map 缓存K线数据长度
    LENGTH: int = 1440 * 2
    # 时间颗粒度
    BAR: str = BINANCE_DEFAULT_BAR
    # candle_map 保存缓存文件时间间隔（秒） None：不保存缓存
    CACHE_DELAY_SECONDS: Union[int, None] = 60 * 60
    # 服务启动 需维护本地多少天的历史K线数据
    LOCAL_CANDLE_DAYS: int = 2
    # 每日下载昨日历史K线数据的时刻 格式：%H:%M:%S None表示不下载
    DOWNLOAD_TIME: Union[str,None] = '00:10:00'
    # 以天为单位的数据存储路径
    CANDLE_DIR = BINANCE_CANDLE_DATE_BASE_DIR
    # 缓存数据路径
    CACHE_DIR = './BINANCE_CACHE'
    # 时区
    TIMEZONE = BINANCE_TIMEZONE
    # KEY 通常无需填写
    KEY: str = None
    # SECRET 通常无需填写
    SECRET: str = None
    # 日志文件夹
    LOG_DIRPATH = './BINANCE_CANDLE_SERVER_LOG_DATA'
    # 日志文件级别
    LOG_FILE_LEVEL = 'INFO'
    # 日志打印级别
    LOG_CONSOLE_LEVEL = 'DEBUG'
