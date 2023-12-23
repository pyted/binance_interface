from typing import Union
from binance_interface.app.trade.trade_spot._base import TradeSPOTBase
from paux.param import to_local
import time


class TradeOrder(TradeSPOTBase):
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
            timeInForce: str = '',
            quantity: Union[float, int, str] = '',
            quoteOrderQty: Union[float, int, str] = '',
            price: Union[float, int, str] = '',
            newClientOrderId: str = '',
            stopPrice: Union[float, int, str] = '',
            trailingDelta: int = '',
            icebergQty: Union[float, int, str] = '',
            newOrderRespType: str = '',
            strategyId: int = '',
            strategyType: int = '',
            recvWindow: int = ''
    ):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade-3

        Name            	Type            	Mandatory	Description
        symbol          	str             	YES
        side            	str             	YES      	详见枚举定义：订单方向
        type            	str             	YES      	详见枚举定义：订单类型
        timeInForce     	str             	NO       	详见枚举定义：有效方式
        quantity        	Union[float,int]    NO
        quoteOrderQty   	Union[float,int]    NO
        price           	Union[float,int]    NO
        newClientOrderId	str             	NO       	客户自定义的唯一订单ID。 如果未发送，则自动生成
        stopPrice       	Union[float,int]	NO
        trailingDelta   	int             	NO
        icebergQty      	Union[float,int]	NO
        newOrderRespType	str             	NO       	设置响应JSON。 ACK，RESULT或FULL； "MARKET"和" LIMIT"订单类型默认为"FULL"，所有其他订单默认为"ACK"。
        strategyId      	int             	NO
        strategyType    	int             	NO
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

        return self.spotAPI.accountTrade.set_order(**to_local(locals()))

    # 查询订单 (USER_DATA) Weight : 2
    def get_order(
            self,
            symbol: str,
            orderId: int = '',
            origClientOrderId: str = '',
            recvWindow: int = ''
    ):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-20

        Name             	Type	Mandatory	Description
        symbol           	str 	YES
        orderId          	int 	NO
        origClientOrderId	str 	NO
        recvWindow       	int 	NO

        系统订单号和用户订单号不能同时为空
        请注意，如果订单满足如下条件，不会被查询到：
            订单的最终状态为 CANCELED 或者 EXPIRED
                并且
            订单没有任何的成交记录
                并且
            订单生成时间 + 7天 < 当前时间
        '''
        return self.spotAPI.accountTrade.get_order(**to_local(locals()))

    # 查看当前全部挂单 (USER_DATA) Weight 1 | 40
    def get_openOrders(
            self,
            symbol: str = '',
            recvWindow: int = ''
    ):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-21

        Name      	Type	Mandatory	Description
        symbol    	str 	NO
        recvWindow	int 	NO

        权重：
            带symbol 1
            不带symbol 40
        '''
        return self.spotAPI.accountTrade.get_openOrders(**to_local(locals()))

    # 查询当前挂单 (USER_DATA) Weight : 1
    def get_openOrder(
            self,
            symbol: str,
            recvWindow: int = ''
    ):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#user_data-21

        Name      	Type	Mandatory	Description
        symbol    	str 	NO
        recvWindow	int 	NO
        '''
        return self.spotAPI.accountTrade.get_openOrders(**to_local(locals()))

    # 撤销订单 (TRADE) Weight : 1
    def cancel_order(
            self,
            symbol: str,
            orderId: int = '',
            origClientOrderId: str = '',
            newClientOrderId: str = '',
            recvWindow: int = ''
    ):
        '''
        https://binance-docs.github.io/apidocs/spot/cn/#trade-4

        Name             	Type	Mandatory	Description
        symbol           	str 	YES      	交易对
        orderId          	int 	NO       	系统订单号
        origClientOrderId	str 	NO       	用户自定义的订单号
        newClientOrderId 	str 	NO       	用户自定义的本次撤销操作的ID(注意不是被撤销的订单的自定义ID)。如无指定会自动赋值。
        recvWindow       	int 	NO

        orderId 与 origClientOrderId 必须至少发送一个
        '''
        return self.spotAPI.accountTrade.cancel_order(**to_local(locals()))

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

