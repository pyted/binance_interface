from binance_interface.api.spot import SPOT  # 现货
from binance_interface.api.margin import Margin  # 杠杆
from binance_interface.api.um import UM  # U本位合约
from binance_interface.api.cm import CM  # 币本位合约
from binance_interface.api.eo import EO  # 欧式期权
from binance_interface.api.pm import PM  # 统一账户
from binance_interface.api.other import Other  # 其他


class Binance():
    def __init__(self, key='', secret='', proxies={}, proxy_host: str = None):
        self.spot = SPOT(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.margin = Margin(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.um = UM(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.cm = CM(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.eo = EO(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.pm = PM(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        self.other = Other(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)


BinanceInterface = Binance
API = Binance