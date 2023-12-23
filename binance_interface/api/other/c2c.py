# C2C 接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _C2CEndpoints():


    get_c2c_orderMatch_listUserOrderHistory = ['https://api.binance.com', 'GET', '/sapi/v1/c2c/orderMatch/listUserOrderHistory', True] # 获取 C2C 交易历史记录 (USER_DATA)  


class C2C(Client):

    # 获取 C2C 交易历史记录 (USER_DATA)
    def get_c2c_orderMatch_listUserOrderHistory(self,tradeType:str = '',startTimestamp:int = '',endTimestamp:int = '',page:int = '',rows:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/c2c/orderMatch/listUserOrderHistory

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        tradeType         	STRING  	YES     	BUY, SEll
        startTimestamp    	LONG    	NO      	
        endTimestamp      	LONG    	NO      	
        page              	INT     	NO      	default 1
        rows              	INT     	NO      	default 100, max 100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_C2CEndpoints.get_c2c_orderMatch_listUserOrderHistory, **to_local(locals()))