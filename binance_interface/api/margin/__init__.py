'''
杠杆
https://binance-docs.github.io/apidocs/spot/cn/
'''

from binance_interface.api.margin.margin_account_trade import MarginAccountTrade  # 杠杆账户和交易接口
from binance_interface.api.margin.margin_blvt import MarginBlvt  # 杠杆代币接口

AccountTrade = MarginAccountTrade
Blvt = MarginBlvt


class Margin():
    def __init__(self, key='', secret='', proxies={}, proxy_host: str = None):
        self.blvt = MarginBlvt(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.accountTrade = MarginAccountTrade(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
