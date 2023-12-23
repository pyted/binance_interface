'''
现货
https://binance-docs.github.io/apidocs/spot/cn/
'''
from binance_interface.api.spot.spot_algo import SPOTAlgo  # 现货策略交易接口
from binance_interface.api.spot.spot_trade import SPOTTrade  # 现货交易接口
from binance_interface.api.spot.spot_market import SPOTMarket  # 行情接口
from binance_interface.api.spot.spot_account import SPOTAccount  # 现货账户接口

Algo = SPOTAlgo
Trade = SPOTTrade
Market = SPOTMarket
Account = SPOTAccount


class SPOT():
    def __init__(self, key='', secret='', proxies={}, proxy_host: str = None):
        self.Algo = SPOTAlgo(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.trade = SPOTTrade(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.market = SPOTMarket(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.account = SPOTAccount(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
