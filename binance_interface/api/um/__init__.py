'''
U本位合约
https://binance-docs.github.io/apidocs/futures/cn/
'''

from binance_interface.api.um.um_account_trade import UMAccountTrade
from binance_interface.api.um.um_market import UMMarket
from binance_interface.api.um.um_portfolio import UMPortfolio

AccountTrade = UMAccountTrade
Market = UMMarket
Portfolio = UMPortfolio


class UM():
    def __init__(self, key='', secret='', proxies={}, proxy_host: str = None):
        self.accountTrade = UMAccountTrade(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.market = UMMarket(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.portfolio = UMPortfolio(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
