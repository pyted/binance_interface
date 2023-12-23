'''
其他
https://binance-docs.github.io/apidocs/spot/cn/
'''

from binance_interface.api.other.auto_invest import AutoInvest  # 定投接口
from binance_interface.api.other.bs_wap import BsWap  # 币安挖矿接口
from binance_interface.api.other.c2c import C2C  # C2C 接口
from binance_interface.api.other.convert import Convert  # 闪兑接口
from binance_interface.api.other.crypto_loans import CryptoLoans  # 质押借币接口
from binance_interface.api.other.fiat import Fiat  # 法币接口
from binance_interface.api.other.futures import Futures  # 合约接口
from binance_interface.api.other.futures_algo import FuturesAlgo  # 合约策略交易接口
from binance_interface.api.other.gift_card import GiftCard  # 币安礼品卡接口
from binance_interface.api.other.mining import Mining  # 矿池接口
from binance_interface.api.other.nft import Nft  # NFT 接口
from binance_interface.api.other.pay import Pay  # Pay 接口
from binance_interface.api.other.portfolio import Portfolio  # 经典统一账户接口
from binance_interface.api.other.rebate import Rebate  # 返佣接口
from binance_interface.api.other.simple_earn import SimpleEarn  # 赚币接口
from binance_interface.api.other.sub_account import SubAccount  # 子母账户接口
from binance_interface.api.other.vip_loans import VipLoans  # VIP借币接口
from binance_interface.api.other.wallet import Wallet  # 钱包接口


class Other():
    def __init__(self, key='', secret='', proxies={}, proxy_host: str = None):
        self.autoInvest = AutoInvest(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)  # 定投接口
        self.bsWap = BsWap(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)  # 币安挖矿接口
        self.c2c = C2C(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)  # C2C 接口
        self.convert = Convert(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)  # 闪兑接口
        self.cryptoLoans = CryptoLoans(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)  # 质押借币接口
        self.fiat = Fiat(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)  # 法币接口
        self.futures = Futures(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)  # 合约接口
        self.futuresAlgo = FuturesAlgo(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)  # 合约策略交易接口
        self.giftCard = GiftCard(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)  # 币安礼品卡接口
        self.mining = Mining(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)  # 矿池接口
        self.nft = Nft(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)  # NFT 接口
        self.pay = Pay(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)  # Pay 接口
        self.portfolio = Portfolio(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)  # 经典统一账户接口
        self.rebate = Rebate(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)  # 返佣接口
        self.simpleEarn = SimpleEarn(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)  # 赚币接口
        self.subAccount = SubAccount(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)  # 子母账户接口
        self.vipLoans = VipLoans(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)  # VIP借币接口
        self.wallet = Wallet(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)  # 钱包接口
