# 行情接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _EOMarketEndpoints():


    get_ping = ['https://eapi.binance.com', 'GET', '/eapi/v1/ping', False] # 测试服务器连通性 PING【
    get_time = ['https://eapi.binance.com', 'GET', '/eapi/v1/time', False] # 获取服务器时间【
    get_exchangeInfo = ['https://eapi.binance.com', 'GET', '/eapi/v1/exchangeInfo', False] # 获取交易规则和交易对【
    get_depth = ['https://eapi.binance.com', 'GET', '/eapi/v1/depth', False] # 深度信息
    get_trades = ['https://eapi.binance.com', 'GET', '/eapi/v1/trades', False] # 近期成交
    get_historicalTrades = ['https://eapi.binance.com', 'GET', '/eapi/v1/historicalTrades', False] # 查询历史成交(MARKET_DATA) 
    get_klines = ['https://eapi.binance.com', 'GET', '/eapi/v1/klines', False] # K线数据
    get_mark = ['https://eapi.binance.com', 'GET', '/eapi/v1/mark', False] # 查询期权标记价格
    get_ticker = ['https://eapi.binance.com', 'GET', '/eapi/v1/ticker', False] # 24hr价格变动情况
    get_index = ['https://eapi.binance.com', 'GET', '/eapi/v1/index', False] # 标的最新价格
    get_exerciseHistory = ['https://eapi.binance.com', 'GET', '/eapi/v1/exerciseHistory', False] # 历史行权记录
    get_openInterest = ['https://eapi.binance.com', 'GET', '/eapi/v1/openInterest', False] # 合约持仓量 


class EOMarket(Client):

    # 测试服务器连通性 PING
    def get_ping(self,proxies={},proxy_host:str=None):
        '''
        GET /eapi/v1/ping

        权重:1
        '''
        return self.send_request(*_EOMarketEndpoints.get_ping, **to_local(locals()))


    # 获取服务器时间
    def get_time(self,proxies={},proxy_host:str=None):
        '''
        GET /eapi/v1/time

        权重:1
        '''
        return self.send_request(*_EOMarketEndpoints.get_time, **to_local(locals()))


    # 获取交易规则和交易对
    def get_exchangeInfo(self,proxies={},proxy_host:str=None):
        '''
        GET /eapi/v1/exchangeInfo

        权重:1
        '''
        return self.send_request(*_EOMarketEndpoints.get_exchangeInfo, **to_local(locals()))


    # 深度信息
    def get_depth(self,symbol:str = '',limit:int = '',proxies={},proxy_host:str=None):
        '''
        GET /eapi/v1/depth

        权重:

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        limit             	INT     	NO      	默认 100; 可选值:[10, 20, 50, 100, 500, 1000]
        '''
        return self.send_request(*_EOMarketEndpoints.get_depth, **to_local(locals()))


    # 近期成交
    def get_trades(self,symbol:str = '',limit:int = '',proxies={},proxy_host:str=None):
        '''
        GET /eapi/v1/trades

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        limit             	INT     	NO      	默认:100，最大500
        '''
        return self.send_request(*_EOMarketEndpoints.get_trades, **to_local(locals()))


    # 查询历史成交(MARKET_DATA)
    def get_historicalTrades(self,symbol:str = '',limit:int = '',fromId:int = '',proxies={},proxy_host:str=None):
        '''
        GET /eapi/v1/historicalTrades

        权重:20

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        limit             	INT     	NO      	默认值:100 最大值:500.
        fromId            	LONG    	NO      	从哪一条成交id开始返回. 缺省返回最近的成交记录
        '''
        return self.send_request(*_EOMarketEndpoints.get_historicalTrades, **to_local(locals()))


    # K线数据
    def get_klines(self,symbol:str = '',interval:str = '',startTime:int = '',endTime:int = '',limit:int = '',proxies={},proxy_host:str=None):
        '''
        GET /eapi/v1/klines

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        interval          	ENUM    	YES     	时间间隔
        startTime         	LONG    	NO      	起始时间
        endTime           	LONG    	NO      	结束时间
        limit             	INT     	NO      	默认值:500 最大值:1500.
        '''
        return self.send_request(*_EOMarketEndpoints.get_klines, **to_local(locals()))


    # 查询期权标记价格
    def get_mark(self,symbol:str = '',proxies={},proxy_host:str=None):
        '''
        GET /eapi/v1/mark

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	交易对
        '''
        return self.send_request(*_EOMarketEndpoints.get_mark, **to_local(locals()))


    # 24hr价格变动情况
    def get_ticker(self,symbol:str = '',proxies={},proxy_host:str=None):
        '''
        GET /eapi/v1/ticker

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	交易对
        '''
        return self.send_request(*_EOMarketEndpoints.get_ticker, **to_local(locals()))


    # 标的最新价格
    def get_index(self,underlying:str = '',proxies={},proxy_host:str=None):
        '''
        GET /eapi/v1/index

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        underlying        	STRING  	YES     	现货交易对如BTCUSDT
        '''
        return self.send_request(*_EOMarketEndpoints.get_index, **to_local(locals()))


    # 历史行权记录
    def get_exerciseHistory(self,underlying:str = '',startTime:int = '',endTime:int = '',limit:int = '',proxies={},proxy_host:str=None):
        '''
        GET /eapi/v1/exerciseHistory

        权重:3

        请求参数:
        Parameter         	Type    	Required	Description

        underlying        	STRING  	NO      	标的资产如BTCUSDT
        startTime         	LONG    	NO      	开始时间
        endTime           	LONG    	NO      	结束时间
        limit             	INT     	NO      	默认值:100 最大值:100.
        '''
        return self.send_request(*_EOMarketEndpoints.get_exerciseHistory, **to_local(locals()))


    # 合约持仓量
    def get_openInterest(self,underlyingAsset:str = '',expiration:str = '',proxies={},proxy_host:str=None):
        '''
        GET /eapi/v1/openInterest

        

        请求参数:
        Parameter         	Type    	Required	Description

        underlyingAsset   	STRING  	YES     	标的资产，如ETH或BTC
        expiration        	STRING  	YES     	到期日，如221225
        '''
        return self.send_request(*_EOMarketEndpoints.get_openInterest, **to_local(locals()))