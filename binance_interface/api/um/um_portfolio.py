# 经典统一账户
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _UMPortfolioEndpoints():


    get_pmAccountInfo = ['https://fapi.binance.com', 'GET', '/fapi/v1/pmAccountInfo', True] # 查询经典统一账户账户信息 (USER_DATA)  


class UMPortfolio(Client):

    # 查询经典统一账户账户信息 (USER_DATA)
    def get_pmAccountInfo(self,asset:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/pmAccountInfo

        权重(IP)：5

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMPortfolioEndpoints.get_pmAccountInfo, **to_local(locals()))