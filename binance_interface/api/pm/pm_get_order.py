# 查询订单
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _PMGetOrderEndpoints():


    get_um_order = ['https://papi.binance.com', 'GET', '/papi/v1/um/order', True] # 查询UM订单 (USER_DATA) 
    get_um_openOrder = ['https://papi.binance.com', 'GET', '/papi/v1/um/openOrder', True] # 查询当前UM挂单 (USER_DATA) 
    get_um_openOrders = ['https://papi.binance.com', 'GET', '/papi/v1/um/openOrders', True] # 查看当前全部UM挂单 (USER_DATA) 
    get_um_allOrders = ['https://papi.binance.com', 'GET', '/papi/v1/um/allOrders', True] # 查询所有UM订单(包括历史订单) (USER_DATA) 
    get_cm_order = ['https://papi.binance.com', 'GET', '/papi/v1/cm/order', True] # 查询CM订单  (USER_DATA) 
    get_cm_openOrder = ['https://papi.binance.com', 'GET', '/papi/v1/cm/openOrder', True] # 查看当前全部CM挂单 (USER_DATA) 
    get_cm_openOrders = ['https://papi.binance.com', 'GET', '/papi/v1/cm/openOrders', True] # 查看当前全部CM挂单 (USER_DATA) 
    get_cm_allOrders = ['https://papi.binance.com', 'GET', '/papi/v1/cm/allOrders', True] # 查询所有CM订单(包括历史订单) (USER_DATA) 
    get_um_conditional_openOrder = ['https://papi.binance.com', 'GET', '/papi/v1/um/conditional/openOrder', True] # 查询UM当前条件挂单 (USER_DATA) 
    get_um_conditional_openOrders = ['https://papi.binance.com', 'GET', '/papi/v1/um/conditional/openOrders', True] # 查看UM当前全部条件挂单 (USER_DATA) 
    get_um_conditional_orderHistory = ['https://papi.binance.com', 'GET', '/papi/v1/um/conditional/orderHistory', True] # 查询UM条件单历史 (USER_DATA) 
    get_um_conditional_allOrders = ['https://papi.binance.com', 'GET', '/papi/v1/um/conditional/allOrders', True] # 查询UM所有条件订单（包括历史订单） (USER_DATA) 
    get_cm_conditional_openOrder = ['https://papi.binance.com', 'GET', '/papi/v1/cm/conditional/openOrder', True] # 查询CM当前条件挂单  (USER_DATA) 
    get_cm_conditional_openOrders = ['https://papi.binance.com', 'GET', '/papi/v1/cm/conditional/openOrders', True] # 查看CM当前全部条件挂单 (USER_DATA) 
    get_cm_conditional_orderHistory = ['https://papi.binance.com', 'GET', '/papi/v1/cm/conditional/orderHistory', True] # 查询CM条件单历史 (USER_DATA) 
    get_cm_conditional_allOrders = ['https://papi.binance.com', 'GET', '/papi/v1/cm/conditional/allOrders', True] # 查询CM所有条件订单（包括历史订单）(USER_DATA) 
    get_margin_order = ['https://papi.binance.com', 'GET', '/papi/v1/margin/order', True] # 查询杠杆账户订单 (USER_DATA) 
    get_margin_openOrders = ['https://papi.binance.com', 'GET', '/papi/v1/margin/openOrders', True] # 查询杠杆账户挂单记录 (USER_DATA) 
    get_margin_allOrders = ['https://papi.binance.com', 'GET', '/papi/v1/margin/allOrders', True] # 查询杠杆账户的所有订单 (USER_DATA) 
    get_margin_orderList = ['https://papi.binance.com', 'GET', '/papi/v1/margin/orderList', True] # 查询杠杆账户 OCO (USER_DATA) 
    get_margin_allOrderList = ['https://papi.binance.com', 'GET', '/papi/v1/margin/allOrderList', True] # 查询特定杠杆账户所有 OCO(USER_DATA) 
    get_margin_openOrderList = ['https://papi.binance.com', 'GET', '/papi/v1/margin/openOrderList', True] # 查询杠杆账户 OCO 挂单 (USER_DATA) 
    get_margin_myTrades = ['https://papi.binance.com', 'GET', '/papi/v1/margin/myTrades', True] # 查询杠杆账户交易历史 (USER_DATA)  


