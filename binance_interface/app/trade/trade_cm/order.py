from typing import Literal, Union
from binance_interface.app.trade.trade_cm._base import TradeCMBase
from paux.param import to_local
import time
import paux.date
import datetime
from binance_interface.app import exception


class TradeOrder(TradeCMBase):
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
        https://binance-docs.github.io/apidocs/delivery/cn/#trade-2

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
        return self.cmAPI.accountTrade.set_order(**to_local(locals()))

    # 查询订单 (USER_DATA) Weight : 2
    def get_order(
            self,
            symbol: str,
            orderId: int = '',
            origClientOrderId: str = '',
            recvWindow: int = ''
    ):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#user_data-3

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
        return self.cmAPI.accountTrade.get_order(**to_local(locals()))

    # 查看当前全部挂单 (USER_DATA) Weight 1 | 40
    def get_orders_pending(
            self,
            symbol: str = '',
            pair: str = '',
            start: Union[str, int, float, datetime.datetime] = '',
            end: Union[str, int, float, datetime.datetime] = '',
            recvWindow: int = ''
    ):
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#user_data-5

        Name      	Type	Mandatory	Description
        symbol    	str 	NO       	交易对
        pair      	str 	NO       	标的交易对

        权重：
            带symbol 1
            不带symbol 40
        '''
        result = self.cmAPI.accountTrade.get_openOrders(symbol=symbol, pair=pair, recvWindow=recvWindow)
        if not result['code'] == 200:
            return result
        if start:
            start = paux.date.to_ts(start, timezone=self.timezone)
        if end:
            end = paux.date.to_ts(end, timezone=self.timezone)
        data2 = []
        for data in result['data']:
            if start and not data['time'] >= start:
                continue
            if end and not data['time'] <= end:
                continue
            data2.append(data)
        result['data'] = data2
        return result

    def get_orders_pending_open(
            self,
            symbol: str = '',
            pair: str = '',
            positionSide: str = '',
            start: Union[str, int, float, datetime.datetime] = '',
            end: Union[str, int, float, datetime.datetime] = '',
            recvWindow: int = '',
    ):

        # 验证positionSide
        positionSide = positionSide.upper()
        if positionSide not in ['LONG', 'SHORT', '']:
            msg = 'positionSide must in [LONG","SHORT",""].'
            raise exception.ParamException(msg)
        if positionSide == 'LONG':  # 买入开多
            side = 'BUY'
        elif positionSide == 'SHORT':  # 卖出开空
            side = 'SELL'
        else:
            side = None

        result = self.get_orders_pending(
            symbol=symbol, pair=pair, start=start, end=end, recvWindow=recvWindow
        )
        if not result['code'] == 200:
            return result

        # 按照posSide与side筛选
        datas_open = []
        for data in result['data']:
            if positionSide:
                if data['positionSide'] == positionSide and data['side'] == side:
                    datas_open.append(data)
            else:
                if (
                        # 买入开多
                        ((data['positionSide'] == 'LONG') and (data['side'] == 'BUY')) or
                        # 卖出开空
                        ((data['positionSide'] == 'SHORT') and (data['side'] == 'SELL'))
                ):
                    datas_open.append(data)

        result['data'] = datas_open
        return result

    def get_orders_pending_close(
            self,
            symbol: str = '',
            pair: str = '',
            positionSide: str = '',
            start: Union[str, int, float, datetime.datetime] = '',
            end: Union[str, int, float, datetime.datetime] = '',
            recvWindow: int = '',
    ):

        # 验证posSide
        positionSide = positionSide.upper()
        if positionSide not in ['LONG', 'SHORT', '']:
            msg = 'positionSide must in [LONG","SHORT",""].'
            raise exception.ParamException(msg)
        # 通过posSide选择side
        if positionSide == 'LONG':  # 卖出平多
            side = 'SELL'
        elif positionSide == 'SHORT':  # 买入平空
            side = 'BUY'
        else:
            positionSide = None
            side = None

        result = self.get_orders_pending(
            symbol=symbol, pair=pair, start=start, end=end, recvWindow=recvWindow
        )
        if not result['code'] == 200:
            return result

        # 按照posSide与side筛选
        datas_open = []
        for data in result['data']:
            if positionSide:
                if data['positionSide'] == positionSide and data['side'] == side:
                    datas_open.append(data)
            else:
                if (
                        # 卖出平多
                        ((data['positionSide'] == 'LONG') and (data['side'] == 'SELL')) or
                        # 买入平空
                        ((data['positionSide'] == 'SHORT') and (data['side'] == 'BUY'))
                ):
                    datas_open.append(data)
        result['data'] = datas_open
        return result


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
        return self.cmAPI.accountTrade.cancel_order(**to_local(locals()))

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
