'''
U本位合约
https://binance-docs.github.io/apidocs/futures/cn/
'''

from binance_interface.api.um.um_account_trade import UMAccountTrade # 账户和交易接口
from binance_interface.api.um.um_market import UMMarket # 行情接口
from binance_interface.api.um.um_portfolio import UMPortfolio # 经典统一账户

AccountTrade = UMAccountTrade
Market = UMMarket
Portfolio = UMPortfolio


class UM():
    def __init__(self, key='', secret='', proxies={}, proxy_host: str = None):
        self.accountTrade = UMAccountTrade(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.market = UMMarket(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.portfolio = UMPortfolio(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
