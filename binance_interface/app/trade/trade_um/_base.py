from binance_interface.app.account import AccountUM
from binance_interface.app.market import MarketUM
from binance_interface.api.um import UM


class TradeUMBase():
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
            self._account = AccountUM(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        else:
            self._account = account

        if not market:
            self._market = MarketUM(key=key, secret=secret, timezone=timezone, proxies=proxies, proxy_host=proxy_host)
        else:
            self._market = market
        self.timezone = timezone
        self.umAPI = UM(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
