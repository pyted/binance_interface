# 行情接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _SPOTMarketEndpoints():


    get_ping = ['https://api.binance.com', 'GET', '/api/v3/ping', False] # 测试服务器连通性
    get_time = ['https://api.binance.com', 'GET', '/api/v3/time', False] # 获取服务器时间
    get_exchangeInfo = ['https://api.binance.com', 'GET', '/api/v3/exchangeInfo', False] # 交易规范信息
    get_depth = ['https://api.binance.com', 'GET', '/api/v3/depth', False] # 深度信息
    get_trades = ['https://api.binance.com', 'GET', '/api/v3/trades', False] # 近期成交列表
    get_historicalTrades = ['https://api.binance.com', 'GET', '/api/v3/historicalTrades', False] # 查询历史成交
    get_aggTrades = ['https://api.binance.com', 'GET', '/api/v3/aggTrades', False] # 近期成交(归集)
    get_klines = ['https://api.binance.com', 'GET', '/api/v3/klines', False] # K线数据
    get_avgPrice = ['https://api.binance.com', 'GET', '/api/v3/avgPrice', False] # 当前平均价格
    get_uiKlines = ['https://api.binance.com', 'GET', '/api/v3/uiKlines', False] # UIK线数据
    get_ticker_24hr = ['https://api.binance.com', 'GET', '/api/v3/ticker/24hr', False] # 24hr 价格变动情况
    get_ticker_tradingDay = ['https://api.binance.com', 'GET', '/api/v3/ticker/tradingDay', False] # 交易日行情(Ticker)
    get_ticker_price = ['https://api.binance.com', 'GET', '/api/v3/ticker/price', False] # 最新价格
    get_ticker_bookTicker = ['https://api.binance.com', 'GET', '/api/v3/ticker/bookTicker', False] # 当前最优挂单
    get_ticker = ['https://api.binance.com', 'GET', '/api/v3/ticker', False] # 滚动窗口价格变动统计


