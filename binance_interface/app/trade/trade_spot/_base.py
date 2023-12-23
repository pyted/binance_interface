from binance_interface.app.account import AccountSPOT
from binance_interface.app.market import MarketSPOT
from binance_interface.api.spot import SPOT


class TradeSPOTBase():
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
            self._account = AccountSPOT(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        else:
            self._account = account

        if not market:
            self._market = MarketSPOT(key=key, secret=secret, timezone=timezone, proxies=proxies, proxy_host=proxy_host)
        else:
            self._market = market
        self.timezone = timezone
        self.spotAPI = SPOT(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
