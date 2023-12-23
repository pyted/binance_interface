# 撤单接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _PMCancelOrderEndpoints():


    cancel_um_order = ['https://papi.binance.com', 'DELETE', '/papi/v1/um/order', True] # 撤销UM订单 (TRADE) 
    cancel_um_allOpenOrders = ['https://papi.binance.com', 'DELETE', '/papi/v1/um/allOpenOrders', True] # 撤销全部UM订单 (TRADE) 
    cancel_cm_order = ['https://papi.binance.com', 'DELETE', '/papi/v1/cm/order', True] # 撤销CM订单  (TRADE) 
    cancel_cm_allOpenOrders = ['https://papi.binance.com', 'DELETE', '/papi/v1/cm/allOpenOrders', True] # 撤销全部CM订单 (TRADE) 
    cancel_margin_order = ['https://papi.binance.com', 'DELETE', '/papi/v1/margin/order', True] # 杠杆账户撤销订单 (TRADE) 
    cancel_margin_allOpenOrders = ['https://papi.binance.com', 'DELETE', '/papi/v1/margin/allOpenOrders', True] # 杠杆账户撤销单一交易对的所有挂单 (TRADE) 
    cancel_margin_orderList = ['https://papi.binance.com', 'DELETE', '/papi/v1/margin/orderList', True] # 取消杠杆账户OCO订单 (TRADE) 
    cancel_um_conditional_order = ['https://papi.binance.com', 'DELETE', '/papi/v1/um/conditional/order', True] # 取消UM条件订单 (TRADE) 
    cancel_um_conditional_allOpenOrders = ['https://papi.binance.com', 'DELETE', '/papi/v1/um/conditional/allOpenOrders', True] # 取消全部UM条件单 (TRADE) 
    cancel_cm_conditional_order = ['https://papi.binance.com', 'DELETE', '/papi/v1/cm/conditional/order', True] # 取消CM条件订单 (TRADE) 
    cancel_cm_conditional_allOpenOrders = ['https://papi.binance.com', 'DELETE', '/papi/v1/cm/conditional/allOpenOrders', True] # 取消全部CM条件单 (TRADE)  


class PMCancelOrder(Client):

    # 撤销UM订单 (TRADE)
    def cancel_um_order(self,symbol:str = '',orderId:int = '',origClientOrderId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /papi/v1/um/order

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        orderId           	LONG    	NO      	
        origClientOrderId 	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMCancelOrderEndpoints.cancel_um_order, **to_local(locals()))


    # 撤销全部UM订单 (TRADE)
    def cancel_um_allOpenOrders(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /papi/v1/um/allOpenOrders

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMCancelOrderEndpoints.cancel_um_allOpenOrders, **to_local(locals()))


    # 撤销CM订单  (TRADE)
    def cancel_cm_order(self,symbol:str = '',orderId:int = '',origClientOrderId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /papi/v1/cm/order

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        orderId           	LONG    	NO      	
        origClientOrderId 	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMCancelOrderEndpoints.cancel_cm_order, **to_local(locals()))


    # 撤销全部CM订单 (TRADE)
    def cancel_cm_allOpenOrders(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /papi/v1/cm/allOpenOrders

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMCancelOrderEndpoints.cancel_cm_allOpenOrders, **to_local(locals()))


    # 杠杆账户撤销订单 (TRADE)
    def cancel_margin_order(self,symbol:str = '',orderId:int = '',origClientOrderId:str = '',newClientOrderId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /papi/v1/margin/order

        权重:2

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        orderId           	LONG    	NO      	
        origClientOrderId 	STRING  	NO      	
        newClientOrderId  	STRING  	NO      	用于唯一识别此撤销订单，默认自动生成。
        recvWindow        	LONG    	NO      	赋值不能超过60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMCancelOrderEndpoints.cancel_margin_order, **to_local(locals()))


    # 杠杆账户撤销单一交易对的所有挂单 (TRADE)
    def cancel_margin_allOpenOrders(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /papi/v1/margin/allOpenOrders

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        recvWindow        	LONG    	NO      	赋值不能超过 60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMCancelOrderEndpoints.cancel_margin_allOpenOrders, **to_local(locals()))


    # 取消杠杆账户OCO订单 (TRADE)
    def cancel_margin_orderList(self,symbol:str = '',orderListId:int = '',listClientOrderId:str = '',newClientOrderId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /papi/v1/margin/orderList

        权重:2

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        orderListId       	LONG    	NO      	orderListId或listClientOrderId必须被提供
        listClientOrderId 	STRING  	NO      	orderListId或listClientOrderId必须被提供
        newClientOrderId  	STRING  	NO      	用户自定义的本次撤销操作的ID(注意不是被撤销的订单的自定义ID)。如无指定会自动赋值
        recvWindow        	LONG    	NO      	赋值不能超过 60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMCancelOrderEndpoints.cancel_margin_orderList, **to_local(locals()))


    # 取消UM条件订单 (TRADE)
    def cancel_um_conditional_order(self,symbol:str = '',strategyId:int = '',newClientStrategyId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /papi/v1/um/conditional/order

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        strategyId        	LONG    	NO      	
        newClientStrategyId	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMCancelOrderEndpoints.cancel_um_conditional_order, **to_local(locals()))


    # 取消全部UM条件单 (TRADE)
    def cancel_um_conditional_allOpenOrders(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /papi/v1/um/conditional/allOpenOrders

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMCancelOrderEndpoints.cancel_um_conditional_allOpenOrders, **to_local(locals()))


    # 取消CM条件订单 (TRADE)
    def cancel_cm_conditional_order(self,symbol:str = '',strategyId:int = '',newClientStrategyId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /papi/v1/cm/conditional/order

        权重(Order):1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        strategyId        	LONG    	NO      	
        newClientStrategyId	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMCancelOrderEndpoints.cancel_cm_conditional_order, **to_local(locals()))


    # 取消全部CM条件单 (TRADE)
    def cancel_cm_conditional_allOpenOrders(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /papi/v1/cm/conditional/allOpenOrders

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMCancelOrderEndpoints.cancel_cm_conditional_allOpenOrders, **to_local(locals()))