# 现货交易接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _SPOTTradeEndpoints():


    set_order_test = ['https://api.binance.com', 'POST', '/api/v3/order/test', True] # 测试下单 (TRADE) 
    set_order = ['https://api.binance.com', 'POST', '/api/v3/order', True] # 下单  (TRADE) 
    cancel_order = ['https://api.binance.com', 'DELETE', '/api/v3/order', True] # 撤销订单 (TRADE) 
    cancel_openOrders = ['https://api.binance.com', 'DELETE', '/api/v3/openOrders', True] # 撤销单一交易对的所有挂单 (TRADE) 
    set_order_cancelReplace = ['https://api.binance.com', 'POST', '/api/v3/order/cancelReplace', True] # 撤消挂单再下单 (TRADE) 
    get_order = ['https://api.binance.com', 'GET', '/api/v3/order', True] # 查询订单 (USER_DATA) 
    get_openOrders = ['https://api.binance.com', 'GET', '/api/v3/openOrders', True] # 当前挂单 (USER_DATA) 
    get_allOrders = ['https://api.binance.com', 'GET', '/api/v3/allOrders', True] # 查询所有订单 (USER_DATA) 
    set_order_oco = ['https://api.binance.com', 'POST', '/api/v3/order/oco', True] # OCO下单(TRADE) 
    cancel_orderList = ['https://api.binance.com', 'DELETE', '/api/v3/orderList', True] # 取消 OCO 订单(TRADE) 
    get_orderList = ['https://api.binance.com', 'GET', '/api/v3/orderList', True] # 查询 OCO (USER_DATA) 
    get_allOrderList = ['https://api.binance.com', 'GET', '/api/v3/allOrderList', True] # 查询所有 OCO (USER_DATA) 
    get_openOrderList = ['https://api.binance.com', 'GET', '/api/v3/openOrderList', True] # 查询 OCO 挂单 (USER_DATA) 
    set_sor_order = ['https://api.binance.com', 'POST', '/api/v3/sor/order', True] # 下 SOR 订单 (TRADE) 
    set_sor_order_test = ['https://api.binance.com', 'POST', '/api/v3/sor/order/test', True] # 测试 SOR 下单接口 (TRADE)  


