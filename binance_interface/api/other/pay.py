# Pay 接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _PayEndpoints():


    get_pay_transactions = ['https://api.binance.com', 'GET', '/sapi/v1/pay/transactions', True] # 获取 Pay 交易历史记录 (USER_DATA)  


class Pay(Client):

    # 获取 Pay 交易历史记录 (USER_DATA)
    def get_pay_transactions(self,startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/pay/transactions

        权重(UID):3000

        请求参数:
        Parameter         	Type    	Required	Description

        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	默认 100, 最大 100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PayEndpoints.get_pay_transactions, **to_local(locals()))