class SPOTMarket(Client):

    # 测试服务器连通性
    def get_ping(self,proxies={},proxy_host:str=None):
        '''
        GET /api/v3/ping

        权重(IP):1
        '''
        return self.send_request(*_SPOTMarketEndpoints.get_ping, **to_local(locals()))


    # 获取服务器时间
    def get_time(self,proxies={},proxy_host:str=None):
        '''
        GET /api/v3/time

        权重(IP):1
        '''
        return self.send_request(*_SPOTMarketEndpoints.get_time, **to_local(locals()))


    # 交易规范信息
    def get_exchangeInfo(self,proxies={},proxy_host:str=None):
        '''
        GET /api/v3/exchangeInfo

        权重(IP):20
        '''
        return self.send_request(*_SPOTMarketEndpoints.get_exchangeInfo, **to_local(locals()))


    # 深度信息
    def get_depth(self,symbol:str = '',limit:int = '',proxies={},proxy_host:str=None):
        '''
        GET /api/v3/depth

        权重(IP):

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        limit             	INT     	NO      	默认 100; 最大 5000. 可选值:[5, 10, 20, 50, 100, 500, 1000, 5000]如果 limit > 5000, 最多返回5000条数据.
        '''
        return self.send_request(*_SPOTMarketEndpoints.get_depth, **to_local(locals()))


    # 近期成交列表
    def get_trades(self,symbol:str = '',limit:int = '',proxies={},proxy_host:str=None):
        '''
        GET /api/v3/trades

        权重(IP):10

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        limit             	INT     	NO      	默认 500; 最大值 1000.
        '''
        return self.send_request(*_SPOTMarketEndpoints.get_trades, **to_local(locals()))


    # 查询历史成交
    def get_historicalTrades(self,symbol:str = '',limit:int = '',fromId:int = '',proxies={},proxy_host:str=None):
        '''
        GET /api/v3/historicalTrades

        权重(IP):10

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        limit             	INT     	NO      	默认 500; 最大值 1000.
        fromId            	LONG    	NO      	从哪一条成交id开始返回. 缺省返回最近的成交记录。
        '''
        return self.send_request(*_SPOTMarketEndpoints.get_historicalTrades, **to_local(locals()))


    # 近期成交(归集)
    def get_aggTrades(self,symbol:str = '',fromId:int = '',startTime:int = '',endTime:int = '',limit:int = '',proxies={},proxy_host:str=None):
        '''
        GET /api/v3/aggTrades

        权重(IP):2

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        fromId            	LONG    	NO      	从包含fromId的成交id开始返回结果
        startTime         	LONG    	NO      	从该时刻之后的成交记录开始返回结果
        endTime           	LONG    	NO      	返回该时刻为止的成交记录
        limit             	INT     	NO      	默认 500; 最大 1000.
        '''
        return self.send_request(*_SPOTMarketEndpoints.get_aggTrades, **to_local(locals()))


    # K线数据
    def get_klines(self,symbol:str = '',interval:str = '',startTime:int = '',endTime:int = '',timeZone:str = '',limit:int = '',proxies={},proxy_host:str=None):
        '''
        GET /api/v3/klines

        权重(IP):2

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        interval          	ENUM    	YES     	详见枚举定义：K线间隔
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        timeZone          	STRING  	NO      	默认: 0 (UTC)
        limit             	INT     	NO      	默认 500; 最大 1000.
        '''
        return self.send_request(*_SPOTMarketEndpoints.get_klines, **to_local(locals()))


    # 当前平均价格
    def get_avgPrice(self,symbol:str = '',proxies={},proxy_host:str=None):
        '''
        GET /api/v3/avgPrice

        权重(IP):2

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES
        '''
        return self.send_request(*_SPOTMarketEndpoints.get_avgPrice, **to_local(locals()))


    # UIK线数据
    def get_uiKlines(self,symbol:str = '',interval:str = '',startTime:int = '',endTime:int = '',timeZone:str = '',limit:int = '',proxies={},proxy_host:str=None):
        '''
        GET /api/v3/uiKlines

        权重(IP):2

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        interval          	ENUM    	YES     	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        timeZone          	STRING  	NO      	Default: 0 (UTC)
        limit             	INT     	NO      	默认 500; 最大 1000.
        '''
        return self.send_request(*_SPOTMarketEndpoints.get_uiKlines, **to_local(locals()))


    # 24hr 价格变动情况
    def get_ticker_24hr(self,symbol:str = '',symbols:str = '',type:str = '',proxies={},proxy_host:str=None):
        '''
        GET /api/v3/ticker/24hr

        权重(IP):

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	参数 `symbol` 和 `symbols` 不可以一起使用如果都不提供, 所有symbol的ticker数据都会返回.symbols参数可接受的格式：
         ["BTCUSDT","BNBUSDT"]或%5B%22BTCUSDT%22,%22BNBUSDT%22%5D
        symbols           	STRING  	NO      	
        type              	ENUM    	NO      	可接受的参数:FULLorMINI.如果不提供, 默认值为FULL
        '''
        return self.send_request(*_SPOTMarketEndpoints.get_ticker_24hr, **to_local(locals()))


    # 交易日行情(Ticker)
    def get_ticker_tradingDay(self,symbol:str='', symbols:list=[], timeZone:str='', type:str='', proxies={},proxy_host:str=None):
        '''
        GET /api/v3/ticker/tradingDay

        权重:
            每个交易对占用4个权重.
            当请求中的交易对数量超过50，此请求的权重将限制在200。

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES      	symbol 或者 symbols 必须提供之一
        symbols           	STRING  	            symbols 可以接受的格式: ["BTCUSDT","BNBUSDT"] 或者 %5B%22BTCUSDT%22,%22BNBUSDT%22%5D symbols 最多可以发送100个.
        timeZone            STRING      NO          Default: 0 (UTC)
        type              	ENUM    	NO      	可接受值: FULL or MINI. 默认值: FULL
        '''
        return self.send_request(*_SPOTMarketEndpoints.get_ticker_tradingDay, **to_local(locals()))


    # 最新价格
    def get_ticker_price(self,symbol:str = '',symbols:str = '',proxies={},proxy_host:str=None):
        '''
        GET /api/v3/ticker/price

        权重(IP):

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	参数 `symbol` 和 `symbols` 不可以一起使用如果都不提供, 所有symbol的价格数据都会返回.symbols参数可接受的格式：
         ["BTCUSDT","BNBUSDT"]或%5B%22BTCUSDT%22,%22BNBUSDT%22%5D
        symbols           	STRING  	NO
        '''
        return self.send_request(*_SPOTMarketEndpoints.get_ticker_price, **to_local(locals()))


    # 当前最优挂单
    def get_ticker_bookTicker(self,symbol:str = '',symbols:str = '',proxies={},proxy_host:str=None):
        '''
        GET /api/v3/ticker/bookTicker

        权重(IP):

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	参数 `symbol` 和 `symbols` 不可以一起使用如果都不提供, 所有symbol的价格数据都会返回.symbols参数可接受的格式：
         ["BTCUSDT","BNBUSDT"]或%5B%22BTCUSDT%22,%22BNBUSDT%22%5D
        symbols           	STRING  	NO
        '''
        return self.send_request(*_SPOTMarketEndpoints.get_ticker_bookTicker, **to_local(locals()))


    # 滚动窗口价格变动统计
    def get_ticker(self,symbol:str='', symbols:list=[], windowSize:str='', type:str='', proxies={},proxy_host:str=None):
        '''
        GET /api/v3/ticker

        权重(IP):4/交易对.如果symbols请求的交易对超过50, 上限是200.

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES      	symbol 或者 symbols 必须提供之一
        symbols           	STRING  	            symbols 可以接受的格式: ["BTCUSDT","BNBUSDT"] 或者 %5B%22BTCUSDT%22,%22BNBUSDT%22%5D symbols 最多可以发送100个.
        windowSize          ENUM        NO          默认为 1d
                                                        windowSize 支持的值:
                                                        如果是分钟: 1m,2m....59m
                                                        如果是小时: 1h, 2h....23h
                                                        如果是天: 1d...7d
        type              	ENUM    	NO      	可接受值: FULL or MINI. 默认值: FULL
        '''
        return self.send_request(*_SPOTMarketEndpoints.get_ticker, **to_local(locals()))