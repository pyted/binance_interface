from binance_interface.app.account import AccountCM
from binance_interface.app.market import MarketCM
from binance_interface.api.cm import CM


class TradeCMBase():
    def __init__(
            self,
            key: str,
            secret: str,
            timezone: str = 'America/New_York',
            account=None,
            market=None,
            proxies={},
            proxy_host: str = None,
    ):
        if not account:
            self._account = AccountCM(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        else:
            self._account = account

        if not market:
            self._market = MarketCM(key=key, secret=secret, timezone=timezone, proxies=proxies, proxy_host=proxy_host)
        else:
            self._market = market
        self.timezone = timezone
        self.cmAPI = CM(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
