'''
统一账户
https://binance-docs.github.io/apidocs/pm/cn/
'''

from binance_interface.api.pm.pm_market import PMMarket  # 行情接口
from binance_interface.api.pm.pm_account import PMAccount  # 账户信息
from binance_interface.api.pm.pm_get_order import PMGetOrder  # 查询订单
from binance_interface.api.pm.pm_set_order import PMSetOrder  # 下单接口
from binance_interface.api.pm.pm_cancel_order import PMCancelOrder  # 撤单接口

Market = PMMarket
Account = PMAccount
GetOrder = PMGetOrder
SetOrder = PMSetOrder
CancelOrder = PMCancelOrder


class PM():
    def __init__(self, key='', secret='', proxies={}, proxy_host: str = None):
        self.market = PMMarket(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.account = PMAccount(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.getOrder = PMGetOrder(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.setOrder = PMSetOrder(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.cancelOrder = PMCancelOrder(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
