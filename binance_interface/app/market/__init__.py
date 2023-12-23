from binance_interface.app.market.ticker import Ticker # 实时价格
from binance_interface.app.market.history_candle import HistoryCandle # 历史K线
from binance_interface.app.market.exchange_info import ExchangeInfo # 交易对信息

__all__ = ['Market', 'MarketSPOT', 'MarketUM', 'MarketCM']


class Market(HistoryCandle, Ticker, ExchangeInfo):
    pass


class MarketSPOT(Market):
    def __init__(self, key: str = '', secret: str = '', timezone: str = 'America/New_York', proxies={}, proxy_host: str = None, ):
        instType = 'SPOT'
        super(MarketSPOT, self).__init__(instType=instType, key=key, secret=secret, timezone=timezone, proxies=proxies, proxy_host=proxy_host)


class MarketUM(Market):
    def __init__(self, key: str = '', secret: str = '', timezone: str = 'America/New_York',proxies={}, proxy_host: str = None, ):
        instType = 'UM'
        super(MarketUM, self).__init__(instType=instType, key=key, secret=secret, timezone=timezone, proxies=proxies, proxy_host=proxy_host)


class MarketCM(Market):
    def __init__(self, key: str = '', secret: str = '', timezone: str = 'America/New_York',proxies={}, proxy_host: str = None, ):
        instType = 'CM'
        super(MarketCM, self).__init__(instType=instType, key=key, secret=secret, timezone=timezone, proxies=proxies, proxy_host=proxy_host)
