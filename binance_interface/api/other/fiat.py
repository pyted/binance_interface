# 法币接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _FiatEndpoints():


    get_fiat_orders = ['https://api.binance.com', 'GET', '/sapi/v1/fiat/orders', True] # 获取法币充值/提现历史记录 (USER_DATA) 
    get_fiat_payments = ['https://api.binance.com', 'GET', '/sapi/v1/fiat/payments', True] # 获取法币支付历史记录 (USER_DATA)  


class Fiat(Client):

    # 获取法币充值/提现历史记录 (USER_DATA)
    def get_fiat_orders(self,transactionType:str = '',beginTime:int = '',endTime:int = '',page:int = '',rows:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/fiat/orders

        权重(UID):90000

        请求参数:
        Parameter         	Type    	Required	Description

        transactionType   	STRING  	YES     	0-deposit,1-withdraw
        beginTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        page              	INT     	NO      	默认 1
        rows              	INT     	NO      	默认 100, 最大 500
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_FiatEndpoints.get_fiat_orders, **to_local(locals()))


    # 获取法币支付历史记录 (USER_DATA)
    def get_fiat_payments(self,transactionType:str = '',beginTime:int = '',endTime:int = '',page:int = '',rows:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/fiat/payments

        

        请求参数:
        Parameter         	Type    	Required	Description

        transactionType   	STRING  	YES     	0-buy,1-sell
        beginTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        page              	INT     	NO      	默认 1
        rows              	INT     	NO      	默认 100, 最大 500
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_FiatEndpoints.get_fiat_payments, **to_local(locals()))