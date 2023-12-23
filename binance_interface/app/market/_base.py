from typing import Literal
from binance_interface.app import exception
from binance_interface.api.spot.spot_market import SPOTMarket
from binance_interface.api.um.um_market import UMMarket
from binance_interface.api.cm.cm_market import CMMarket
from binance_interface.api.eo.eo_market import EOMarket


# 市场信息基类
class MarketBase():

    def __init__(
            self,
            instType: Literal['SPOT', 'UM', 'CM'],
            key: str = '',
            secret: str = '',
            timezone='America/New_York',
            proxies={},
            proxy_host: str = None,
    ):
        '''
        主要为了处理inst
            instType = 'SPOT'   self.inst -> self.spot
            instType = 'UM'     self.inst -> self.um
            instType = 'CM'     self.inst -> self.cm

        :param instType: 产品类型
            SPOT:   现货
            UM:     U本位合约
            CM:     币本位合约
        :param key: API KEY 可以不填写
        :param secret: API SECRET 可以不填写
        :param timezone: 时区
            America/New_York:   美国时间
            Asia/Shanghai:      中国时间
        '''
        # 时区与产品类别
        self.timezone = timezone
        self.instType = instType.upper()
        # inst
        if self.instType == 'SPOT':  # 现货交易
            self.marketAPI = SPOTMarket(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        elif self.instType == 'UM':  # U本位
            self.marketAPI = UMMarket(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        elif self.instType == 'CM':  # 币本位
            self.marketAPI = CMMarket(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)
        else:
            msg = '[instType error] your input instType={instType} instType must in ["SPOT","UM","CM"]'.format(
                instType=str(instType)
            )
            raise exception.ParamException(msg)
