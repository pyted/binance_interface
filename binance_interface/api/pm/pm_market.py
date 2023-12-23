# 行情接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _PMMarketEndpoints():


    get_ping = ['https://papi.binance.com', 'GET', '/papi/v1/ping', False] # 测试服务器连通性 PING


class PMMarket(Client):

    # 测试服务器连通性 PING
    def get_ping(self,proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/ping

        权重:1

        
        '''
        return self.send_request(*_PMMarketEndpoints.get_ping, **to_local(locals()))