class SPOTTrade(Client):

    # 测试下单 (TRADE)
    def set_order_test(self,symbol:str = '',side:str = '',type:str = '',timeInForce:str = '',quantity:Union[int,float] = '',quoteOrderQty:Union[int,float] = '',price:Union[int,float] = '',newClientOrderId:str = '',stopPrice:Union[int,float] = '',trailingDelta:int = '',icebergQty:Union[int,float] = '',newOrderRespType:str = '',selfTradePreventionMode:str = '',strategyId:int = '',strategyType:int = '',computeCommissionRates:bool='', recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /api/v3/order/test

        权重:

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES
        side              	ENUM    	YES     	详见枚举定义：订单方向
        type              	ENUM    	YES     	详见枚举定义：订单类型
        timeInForce       	ENUM    	NO      	详见枚举定义：有效方式
        quantity          	DECIMAL 	NO
        quoteOrderQty     	DECIMAL 	NO
        price             	DECIMAL 	NO
        newClientOrderId  	STRING  	NO      	客户自定义的唯一订单ID。 如果未发送，则自动生成。
        stopPrice         	DECIMAL 	NO      	仅STOP_LOSS,STOP_LOSS_LIMIT,TAKE_PROFIT和TAKE_PROFIT_LIMIT需要此参数。
        trailingDelta     	LONG    	NO      	用于STOP_LOSS,STOP_LOSS_LIMIT,TAKE_PROFIT和TAKE_PROFIT_LIMIT类型的订单。更多追踪止盈止损订单细节, 请参考追踪止盈止损(Trailing Stop)订单常见问题。
        icebergQty        	DECIMAL 	NO      	仅使用LIMIT,STOP_LOSS_LIMIT, 和TAKE_PROFIT_LIMIT创建新的 iceberg 订单时需要此参数。
        newOrderRespType  	ENUM    	NO      	设置响应JSON。ACK，RESULT或FULL；MARKET和LIMIT订单类型默认为FULL，所有其他订单默认为ACK。
        selfTradePreventionMode	ENUM    	NO      	允许的 ENUM 取决于交易对的配置。支持的值有EXPIRE_TAKER，EXPIRE_MAKER，EXPIRE_BOTH，NONE。
        strategyId        	INT     	NO
        strategyType      	INT     	NO      	不能低于1000000
        computeCommissionRates	BOOLEAN 	NO      	默认值:false
        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SPOTTradeEndpoints.set_order_test, **to_local(locals()))


    # 下单  (TRADE)
    def set_order(self,symbol:str = '',side:str = '',type:str = '',timeInForce:str = '',quantity:Union[int,float] = '',quoteOrderQty:Union[int,float] = '',price:Union[int,float] = '',newClientOrderId:str = '',stopPrice:Union[int,float] = '',trailingDelta:int = '',icebergQty:Union[int,float] = '',newOrderRespType:str = '',selfTradePreventionMode:str = '',strategyId:int = '',strategyType:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /api/v3/order

        权重(UID):1权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        side              	ENUM    	YES     	详见枚举定义：订单方向
        type              	ENUM    	YES     	详见枚举定义：订单类型
        timeInForce       	ENUM    	NO      	详见枚举定义：有效方式
        quantity          	DECIMAL 	NO      	
        quoteOrderQty     	DECIMAL 	NO      	
        price             	DECIMAL 	NO      	
        newClientOrderId  	STRING  	NO      	客户自定义的唯一订单ID。 如果未发送，则自动生成。
        stopPrice         	DECIMAL 	NO      	仅STOP_LOSS,STOP_LOSS_LIMIT,TAKE_PROFIT和TAKE_PROFIT_LIMIT需要此参数。
        trailingDelta     	LONG    	NO      	用于STOP_LOSS,STOP_LOSS_LIMIT,TAKE_PROFIT和TAKE_PROFIT_LIMIT类型的订单。更多追踪止盈止损订单细节, 请参考追踪止盈止损(Trailing Stop)订单常见问题。
        icebergQty        	DECIMAL 	NO      	仅使用LIMIT,STOP_LOSS_LIMIT, 和TAKE_PROFIT_LIMIT创建新的 iceberg 订单时需要此参数。
        newOrderRespType  	ENUM    	NO      	设置响应JSON。ACK，RESULT或FULL；MARKET和LIMIT订单类型默认为FULL，所有其他订单默认为ACK。
        selfTradePreventionMode	ENUM    	NO      	允许的 ENUM 取决于交易对的配置。支持的值有EXPIRE_TAKER，EXPIRE_MAKER，EXPIRE_BOTH，NONE。
        strategyId        	INT     	NO      	
        strategyType      	INT     	NO      	不能低于1000000
        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SPOTTradeEndpoints.set_order, **to_local(locals()))


    # 撤销订单 (TRADE)
    def cancel_order(self,symbol:str = '',orderId:int = '',origClientOrderId:str = '',newClientOrderId:str = '',cancelRestrictions:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /api/v3/order

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        orderId           	LONG    	NO      	
        origClientOrderId 	STRING  	NO      	
        newClientOrderId  	STRING  	NO      	用户自定义的本次撤销操作的ID(注意不是被撤销的订单的自定义ID)。如无指定会自动赋值。
        cancelRestrictions	ENUM    	NO      	支持的值:ONLY_NEW- 如果订单状态为NEW，订单取消将成功。ONLY_PARTIALLY_FILLED- 如果订单状态为PARTIALLY_FILLED，订单取消将成功。
        recvWindow        	LONG    	NO      	赋值不得大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SPOTTradeEndpoints.cancel_order, **to_local(locals()))


    # 撤销单一交易对的所有挂单 (TRADE)
    def cancel_openOrders(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /api/v3/openOrders

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        recvWindow        	LONG    	NO      	不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SPOTTradeEndpoints.cancel_openOrders, **to_local(locals()))


    # 撤消挂单再下单 (TRADE)
    def set_order_cancelReplace(self,symbol:str = '',side:str = '',type:str = '',cancelReplaceMode:str = '',timeInForce:str = '',quantity:Union[int,float] = '',quoteOrderQty:Union[int,float] = '',price:Union[int,float] = '',cancelNewClientOrderId:str = '',cancelOrigClientOrderId:str = '',cancelOrderId:int = '',newClientOrderId:str = '',strategyId:int = '',strategyType:int = '',stopPrice:Union[int,float] = '',trailingDelta:int = '',icebergQty:Union[int,float] = '',newOrderRespType:str = '',selfTradePreventionMode:str = '',cancelRestrictions:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /api/v3/order/cancelReplace

        

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        side              	ENUM    	YES     	
        type              	ENUM    	YES     	
        cancelReplaceMode 	ENUM    	YES     	指定类型：STOP_ON_FAILURE- 如果撤消订单失败将不会继续重新下单。ALLOW_FAILURE- 不管撤消订单是否成功都会继续重新下单。
        timeInForce       	ENUM    	NO      	
        quantity          	DECIMAL 	NO      	
        quoteOrderQty     	DECIMAL 	NO      	
        price             	DECIMAL 	NO      	
        cancelNewClientOrderId	STRING  	NO      	用户自定义的id，如空缺系统会自动赋值
        cancelOrigClientOrderId	STRING  	NO      	必须提供cancelOrigClientOrderId或者cancelOrderId。 如果两个参数都提供,cancelOrderId会占优先。
        cancelOrderId     	LONG    	NO      	必须提供cancelOrigClientOrderId或者cancelOrderId。 如果两个参数都提供,cancelOrderId会占优先。
        newClientOrderId  	STRING  	NO      	用于辨识新订单。
        strategyId        	INT     	NO      	
        strategyType      	INT     	NO      	不能低于1000000
        stopPrice         	DECIMAL 	NO      	
        trailingDelta     	LONG    	NO      	
        icebergQty        	DECIMAL 	NO      	
        newOrderRespType  	ENUM    	NO      	指定响应类型:指定响应类型ACK,RESULT, orFULL;MARKET与LIMIT订单默认为FULL, 其他默认为ACK.
        selfTradePreventionMode	ENUM    	NO      	允许的 ENUM 取决于交易对的配置。支持的值有EXPIRE_TAKER，EXPIRE_MAKER，EXPIRE_BOTH，NONE。
        cancelRestrictions	ENUM    	NO      	支持的值:ONLY_NEW- 如果订单状态为NEW，撤销将成功。ONLY_PARTIALLY_FILLED- 如果订单状态为PARTIALLY_FILLED，撤销将成功。
        recvWindow        	LONG    	NO      	不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SPOTTradeEndpoints.set_order_cancelReplace, **to_local(locals()))


    # 查询订单 (USER_DATA)
    def get_order(self,symbol:str = '',orderId:int = '',origClientOrderId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /api/v3/order

        权重(IP):4

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        orderId           	LONG    	NO      	
        origClientOrderId 	STRING  	NO      	
        recvWindow        	LONG    	NO      	赋值不得大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SPOTTradeEndpoints.get_order, **to_local(locals()))


    # 当前挂单 (USER_DATA)
    def get_openOrders(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /api/v3/openOrders

        权重(IP):6 单一交易对;80交易对参数缺失;

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        recvWindow        	LONG    	NO      	赋值不得大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SPOTTradeEndpoints.get_openOrders, **to_local(locals()))


    # 查询所有订单 (USER_DATA)
    def get_allOrders(self,symbol:str = '',orderId:int = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /api/v3/allOrders

        权重(IP):20

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        orderId           	LONG    	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	默认 500; 最大 1000.
        recvWindow        	LONG    	NO      	赋值不得大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SPOTTradeEndpoints.get_allOrders, **to_local(locals()))


    # OCO下单(TRADE)
    def set_order_oco(self,symbol:str = '',listClientOrderId:str = '',side:str = '',quantity:Union[int,float] = '',limitClientOrderId:str = '',limitStrategyId:int = '',limitStrategyType:int = '',price:Union[int,float] = '',limitIcebergQty:Union[int,float] = '',trailingDelta:int = '',stopClientOrderId:str = '',stopPrice:Union[int,float] = '',stopStrategyId:int = '',stopStrategyType:int = '',stopLimitPrice:Union[int,float] = '',stopIcebergQty:Union[int,float] = '',stopLimitTimeInForce:str = '',newOrderRespType:str = '',selfTradePreventionMode:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /api/v3/order/oco

        权重(UID): 2权重(IP): 1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        listClientOrderId 	STRING  	NO      	整个orderList的唯一ID
        side              	ENUM    	YES     	详见枚举定义：订单方向
        quantity          	DECIMAL 	YES     	
        limitClientOrderId	STRING  	NO      	限价单的唯一ID
        limitStrategyId   	INT     	NO      	
        limitStrategyType 	INT     	NO      	不能低于1000000
        price             	DECIMAL 	YES     	
        limitIcebergQty   	DECIMAL 	NO      	
        trailingDelta     	LONG    	NO      	
        stopClientOrderId 	STRING  	NO      	止损/止损限价单的唯一ID
        stopPrice         	DECIMAL 	YES     	
        stopStrategyId    	INT     	NO      	
        stopStrategyType  	INT     	NO      	不能低于1000000
        stopLimitPrice    	DECIMAL 	NO      	如果提供，须配合提交stopLimitTimeInForce
        stopIcebergQty    	DECIMAL 	NO      	
        stopLimitTimeInForce	ENUM    	NO      	有效值GTC/FOK/IOC
        newOrderRespType  	ENUM    	NO      	详见枚举定义：订单返回类型
        selfTradePreventionMode	ENUM    	NO      	允许的 ENUM 取决于交易对的配置。支持的值有EXPIRE_TAKER，EXPIRE_MAKER，EXPIRE_BOTH，NONE。｜
        recvWindow        	LONG    	NO      	不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SPOTTradeEndpoints.set_order_oco, **to_local(locals()))


    # 取消 OCO 订单(TRADE)
    def cancel_orderList(self,symbol:str = '',orderListId:int = '',listClientOrderId:str = '',newClientOrderId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /api/v3/orderList

        权重(IP): 1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        orderListId       	LONG    	NO      	orderListId或listClientOrderId必须被提供
        listClientOrderId 	STRING  	NO      	orderListId或listClientOrderId必须被提供
        newClientOrderId  	STRING  	NO      	用户自定义的本次撤销操作的ID(注意不是被撤销的订单的自定义ID)。如无指定会自动赋值。
        recvWindow        	LONG    	NO      	不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SPOTTradeEndpoints.cancel_orderList, **to_local(locals()))


    # 查询 OCO (USER_DATA)
    def get_orderList(self,orderListId:int = '',origClientOrderId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /api/v3/orderList

        权重(IP): 4

        请求参数:
        Parameter         	Type    	Required	Description

        orderListId       	LONG    	NO      	orderListId或origClientOrderId必须提供一个。
        origClientOrderId 	STRING  	NO      	orderListId或origClientOrderId必须提供一个。
        recvWindow        	LONG    	NO      	赋值不得大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SPOTTradeEndpoints.get_orderList, **to_local(locals()))


    # 查询所有 OCO (USER_DATA)
    def get_allOrderList(self,fromId:int = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /api/v3/allOrderList

        权重(IP): 20

        请求参数:
        Parameter         	Type    	Required	Description

        fromId            	LONG    	NO      	提供该项后,startTime和endTime都不可提供
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	默认值: 500; 最大值: 1000
        recvWindow        	LONG    	NO      	赋值不能超过60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SPOTTradeEndpoints.get_allOrderList, **to_local(locals()))


    # 查询 OCO 挂单 (USER_DATA)
    def get_openOrderList(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /api/v3/openOrderList

        权重(IP): 6

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SPOTTradeEndpoints.get_openOrderList, **to_local(locals()))


    # 下 SOR 订单 (TRADE)
    def set_sor_order(self,symbol:str = '',side:str = '',type:str = '',timeInForce:str = '',quantity:Union[int,float] = '',price:Union[int,float] = '',newClientOrderId:str = '',strategyId:int = '',strategyType:int = '',icebergQty:Union[int,float] = '',newOrderRespType:str = '',selfTradePreventionMode:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /api/v3/sor/order

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        side              	ENUM    	YES     	
        type              	ENUM    	YES     	
        timeInForce       	ENUM    	NO      	
        quantity          	DECIMAL 	YES     	
        price             	DECIMAL 	NO      	
        newClientOrderId  	STRING  	NO      	用户自定义的orderid，如空缺系统会自动赋值。如果几个订单具有相同的newClientOrderID赋值，那么只有在前一个订单成交后才可以接受下一个订单，否则该订单将被拒绝。
        strategyId        	INT     	NO      	
        strategyType      	INT     	NO      	赋值不能小于1000000.
        icebergQty        	DECIMAL 	NO      	仅有限价单可以使用该参数，含义为创建冰山订单并指定冰山订单的数量。
        newOrderRespType  	ENUM    	NO      	指定响应类型:指定响应类型ACK,RESULT或FULL; 默认为FULL。
        selfTradePreventionMode	ENUM    	NO      	允许的 ENUM 取决于交易对的配置。支持的值有EXPIRE_TAKER，EXPIRE_MAKER，EXPIRE_BOTH，NONE。
        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SPOTTradeEndpoints.set_sor_order, **to_local(locals()))


    # 测试 SOR 下单接口 (TRADE)
    def set_sor_order_test(self,computeCommissionRates:bool = '',proxies={},proxy_host:str=None):
        '''
        POST /api/v3/sor/order/test

        权重:

        请求参数:
        Parameter         	Type    	Required	Description

        computeCommissionRates	BOOLEAN 	NO      	默认值:false
        '''
        return self.send_request(*_SPOTTradeEndpoints.set_sor_order_test, **to_local(locals()))