# 下单接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _PMSetOrderEndpoints():


    set_um_order = ['https://papi.binance.com', 'POST', '/papi/v1/um/order', True] # UM下单 (TRADE) 
    set_cm_order = ['https://papi.binance.com', 'POST', '/papi/v1/cm/order', True] # CM下单 (TRADE) 
    set_margin_order = ['https://papi.binance.com', 'POST', '/papi/v1/margin/order', True] # 杠杆账户下单(TRADE) 
    set_marginLoan = ['https://papi.binance.com', 'POST', '/papi/v1/marginLoan', True] # 杠杆账户借贷 (MARGIN) 
    set_repayLoan = ['https://papi.binance.com', 'POST', '/papi/v1/repayLoan', True] # 杠杆账户归还借贷 (MARGIN) 
    set_margin_order_oco = ['https://papi.binance.com', 'POST', '/papi/v1/margin/order/oco', True] # 杠杆账户 OCO 下单 (TRADE) 
    set_um_conditional_order = ['https://papi.binance.com', 'POST', '/papi/v1/um/conditional/order', True] # UM条件单下单 (TRADE) 
    set_cm_conditional_order = ['https://papi.binance.com', 'POST', '/papi/v1/cm/conditional/order', True] # CM条件单下单 (TRADE)  


class PMSetOrder(Client):

    # UM下单 (TRADE)
    def set_um_order(self,symbol:str = '',side:str = '',positionSide:str = '',type:str = '',timeInForce:str = '',quantity:Union[int,float] = '',reduceOnly:str = '',price:Union[int,float] = '',newClientOrderId:str = '',newOrderRespType:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /papi/v1/um/order

        权重(order): 1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        side              	ENUM    	YES     	方向
        positionSide      	ENUM    	NO      	持仓方向，单向持仓模式下非必填，默认且仅可填BOTH;在双向持仓模式下必填,且仅可选择LONG或SHORT
        type              	ENUM    	YES     	LIMIT,MARKET
        timeInForce       	ENUM    	NO      	有效方法
        quantity          	DECIMAL 	NO      	下单数量
        reduceOnly        	STRING  	NO      	true或false; 非双开模式下默认false；双开模式下不接受此参数
        price             	DECIMAL 	NO      	委托价格
        newClientOrderId  	STRING  	NO      	用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则:^[\.A-Z\:/a-z0-9_-]{1,32}$
        newOrderRespType  	ENUM    	NO      	ACK，RESULT，默认ACK
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMSetOrderEndpoints.set_um_order, **to_local(locals()))


    # CM下单 (TRADE)
    def set_cm_order(self,symbol:str = '',side:str = '',positionSide:str = '',type:str = '',timeInForce:str = '',quantity:Union[int,float] = '',reduceOnly:str = '',price:Union[int,float] = '',newClientOrderId:str = '',newOrderRespType:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /papi/v1/cm/order

        权重(order): 1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        side              	ENUM    	YES     	方向
        positionSide      	ENUM    	NO      	持仓方向，单向持仓模式下非必填，默认且仅可填BOTH;在双向持仓模式下必填,且仅可选择LONG或SHORT
        type              	ENUM    	YES     	LIMIT,MARKET
        timeInForce       	ENUM    	NO      	有效方法
        quantity          	DECIMAL 	NO      	下单数量
        reduceOnly        	STRING  	NO      	true或false; 非双开模式下默认false；双开模式下不接受此参数
        price             	DECIMAL 	NO      	委托价格
        newClientOrderId  	STRING  	NO      	用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则:^[\.A-Z\:/a-z0-9_-]{1,32}$
        newOrderRespType  	ENUM    	NO      	ACK，RESULT，默认ACK
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMSetOrderEndpoints.set_cm_order, **to_local(locals()))


    # 杠杆账户下单(TRADE)
    def set_margin_order(self,symbol:str = '',side:str = '',type:str = '',quantity:Union[int,float] = '',quoteOrderQty:Union[int,float] = '',price:Union[int,float] = '',stopPrice:Union[int,float] = '',newClientOrderId:str = '',newOrderRespType:str = '',icebergQty:Union[int,float] = '',sideEffectType:str = '',timeInForce:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /papi/v1/margin/order

        权重(order):1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        side              	ENUM    	YES     	BUY;SELL
        type              	ENUM    	YES     	详见枚举定义：订单类型
        quantity          	DECIMAL 	NO      	
        quoteOrderQty     	DECIMAL 	NO      	
        price             	DECIMAL 	NO      	
        stopPrice         	DECIMAL 	NO      	与STOP_LOSS,STOP_LOSS_LIMIT,TAKE_PROFIT，和TAKE_PROFIT_LIMIT订单一起使用
        newClientOrderId  	STRING  	NO      	客户自定义的唯一订单ID。若未发送自动生成。
        newOrderRespType  	ENUM    	NO      	设置响应: JSON。ACK，RESULT， 或FULL;MARKET和LIMIT订单类型默认为FULL， 所有其他订单默认为ACK
        icebergQty        	DECIMAL 	NO      	与LIMIT，STOP_LOSS_LIMIT，和TAKE_PROFIT_LIMIT一起使用创建 iceberg 订单
        sideEffectType    	ENUM    	NO      	NO_SIDE_EFFECT，MARGIN_BUY，AUTO_REPAY；默认为NO_SIDE_EFFECT
        timeInForce       	ENUM    	NO      	GTC，IOC，FOK
        recvWindow        	LONG    	NO      	赋值不能超过60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMSetOrderEndpoints.set_margin_order, **to_local(locals()))


    # 杠杆账户借贷 (MARGIN)
    def set_marginLoan(self,asset:str = '',amount:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /papi/v1/marginLoan

        权重:100

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	YES     	
        amount            	DECIMAL 	YES     	
        recvWindow        	LONG    	NO      	赋值不能超过60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMSetOrderEndpoints.set_marginLoan, **to_local(locals()))


    # 杠杆账户归还借贷 (MARGIN)
    def set_repayLoan(self,asset:str = '',amount:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /papi/v1/repayLoan

        权重:100

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	YES     	
        amount            	DECIMAL 	YES     	
        recvWindow        	LONG    	NO      	赋值不能超过60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMSetOrderEndpoints.set_repayLoan, **to_local(locals()))


    # 杠杆账户 OCO 下单 (TRADE)
    def set_margin_order_oco(self,symbol:str = '',listClientOrderId:str = '',side:str = '',quantity:Union[int,float] = '',limitClientOrderId:str = '',price:Union[int,float] = '',limitIcebergQty:Union[int,float] = '',stopClientOrderId:str = '',stopPrice:Union[int,float] = '',stopLimitPrice:Union[int,float] = '',stopIcebergQty:Union[int,float] = '',stopLimitTimeInForce:str = '',newOrderRespType:str = '',sideEffectType:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /papi/v1/margin/order/oco

        权重(order):1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        listClientOrderId 	STRING  	NO      	整个orderList的唯一ID
        side              	ENUM    	YES     	详见枚举定义：订单方向
        quantity          	DECIMAL 	YES     	
        limitClientOrderId	STRING  	NO      	限价单的唯一ID
        price             	DECIMAL 	YES     	
        limitIcebergQty   	DECIMAL 	NO      	
        stopClientOrderId 	STRING  	NO      	止损/止损限价单的唯一ID
        stopPrice         	DECIMAL 	YES     	
        stopLimitPrice    	DECIMAL 	NO      	如果提供，须配合提交stopLimitTimeInForce
        stopIcebergQty    	DECIMAL 	NO      	
        stopLimitTimeInForce	ENUM    	NO      	有效值GTC/FOK/IOC
        newOrderRespType  	ENUM    	NO      	详见枚举定义：订单返回类型
        sideEffectType    	ENUM    	NO      	NO_SIDE_EFFECT, MARGIN_BUY, AUTO_REPAY; 默认为 NO_SIDE_EFFECT
        recvWindow        	LONG    	NO      	不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMSetOrderEndpoints.set_margin_order_oco, **to_local(locals()))


    # UM条件单下单 (TRADE)
    def set_um_conditional_order(self,symbol:str = '',side:str = '',positionSide:str = '',strategyType:str = '',timeInForce:str = '',quantity:Union[int,float] = '',reduceOnly:str = '',price:Union[int,float] = '',workingType:str = '',priceProtect:str = '',newClientStrategyId:str = '',stopPrice:Union[int,float] = '',activationPrice:Union[int,float] = '',callbackRate:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /papi/v1/um/conditional/order

        权重(Order):1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        side              	ENUM    	YES     	方向
        positionSide      	ENUM    	NO      	持仓方向，单向持仓模式下非必填，默认且仅可填BOTH;在双向持仓模式下必填,且仅可选择LONG或SHORT
        strategyType      	ENUM    	YES     	条件单类型"STOP", "STOP_MARKET", "TAKE_PROFIT", "TAKE_PROFIT_MARKET"或"TRAILING_STOP_MARKET"
        timeInForce       	ENUM    	NO      	
        quantity          	DECIMAL 	NO      	
        reduceOnly        	STRING  	NO      	true或false; 非双开模式下默认false；双开模式下不接受此参数
        price             	DECIMAL 	NO      	
        workingType       	ENUM    	NO      	stopPrice 触发类型:MARK_PRICE(标记价格),CONTRACT_PRICE(合约最新价). 默认CONTRACT_PRICE
        priceProtect      	STRING  	NO      	条件单触发保护："TRUE","FALSE", 默认"FALSE". 仅STOP,STOP_MARKET,TAKE_PROFIT,TAKE_PROFIT_MARKET需要此参数
        newClientStrategyId	STRING  	NO      	用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则:^[\.A-Z\:/a-z0-9_-]{1,32}$
        stopPrice         	DECIMAL 	NO      	Used withSTOP/STOP_MARKETorTAKE_PROFIT/TAKE_PROFIT_MARKETorders.
        activationPrice   	DECIMAL 	NO      	TRAILING_STOP_MARKET单使用，默认标记价格
        callbackRate      	DECIMAL 	NO      	TRAILING_STOP_MARKET单使用, 最小0.1, 最大5，1代表1%
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMSetOrderEndpoints.set_um_conditional_order, **to_local(locals()))


    # CM条件单下单 (TRADE)
    def set_cm_conditional_order(self,symbol:str = '',side:str = '',positionSide:str = '',strategyType:str = '',timeInForce:str = '',quantity:Union[int,float] = '',reduceOnly:str = '',price:Union[int,float] = '',workingType:str = '',priceProtect:str = '',newClientStrategyId:str = '',stopPrice:Union[int,float] = '',activationPrice:Union[int,float] = '',callbackRate:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /papi/v1/cm/conditional/order

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        side              	ENUM    	YES     	方向
        positionSide      	ENUM    	NO      	持仓方向，单向持仓模式下非必填，默认且仅可填BOTH;在双向持仓模式下必填,且仅可选择LONG或SHORT
        strategyType      	ENUM    	YES     	条件单类型"STOP", "STOP_MARKET", "TAKE_PROFIT", "TAKE_PROFIT_MARKET"或"TRAILING_STOP_MARKET"
        timeInForce       	ENUM    	NO      	
        quantity          	DECIMAL 	NO      	
        reduceOnly        	STRING  	NO      	true或false; 非双开模式下默认false；双开模式下不接受此参数
        price             	DECIMAL 	NO      	
        workingType       	ENUM    	NO      	stopPrice 触发类型:MARK_PRICE,CONTRACT_PRICE. 默认CONTRACT_PRICE
        priceProtect      	STRING  	NO      	条件单触发保护："TRUE" or "FALSE", 默认 "FALSE".STOP/STOP_MARKETorTAKE_PROFIT/TAKE_PROFIT_MARKET需要此参数
        newClientStrategyId	STRING  	NO      	用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则:^[\.A-Z\:/a-z0-9_-]{1,32}$
        stopPrice         	DECIMAL 	NO      	Used withSTOP/STOP_MARKETorTAKE_PROFIT/TAKE_PROFIT_MARKETorders.
        activationPrice   	DECIMAL 	NO      	TRAILING_STOP_MARKET单使用，默认标记价格
        callbackRate      	DECIMAL 	NO      	TRAILING_STOP_MARKET单使用, 最小0.1, 最大5，1代表1%
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMSetOrderEndpoints.set_cm_conditional_order, **to_local(locals()))