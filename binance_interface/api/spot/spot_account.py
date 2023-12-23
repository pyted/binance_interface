# 现货账户接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _SPOTAccountEndpoints():


    get_account = ['https://api.binance.com', 'GET', '/api/v3/account', True] # 账户信息 (USER_DATA) 
    get_myTrades = ['https://api.binance.com', 'GET', '/api/v3/myTrades', True] # 账户成交历史 (USER_DATA) 
    get_rateLimit_order = ['https://api.binance.com', 'GET', '/api/v3/rateLimit/order', True] # 查询目前下单数 (TRADE) 
    get_myPreventedMatches = ['https://api.binance.com', 'GET', '/api/v3/myPreventedMatches', True] # 获取 Prevented Matches (USER_DATA) 
    get_myAllocations = ['https://api.binance.com', 'GET', '/api/v3/myAllocations', True] # 查询分配结果 (USER_DATA) 
    get_account_commission = ['https://api.binance.com', 'GET', '/api/v3/account/commission', True] # 查询佣金费率 (USER_DATA)  


class SPOTAccount(Client):

    # 账户信息 (USER_DATA)
    def get_account(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /api/v3/account

        权重(IP):20

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SPOTAccountEndpoints.get_account, **to_local(locals()))


    # 账户成交历史 (USER_DATA)
    def get_myTrades(self,symbol:str = '',orderId:int = '',startTime:int = '',endTime:int = '',fromId:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /api/v3/myTrades

        权重(IP):20

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        orderId           	LONG    	NO      	必须要和参数symbol一起使用.
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        fromId            	LONG    	NO      	起始Trade id。 默认获取最新交易。
        limit             	INT     	NO      	默认 500; 最大 1000.
        recvWindow        	LONG    	NO      	赋值不能超过60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SPOTAccountEndpoints.get_myTrades, **to_local(locals()))


    # 查询目前下单数 (TRADE)
    def get_rateLimit_order(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /api/v3/rateLimit/order

        权重(IP):40

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	赋值不得大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SPOTAccountEndpoints.get_rateLimit_order, **to_local(locals()))


    # 获取 Prevented Matches (USER_DATA)
    def get_myPreventedMatches(self,symbol:str = '',preventedMatchId:int = '',orderId:int = '',fromPreventedMatchId:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /api/v3/myPreventedMatches

        权重(IP):

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        preventedMatchId  	LONG    	NO      	
        orderId           	LONG    	NO      	
        fromPreventedMatchId	LONG    	NO      	
        limit             	INT     	NO      	默认：500；最大：1000
        recvWindow        	LONG    	NO      	赋值不得大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SPOTAccountEndpoints.get_myPreventedMatches, **to_local(locals()))


    # 查询分配结果 (USER_DATA)
    def get_myAllocations(self,symbol:str = '',startTime:int = '',endTime:int = '',fromAllocationId:int = '',limit:int = '',orderId:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /api/v3/myAllocations

        权重:20

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	Yes     	
        startTime         	LONG    	No      	
        endTime           	LONG    	No      	
        fromAllocationId  	INT     	No      	
        limit             	INT     	No      	默认值 500； 最大值 1000
        orderId           	LONG    	No      	
        recvWindow        	LONG    	No      	不能大于60000
        timestamp         	LONG    	No
        '''
        return self.send_request(*_SPOTAccountEndpoints.get_myAllocations, **to_local(locals()))


    # 查询佣金费率 (USER_DATA)
    def get_account_commission(self,symbol:str = '',proxies={},proxy_host:str=None):
        '''
        GET /api/v3/account/commission

        权重:20

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES
        '''
        return self.send_request(*_SPOTAccountEndpoints.get_account_commission, **to_local(locals()))