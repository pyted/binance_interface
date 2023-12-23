# 经典统一账户接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _CMPortfolioEndpoints():


    get_pmExchangeInfo = ['https://dapi.binance.com', 'GET', '/dapi/v1/pmExchangeInfo', True] # 查询经典统一账户Notional Limit(USER_DATA) 
    get_pmAccountInfo = ['https://dapi.binance.com', 'GET', '/dapi/v1/pmAccountInfo', True] # 查询经典统一账户账户信息 (USER_DATA)  


class CMPortfolio(Client):

    # 查询经典统一账户Notional Limit(USER_DATA)
    def get_pmExchangeInfo(self,symbol:str = '',pair:str = '',proxies={},proxy_host:str=None):
        '''
        GET /dapi/v1/pmExchangeInfo

        权重(IP)：5

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        pair              	STRING  	NO
        '''
        return self.send_request(*_CMPortfolioEndpoints.get_pmExchangeInfo, **to_local(locals()))


    # 查询经典统一账户账户信息 (USER_DATA)
    def get_pmAccountInfo(self,asset:str = '',recvWindow:int = '',proxies={},proxy_host:str=None):
        '''
        GET /dapi/v1/pmAccountInfo

        权重(IP)：5

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	YES     	
        recvWindow        	LONG    	NO
        '''
        return self.send_request(*_CMPortfolioEndpoints.get_pmAccountInfo, **to_local(locals()))