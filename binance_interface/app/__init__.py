from binance_interface.app.account import AccountSPOT, AccountUM, AccountCM
from binance_interface.app.market import MarketSPOT, MarketUM, MarketCM
from binance_interface.app.trade import TradeSPOT, TradeUM, TradeCM


class BinanceSPOT():
    def __init__(self,
                 key: str,
                 secret: str,
                 timezone: str = 'America/New_York',
                 proxies={},
                 proxy_host: str = None,
                 ):
        self.account = AccountSPOT(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.market = MarketSPOT(key=key, secret=secret, timezone=timezone, proxies=proxies, proxy_host=proxy_host)
        self.trade = TradeSPOT(key=key, secret=secret, timezone=timezone, account=self.account, market=self.market,
                               proxies=proxies, proxy_host=proxy_host)
        self.timezone = timezone


class BinanceUM():
    def __init__(self,
                 key: str,
                 secret: str,
                 timezone: str = 'America/New_York',
                 proxies={},
                 proxy_host: str = None,
                 ):
        self.account = AccountUM(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.market = MarketUM(key=key, secret=secret, timezone=timezone, proxies=proxies, proxy_host=proxy_host)
        self.trade = TradeUM(key=key, secret=secret, timezone=timezone, account=self.account, market=self.market,
                               proxies=proxies, proxy_host=proxy_host)
        self.timezone = timezone


class BinanceCM():
    def __init__(self,
                 key: str,
                 secret: str,
                 timezone: str = 'America/New_York',
                 proxies={},
                 proxy_host: str = None,
                 ):
        self.account = AccountCM(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.market = MarketCM(key=key, secret=secret, timezone=timezone, proxies=proxies, proxy_host=proxy_host)
        self.trade = TradeCM(key=key, secret=secret, timezone=timezone, account=self.account, market=self.market,
                               proxies=proxies, proxy_host=proxy_host)
        self.timezone = timezone
