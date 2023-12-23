from typing import Literal, Union
from binance_interface.app.trade.trade_um._base import TradeUMBase
from paux.param import to_local
import time


class TradeOrder(TradeUMBase):
    # 订单状态
    class ORDER_STATUS():
        NEW = 'NEW'  # 新建订单
        PARTIALLY_FILLED = 'PARTIALLY_FILLED'  # 部分成交
        FILLED = 'FILLED'  # 全部成交
        CANCELED = 'CANCELED'  # 已撤销
        REJECTED = 'REJECTED'  # 订单被拒绝
        EXPIRED = 'EXPIRED'  # 订单过期(根据timeInForce参数规则)

    # 下单 (TRADE) Weight : 1
    def set_order(
            self,
            symbol: str,
            side: str,
            type: str,
            positionSide: str = '',
            reduceOnly: str = '',
            quantity: Union[float, int] = '',
            price: Union[float, int] = '',
            newClientOrderId: str = '',
            stopPrice: Union[float, int] = '',
            closePosition: str = '',
            activationPrice: Union[float, int] = '',
            callbackRate: Union[float, int] = '',
            timeInForce: str = '',
            workingType: str = '',
            priceProtect: str = '',
            newOrderRespType: str = '',
            recvWindow: int = ''
    ):
        '''
        https://binance-docs.github.io/apidocs/futures/cn/#trade-3

        Name            	Type            	Mandatory	Description
        symbol          	str             	YES      	交易对
        side            	str             	YES
        type            	str             	YES
        positionSide    	str             	NO
        reduceOnly      	str             	NO
        quantity        	Union[float,int]	NO
        price           	Union[float,int]	NO       	委托价格
        newClientOrderId	str             	NO
        stopPrice       	Union[float,int]	NO
        closePosition   	str             	NO
        activationPrice 	Union[float,int]	NO
        callbackRate    	Union[float,int]	NO
        timeInForce     	str             	NO       	有效方法
        workingType     	str             	NO
        priceProtect    	str             	NO
        newOrderRespType	str             	NO       	"ACK", "RESULT", 默认 "ACK"
        recvWindow      	int             	NO

        :param side: 买卖方向
            BUY:    购买
            SELL:   卖出
        :param timeInForce: 有效方法 限价单必须填写，市价单无需填写
            GTC:    成交为止, 一直有效
            IOC:    无法立即成交(吃单)的部分就撤销
            FOK:    无法全部立即成交就撤销
            GTX:    无法成为挂单方就撤销
        '''
        return self.umAPI.accountTrade.set_order(**to_local(locals()))

    # 查询订单 (USER_DATA) Weight : 2
    def get_order(
            self,
            symbol: str,
            orderId: int = '',
            origClientOrderId: str = '',
            recvWindow: int = ''
    ):
        '''
        https://binance-docs.github.io/apidocs/futures/cn/#user_data-3

        Name             	Type	Mandatory	Description
        symbol           	str 	YES      	交易对
        orderId          	int 	NO       	系统订单号
        origClientOrderId	str 	NO       	用户自定义的订单号
        recvWindow       	int 	NO

        系统订单号和用户订单号不能同时为空
        请注意，如果订单满足如下条件，不会被查询到：
            订单的最终状态为 CANCELED 或者 EXPIRED
                并且
            订单没有任何的成交记录
                并且
            订单生成时间 + 7天 < 当前时间
        '''
        return self.umAPI.accountTrade.get_order(**to_local(locals()))

    # 查看当前全部挂单 (USER_DATA) Weight 1 | 40
    def get_openOrders(
            self,
            symbol: str = '',
            recvWindow: int = ''
    ):
        '''
        https://binance-docs.github.io/apidocs/futures/cn/#user_data-5

        Name      	Type	Mandatory	Description
        symbol    	str 	NO       	交易对
        recvWindow	int 	NO

        权重：
            带symbol 1
            不带symbol 40
        '''
        return self.umAPI.accountTrade.get_openOrders(**to_local(locals()))

    # 查询当前挂单 (USER_DATA) Weight : 1
    def get_openOrder(
            self,
            symbol: str,
            orderId: int = '',
            origClientOrderId: str = '',
            recvWindow: int = ''
    ):
        '''
        https://binance-docs.github.io/apidocs/futures/cn/#user_data-4

        Name             	Type	Mandatory	Description
        symbol           	str 	YES      	交易对
        orderId          	int 	NO       	系统订单号
        origClientOrderId	str 	NO       	用户自定义的订单号
        recvWindow       	int 	NO
        '''
        return self.umAPI.accountTrade.get_openOrder(**to_local(locals()))

    # 撤销订单 (TRADE) Weight : 1
    def cancel_order(
            self,
            symbol: str,
            orderId: int = '',
            origClientOrderId: str = '',
            recvWindow: int = ''
    ):
        '''
        https://binance-docs.github.io/apidocs/futures/cn/#trade-6

        Name             	Type	Mandatory	Description
        symbol           	str 	YES      	交易对
        orderId          	int 	NO       	系统订单号
        origClientOrderId	str 	NO       	用户自定义的订单号
        recvWindow       	int 	NO

        orderId 与 origClientOrderId 必须至少发送一个
        '''
        return self.umAPI.accountTrade.cancel_order(**to_local(locals()))

    # 等待订单成交
    def wait_order_FILLED(self, symbol: str, orderId: int = '', origClientOrderId: str = '', timeout=60, delay=0.2):
        start_time = time.time()
        while True:
            # 查询订单
            order_result = self.get_order(symbol=symbol, orderId=orderId, origClientOrderId=origClientOrderId)
            # [ERROR_RETURN] code异常
            if order_result['code'] != 200:
                return order_result
            # [SUCCESS_RETURN] 全部成交
            if order_result['data']['status'] == self.ORDER_STATUS.FILLED:
                return order_result
            # [TIMEOUT_RETURN] 超时
            if time.time() - start_time >= timeout:
                return order_result
            time.sleep(delay)
