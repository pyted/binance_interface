# 杠杆代币接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _MarginBlvtEndpoints():


    get_blvt_tokenInfo = ['https://api.binance.com', 'GET', '/sapi/v1/blvt/tokenInfo', False] # 杠杆代币信息 (MARKET_DATA) 
    set_blvt_subscribe = ['https://api.binance.com', 'POST', '/sapi/v1/blvt/subscribe', True] # 申购代币 (USER_DATA) 
    get_blvt_subscribe_record = ['https://api.binance.com', 'GET', '/sapi/v1/blvt/subscribe/record', True] # 查询申购记录 (USER_DATA) 
    set_blvt_redeem = ['https://api.binance.com', 'POST', '/sapi/v1/blvt/redeem', True] # 赎回代币 (USER_DATA) 
    get_blvt_redeem_record = ['https://api.binance.com', 'GET', '/sapi/v1/blvt/redeem/record', True] # 查询赎回记录 (USER_DATA) 
    get_blvt_userLimit = ['https://api.binance.com', 'GET', '/sapi/v1/blvt/userLimit', True] # 查询用户每日申购赎回限额 (USER_DATA)  


class MarginBlvt(Client):

    # 杠杆代币信息 (MARKET_DATA)
    def get_blvt_tokenInfo(self,tokenName:str = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/blvt/tokenInfo

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        tokenName         	STRING  	NO      	BTCDOWN, BTCUP
        '''
        return self.send_request(*_MarginBlvtEndpoints.get_blvt_tokenInfo, **to_local(locals()))


    # 申购代币 (USER_DATA)
    def set_blvt_subscribe(self,tokenName:str = '',cost:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/blvt/subscribe

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        tokenName         	STRING  	YES     	BTCDOWN, BTCUP
        cost              	DECIMAL 	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginBlvtEndpoints.set_blvt_subscribe, **to_local(locals()))


    # 查询申购记录 (USER_DATA)
    def get_blvt_subscribe_record(self,tokenName:str = '',id:int = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/blvt/subscribe/record

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        tokenName         	STRING  	NO      	BTCDOWN, BTCUP
        id                	LONG    	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	默认 1000, 最大 1000
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginBlvtEndpoints.get_blvt_subscribe_record, **to_local(locals()))


    # 赎回代币 (USER_DATA)
    def set_blvt_redeem(self,tokenName:str = '',amount:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/blvt/redeem

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        tokenName         	STRING  	YES     	BTCDOWN, BTCUP
        amount            	DECIMAL 	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginBlvtEndpoints.set_blvt_redeem, **to_local(locals()))


    # 查询赎回记录 (USER_DATA)
    def get_blvt_redeem_record(self,tokenName:str = '',id:int = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/blvt/redeem/record

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        tokenName         	STRING  	NO      	BTCDOWN, BTCUP
        id                	LONG    	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	默认 1000, 最大 1000
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginBlvtEndpoints.get_blvt_redeem_record, **to_local(locals()))


    # 查询用户每日申购赎回限额 (USER_DATA)
    def get_blvt_userLimit(self,tokenName:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/blvt/userLimit

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        tokenName         	STRING  	NO      	BTCDOWN, BTCUP
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginBlvtEndpoints.get_blvt_userLimit, **to_local(locals()))