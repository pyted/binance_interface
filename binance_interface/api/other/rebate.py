# 返佣接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _RebateEndpoints():


    get_rebate_taxQuery = ['https://api.binance.com', 'GET', '/sapi/v1/rebate/taxQuery', True] # 获取现货返佣历史记录 (USER_DATA)  


class Rebate(Client):

    # 获取现货返佣历史记录 (USER_DATA)
    def get_rebate_taxQuery(self,startTime:int = '',endTime:int = '',page:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/rebate/taxQuery

        权重(UID):12000

        请求参数:
        Parameter         	Type    	Required	Description

        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        page              	INT     	NO      	默认 1
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_RebateEndpoints.get_rebate_taxQuery, **to_local(locals()))