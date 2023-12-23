'''
币本位合约
https://binance-docs.github.io/apidocs/delivery/cn/
'''
from binance_interface.api.cm.cm_market import CMMarket  # 行情接口
from binance_interface.api.cm.cm_account_trade import CMAccountTrade  # 账户和交易接口
from binance_interface.api.cm.cm_portfolio import CMPortfolio  # 经典统一账户接口

Market = CMMarket
AccountTrade = CMAccountTrade
Portfolio = CMPortfolio


class CM():
    def __init__(self, key='', secret='', proxies={}, proxy_host: str = None):
        self.market = CMMarket(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.accountTrade = CMAccountTrade(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.portfolio = CMPortfolio(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
