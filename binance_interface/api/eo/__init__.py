'''
欧式期权
https://binance-docs.github.io/apidocs/voptions/cn/
'''
from binance_interface.api.eo.eo_market import EOMarket  # 行情接口
from binance_interface.api.eo.eo_account_trade import EOAccountTrade  # 账户和交易接口
from binance_interface.api.eo.eo_market_maker import EOMarketMaker  # 做市商接口

Market = EOMarket
AccountTrade = EOAccountTrade
MarketMaker = EOMarketMaker


class EO():
    def __init__(self, key='', secret='', proxies={}, proxy_host: str = None):
        self.market = EOMarket(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.accountTrade = EOAccountTrade(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.marketMaker = EOMarketMaker(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