class PMGetOrder(Client):

    # 查询UM订单 (USER_DATA)
    def get_um_order(self,symbol:str = '',orderId:int = '',origClientOrderId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/um/order

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        orderId           	LONG    	NO      	
        origClientOrderId 	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMGetOrderEndpoints.get_um_order, **to_local(locals()))


    # 查询当前UM挂单 (USER_DATA)
    def get_um_openOrder(self,symbol:str = '',orderId:int = '',origClientOrderId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/um/openOrder

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        orderId           	LONG    	NO      	
        origClientOrderId 	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMGetOrderEndpoints.get_um_openOrder, **to_local(locals()))


    # 查看当前全部UM挂单 (USER_DATA)
    def get_um_openOrders(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/um/openOrders

        权重:带symbol1- 不带40

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMGetOrderEndpoints.get_um_openOrders, **to_local(locals()))


    # 查询所有UM订单(包括历史订单) (USER_DATA)
    def get_um_allOrders(self,symbol:str = '',orderId:int = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/um/allOrders

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        orderId           	LONG    	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	Default 500; max 1000.
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMGetOrderEndpoints.get_um_allOrders, **to_local(locals()))


    # 查询CM订单  (USER_DATA)
    def get_cm_order(self,symbol:str = '',orderId:int = '',origClientOrderId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/cm/order

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        orderId           	LONG    	NO      	
        origClientOrderId 	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMGetOrderEndpoints.get_cm_order, **to_local(locals()))


    # 查看当前全部CM挂单 (USER_DATA)
    def get_cm_openOrder(self,symbol:str = '',orderId:int = '',origClientOrderId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/cm/openOrder

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        orderId           	LONG    	NO      	
        origClientOrderId 	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMGetOrderEndpoints.get_cm_openOrder, **to_local(locals()))


    # 查看当前全部CM挂单 (USER_DATA)
    def get_cm_openOrders(self,symbol:str = '',pair:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/cm/openOrders

        权重:

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        pair              	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMGetOrderEndpoints.get_cm_openOrders, **to_local(locals()))


    # 查询所有CM订单(包括历史订单) (USER_DATA)
    def get_cm_allOrders(self,symbol:str = '',pair:str = '',orderId:int = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/cm/allOrders

        权重:

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        pair              	STRING  	NO      	
        orderId           	LONG    	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	返回的结果集数量 默认值:50 最大值:100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMGetOrderEndpoints.get_cm_allOrders, **to_local(locals()))


    # 查询UM当前条件挂单 (USER_DATA)
    def get_um_conditional_openOrder(self,symbol:str = '',strategyId:int = '',newClientStrategyId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/um/conditional/openOrder

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        strategyId        	LONG    	NO      	
        newClientStrategyId	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMGetOrderEndpoints.get_um_conditional_openOrder, **to_local(locals()))


    # 查看UM当前全部条件挂单 (USER_DATA)
    def get_um_conditional_openOrders(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/um/conditional/openOrders

        权重:带symbol1;  不带40

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMGetOrderEndpoints.get_um_conditional_openOrders, **to_local(locals()))


    # 查询UM条件单历史 (USER_DATA)
    def get_um_conditional_orderHistory(self,symbol:str = '',strategyId:int = '',newClientStrategyId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/um/conditional/orderHistory

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        strategyId        	LONG    	NO      	
        newClientStrategyId	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMGetOrderEndpoints.get_um_conditional_orderHistory, **to_local(locals()))


    # 查询UM所有条件订单（包括历史订单） (USER_DATA)
    def get_um_conditional_allOrders(self,symbol:str = '',strategyId:int = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/um/conditional/allOrders

        权重:带symbol1;  不带40

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        strategyId        	LONG    	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	Default 500; max 1000.
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMGetOrderEndpoints.get_um_conditional_allOrders, **to_local(locals()))


    # 查询CM当前条件挂单  (USER_DATA)
    def get_cm_conditional_openOrder(self,symbol:str = '',strategyId:int = '',newClientStrategyId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/cm/conditional/openOrder

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        strategyId        	LONG    	NO      	
        newClientStrategyId	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMGetOrderEndpoints.get_cm_conditional_openOrder, **to_local(locals()))


    # 查看CM当前全部条件挂单 (USER_DATA)
    def get_cm_conditional_openOrders(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/cm/conditional/openOrders

        权重:带symbol1;  不带40

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMGetOrderEndpoints.get_cm_conditional_openOrders, **to_local(locals()))


    # 查询CM条件单历史 (USER_DATA)
    def get_cm_conditional_orderHistory(self,symbol:str = '',strategyId:int = '',newClientStrategyId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/cm/conditional/orderHistory

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        strategyId        	LONG    	NO      	
        newClientStrategyId	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMGetOrderEndpoints.get_cm_conditional_orderHistory, **to_local(locals()))


    # 查询CM所有条件订单（包括历史订单）(USER_DATA)
    def get_cm_conditional_allOrders(self,symbol:str = '',strategyId:int = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/cm/conditional/allOrders

        权重:带symbol1;  不带40

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        strategyId        	LONG    	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	Default 500; max 1000.
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMGetOrderEndpoints.get_cm_conditional_allOrders, **to_local(locals()))


    # 查询杠杆账户订单 (USER_DATA)
    def get_margin_order(self,symbol:str = '',orderId:int = '',origClientOrderId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/margin/order

        权重(IP):5

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        orderId           	LONG    	NO      	
        origClientOrderId 	STRING  	NO      	
        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMGetOrderEndpoints.get_margin_order, **to_local(locals()))


    # 查询杠杆账户挂单记录 (USER_DATA)
    def get_margin_openOrders(self,symbol:str = '',isIsolated:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/margin/openOrders

        权重(IP):5

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        isIsolated        	STRING  	NO      	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMGetOrderEndpoints.get_margin_openOrders, **to_local(locals()))


    # 查询杠杆账户的所有订单 (USER_DATA)
    def get_margin_allOrders(self,symbol:str = '',orderId:int = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/margin/allOrders

        权重(IP):100

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        orderId           	LONG    	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	默认 500;最大500.
        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMGetOrderEndpoints.get_margin_allOrders, **to_local(locals()))


    # 查询杠杆账户 OCO (USER_DATA)
    def get_margin_orderList(self,orderListId:int = '',listClientOrderId:str = '',newClientOrderId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/margin/orderList

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        orderListId       	LONG    	NO      	orderListId或listClientOrderId必须被提供
        listClientOrderId 	STRING  	NO      	orderListId或listClientOrderId必须被提供
        newClientOrderId  	STRING  	NO      	用户自定义的本次撤销操作的ID(注意不是被撤销的订单的自定义ID)。如无指定会自动赋值。
        recvWindow        	LONG    	NO      	不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMGetOrderEndpoints.get_margin_orderList, **to_local(locals()))


    # 查询特定杠杆账户所有 OCO(USER_DATA)
    def get_margin_allOrderList(self,fromId:int = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/margin/allOrderList

        权重:100

        请求参数:
        Parameter         	Type    	Required	Description

        fromId            	LONG    	NO      	提供该项后,startTime和endTime都不可提供
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	默认值: 500; 最大值: 1000
        recvWindow        	LONG    	NO      	赋值不能超过60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMGetOrderEndpoints.get_margin_allOrderList, **to_local(locals()))


    # 查询杠杆账户 OCO 挂单 (USER_DATA)
    def get_margin_openOrderList(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/margin/openOrderList

        权重(IP): 5

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMGetOrderEndpoints.get_margin_openOrderList, **to_local(locals()))


    # 查询杠杆账户交易历史 (USER_DATA)
    def get_margin_myTrades(self,symbol:str = '',orderId:int = '',startTime:int = '',endTime:int = '',fromId:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/margin/myTrades

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        orderId           	LONG    	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        fromId            	LONG    	NO      	获取TradeId，默认获取近期交易历史。
        limit             	INT     	NO      	默认 500; 最大 1000.
        recvWindow        	LONG    	NO      	默认值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMGetOrderEndpoints.get_margin_myTrades, **to_local(locals()))