# 合约接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _FuturesEndpoints():


    set_futures_transfer = ['https://api.binance.com', 'POST', '/sapi/v1/futures/transfer', True] # 合约资金划转 (USER_DATA) 
    get_futures_transfer = ['https://api.binance.com', 'GET', '/sapi/v1/futures/transfer', True] # 获取合约资金划转历史 (USER_DATA) 
    get_futures_histDataLink = ['https://api.binance.com', 'GET', '/sapi/v1/futures/histDataLink', True] # 获取合约订单薄历史数据下载地址(USER_DATA)  


class Futures(Client):

    # 合约资金划转 (USER_DATA)
    def set_futures_transfer(self,asset:str = '',amount:Union[int,float] = '',type:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/futures/transfer

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	YES     	The asset being transferred, e.g., USDT
        amount            	DECIMAL 	YES     	The amount to be transferred
        type              	INT     	YES     	1:现货账户向USDT合约账户划转2:USDT合约账户向现货账户划转3:现货账户向币本位合约账户划转4:币本位合约账户向现货账户划转
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_FuturesEndpoints.set_futures_transfer, **to_local(locals()))


    # 获取合约资金划转历史 (USER_DATA)
    def get_futures_transfer(self,asset:str = '',startTime:int = '',endTime:int = '',current:int = '',size:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/futures/transfer

        权重(IP):10

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	NO      	
        startTime         	LONG    	YES     	
        endTime           	LONG    	NO      	
        current           	LONG    	NO      	当前页面. 起始计数为1. 默认值1
        size              	LONG    	NO      	单页数据条目数，默认:10 最大:100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_FuturesEndpoints.get_futures_transfer, **to_local(locals()))


    # 获取合约订单薄历史数据下载地址(USER_DATA)
    def get_futures_histDataLink(self,symbol:str = '',dataType:str = '',startTime:int = '',endTime:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/futures/histDataLink

        权重(IP):200

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对，如BTCUSDT或BTCUSD_PERP ｜
        dataType          	ENUM    	YES     	T_DEPTHfor ticklevel orderbook data,S_DEPTHfor orderbook snapshot data
        startTime         	LONG    	YES     	
        endTime           	LONG    	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_FuturesEndpoints.get_futures_histDataLink, **to_local(locals()))