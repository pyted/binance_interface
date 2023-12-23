# 行情接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _UMMarketEndpoints():


    get_ping = ['https://fapi.binance.com', 'GET', '/fapi/v1/ping', False] # 测试服务器连通性 PING
    get_time = ['https://fapi.binance.com', 'GET', '/fapi/v1/time', False] # 获取服务器时间
    get_exchangeInfo = ['https://fapi.binance.com', 'GET', '/fapi/v1/exchangeInfo', False] # 获取交易规则和交易对
    get_depth = ['https://fapi.binance.com', 'GET', '/fapi/v1/depth', False] # 深度信息
    get_trades = ['https://fapi.binance.com', 'GET', '/fapi/v1/trades', False] # 近期成交
    get_historicalTrades = ['https://fapi.binance.com', 'GET', '/fapi/v1/historicalTrades', False] # 查询历史成交(MARKET_DATA) 
    get_aggTrades = ['https://fapi.binance.com', 'GET', '/fapi/v1/aggTrades', False] # 近期成交(归集)
    get_klines = ['https://fapi.binance.com', 'GET', '/fapi/v1/klines', False] # K线数据
    get_continuousKlines = ['https://fapi.binance.com', 'GET', '/fapi/v1/continuousKlines', False] # 连续合约K线数据
    get_indexPriceKlines = ['https://fapi.binance.com', 'GET', '/fapi/v1/indexPriceKlines', False] # 价格指数K线数据
    get_markPriceKlines = ['https://fapi.binance.com', 'GET', '/fapi/v1/markPriceKlines', False] # 标记价格K线数据
    get_premiumIndexKlines = ['https://fapi.binance.com', 'GET', '/fapi/v1/premiumIndexKlines', False] # 溢价指数K线数据
    get_premiumIndex = ['https://fapi.binance.com', 'GET', '/fapi/v1/premiumIndex', False] # 最新标记价格和资金费率
    get_fundingRate = ['https://fapi.binance.com', 'GET', '/fapi/v1/fundingRate', False] # 查询资金费率历史
    get_fundingInfo = ['https://fapi.binance.com', 'GET', '/fapi/v1/fundingInfo', False] # 查询资金费率信息
    get_ticker_24hr = ['https://fapi.binance.com', 'GET', '/fapi/v1/ticker/24hr', False] # 24hr价格变动情况
    get_ticker_price_v1 = ['https://fapi.binance.com', 'GET', '/fapi/v1/ticker/price', False] # 最新价格
    get_ticker_price = ['https://fapi.binance.com', 'GET', '/fapi/v2/ticker/price', False] # 最新价格V2
    get_ticker_bookTicker = ['https://fapi.binance.com', 'GET', '/fapi/v1/ticker/bookTicker', False] # 当前最优挂单
    get_openInterest = ['https://fapi.binance.com', 'GET', '/fapi/v1/openInterest', False] # 获取未平仓合约数
    get_delivery_price = ['https://fapi.binance.com', 'GET', '/futures/data/delivery-price', False] # 季度合约历史结算价
    get_openInterestHist = ['https://fapi.binance.com', 'GET', '/futures/data/openInterestHist', False] # 合约持仓量
    get_topLongShortAccountRatio = ['https://fapi.binance.com', 'GET', '/futures/data/topLongShortAccountRatio', False] # 大户账户数多空比
    get_topLongShortPositionRatio = ['https://fapi.binance.com', 'GET', '/futures/data/topLongShortPositionRatio', False] # 大户持仓量多空比
    get_globalLongShortAccountRatio = ['https://fapi.binance.com', 'GET', '/futures/data/globalLongShortAccountRatio', False] # 多空持仓人数比
    get_takerlongshortRatio = ['https://fapi.binance.com', 'GET', '/futures/data/takerlongshortRatio', False] # 合约主动买卖量
    get_basis = ['https://fapi.binance.com', 'GET', '/futures/data/basis', False] # 基差
    get_lvtKlines = ['https://fapi.binance.com', 'GET', '/fapi/v1/lvtKlines', False] # 杠杆代币历史净值K线
    get_indexInfo = ['https://fapi.binance.com', 'GET', '/fapi/v1/indexInfo', False] # 综合指数交易对信息
    get_assetIndex = ['https://fapi.binance.com', 'GET', '/fapi/v1/assetIndex', False] # 多资产模式资产汇率指数
    get_constituents = ['https://fapi.binance.com', 'GET', '/fapi/v1/constituents', False] # 查询指数价格成分 


class UMMarket(Client):

    # 测试服务器连通性 PING
    def get_ping(self,proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/ping

        权重:1
        '''
        return self.send_request(*_UMMarketEndpoints.get_ping, **to_local(locals()))


    # 获取服务器时间
    def get_time(self,proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/time

        权重:1
        '''
        return self.send_request(*_UMMarketEndpoints.get_time, **to_local(locals()))


    # 获取交易规则和交易对
    def get_exchangeInfo(self,proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/exchangeInfo

        权重:1
        '''
        return self.send_request(*_UMMarketEndpoints.get_exchangeInfo, **to_local(locals()))


    # 深度信息
    def get_depth(self,symbol:str = '',limit:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/depth

        权重:

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        limit             	INT     	NO      	默认 500; 可选值:[5, 10, 20, 50, 100, 500, 1000]
        '''
        return self.send_request(*_UMMarketEndpoints.get_depth, **to_local(locals()))


    # 近期成交
    def get_trades(self,symbol:str = '',limit:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/trades

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        limit             	INT     	NO      	默认:500，最大1000
        '''
        return self.send_request(*_UMMarketEndpoints.get_trades, **to_local(locals()))


    # 查询历史成交(MARKET_DATA)
    def get_historicalTrades(self,symbol:str = '',limit:int = '',fromId:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/historicalTrades

        权重:20

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        limit             	INT     	NO      	默认值:500 最大值:1000.
        fromId            	LONG    	NO      	从哪一条成交id开始返回. 缺省返回最近的成交记录
        '''
        return self.send_request(*_UMMarketEndpoints.get_historicalTrades, **to_local(locals()))


    # 近期成交(归集)
    def get_aggTrades(self,symbol:str = '',fromId:int = '',startTime:int = '',endTime:int = '',limit:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/aggTrades

        权重:20

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        fromId            	LONG    	NO      	从包含fromID的成交开始返回结果
        startTime         	LONG    	NO      	从该时刻之后的成交记录开始返回结果
        endTime           	LONG    	NO      	返回该时刻为止的成交记录
        limit             	INT     	NO      	默认 500; 最大 1000.
        '''
        return self.send_request(*_UMMarketEndpoints.get_aggTrades, **to_local(locals()))


    # K线数据
    def get_klines(self,symbol:str = '',interval:str = '',startTime:int = '',endTime:int = '',limit:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/klines

        权重:取决于请求中的LIMIT参数

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        interval          	ENUM    	YES     	时间间隔
        startTime         	LONG    	NO      	起始时间
        endTime           	LONG    	NO      	结束时间
        limit             	INT     	NO      	默认值:500 最大值:1500.
        '''
        return self.send_request(*_UMMarketEndpoints.get_klines, **to_local(locals()))


    # 连续合约K线数据
    def get_continuousKlines(self,pair:str = '',contractType:str = '',interval:str = '',startTime:int = '',endTime:int = '',limit:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/continuousKlines

        权重:取决于请求中的LIMIT参数

        请求参数:
        Parameter         	Type    	Required	Description

        pair              	STRING  	YES     	标的交易对
        contractType      	ENUM    	YES     	合约类型
        interval          	ENUM    	YES     	时间间隔
        startTime         	LONG    	NO      	起始时间
        endTime           	LONG    	NO      	结束时间
        limit             	INT     	NO      	默认值:500 最大值:1500
        '''
        return self.send_request(*_UMMarketEndpoints.get_continuousKlines, **to_local(locals()))


    # 价格指数K线数据
    def get_indexPriceKlines(self,pair:str = '',interval:str = '',startTime:int = '',endTime:int = '',limit:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/indexPriceKlines

        权重:取决于请求中的LIMIT参数

        请求参数:
        Parameter         	Type    	Required	Description

        pair              	STRING  	YES     	标的交易对
        interval          	ENUM    	YES     	时间间隔
        startTime         	LONG    	NO      	起始时间
        endTime           	LONG    	NO      	结束时间
        limit             	INT     	NO      	默认值:500 最大值:1500
        '''
        return self.send_request(*_UMMarketEndpoints.get_indexPriceKlines, **to_local(locals()))


    # 标记价格K线数据
    def get_markPriceKlines(self,symbol:str = '',interval:str = '',startTime:int = '',endTime:int = '',limit:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/markPriceKlines

        权重:取决于请求中的LIMIT参数

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        interval          	ENUM    	YES     	时间间隔
        startTime         	LONG    	NO      	起始时间
        endTime           	LONG    	NO      	结束时间
        limit             	INT     	NO      	默认值:500 最大值:1500
        '''
        return self.send_request(*_UMMarketEndpoints.get_markPriceKlines, **to_local(locals()))


    # 溢价指数K线数据
    def get_premiumIndexKlines(self,symbol:str = '',interval:str = '',startTime:int = '',endTime:int = '',limit:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/premiumIndexKlines

        权重:取决于请求中的LIMIT参数

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        interval          	ENUM    	YES     	时间间隔
        startTime         	LONG    	NO      	起始时间
        endTime           	LONG    	NO      	结束时间
        limit             	INT     	NO      	默认值:500 最大值:1500
        '''
        return self.send_request(*_UMMarketEndpoints.get_premiumIndexKlines, **to_local(locals()))


    # 最新标记价格和资金费率
    def get_premiumIndex(self,symbol:str = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/premiumIndex

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	交易对
        '''
        return self.send_request(*_UMMarketEndpoints.get_premiumIndex, **to_local(locals()))


    # 查询资金费率历史
    def get_fundingRate(self,symbol:str = '',startTime:int = '',endTime:int = '',limit:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/fundingRate

        

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	交易对
        startTime         	LONG    	NO      	起始时间
        endTime           	LONG    	NO      	结束时间
        limit             	INT     	NO      	默认值:100 最大值:1000
        '''
        return self.send_request(*_UMMarketEndpoints.get_fundingRate, **to_local(locals()))


    # 查询资金费率信息
    def get_fundingInfo(self,proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/fundingInfo
        '''
        return self.send_request(*_UMMarketEndpoints.get_fundingInfo, **to_local(locals()))


    # 24hr价格变动情况
    def get_ticker_24hr(self,symbol:str = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/ticker/24hr

        权重:* 带symbol为1* 不带为40

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	交易对
        '''
        return self.send_request(*_UMMarketEndpoints.get_ticker_24hr, **to_local(locals()))


    # 最新价格
    def get_ticker_price_v1(self,symbol:str = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/ticker/price

        权重:* 单交易对1* 无交易对2

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	交易对
        '''
        return self.send_request(*_UMMarketEndpoints.get_ticker_price_v1, **to_local(locals()))


    # 最新价格V2
    def get_ticker_price(self,symbol:str = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v2/ticker/price

        权重:* 单交易对1* 无交易对2

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	交易对
        '''
        return self.send_request(*_UMMarketEndpoints.get_ticker_price, **to_local(locals()))


    # 当前最优挂单
    def get_ticker_bookTicker(self,symbol:str = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/ticker/bookTicker

        权重:* 单交易对2* 无交易对5

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	交易对
        '''
        return self.send_request(*_UMMarketEndpoints.get_ticker_bookTicker, **to_local(locals()))


    # 获取未平仓合约数
    def get_openInterest(self,symbol:str = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/openInterest

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        '''
        return self.send_request(*_UMMarketEndpoints.get_openInterest, **to_local(locals()))


    # 季度合约历史结算价
    def get_delivery_price(self,pair:str = '',proxies={},proxy_host:str=None):
        '''
        GET /futures/data/delivery-price

        

        请求参数:
        Parameter         	Type    	Required	Description

        pair              	STRING  	YES     	如BTCUSDT
        '''
        return self.send_request(*_UMMarketEndpoints.get_delivery_price, **to_local(locals()))


    # 合约持仓量
    def get_openInterestHist(self,symbol:str = '',period:str = '',limit:int = '',startTime:int = '',endTime:int = '',proxies={},proxy_host:str=None):
        '''
        GET /futures/data/openInterestHist

        

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        period            	ENUM    	YES     	"5m","15m","30m","1h","2h","4h","6h","12h","1d"
        limit             	LONG    	NO      	default 30, max 500
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO
        '''
        return self.send_request(*_UMMarketEndpoints.get_openInterestHist, **to_local(locals()))


    # 大户账户数多空比
    def get_topLongShortAccountRatio(self,symbol:str = '',period:str = '',limit:int = '',startTime:int = '',endTime:int = '',proxies={},proxy_host:str=None):
        '''
        GET /futures/data/topLongShortAccountRatio

        

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        period            	ENUM    	YES     	"5m","15m","30m","1h","2h","4h","6h","12h","1d"
        limit             	LONG    	NO      	default 30, max 500
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO
        '''
        return self.send_request(*_UMMarketEndpoints.get_topLongShortAccountRatio, **to_local(locals()))


    # 大户持仓量多空比
    def get_topLongShortPositionRatio(self,symbol:str = '',period:str = '',limit:int = '',startTime:int = '',endTime:int = '',proxies={},proxy_host:str=None):
        '''
        GET /futures/data/topLongShortPositionRatio

        

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        period            	ENUM    	YES     	"5m","15m","30m","1h","2h","4h","6h","12h","1d"
        limit             	LONG    	NO      	default 30, max 500
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO
        '''
        return self.send_request(*_UMMarketEndpoints.get_topLongShortPositionRatio, **to_local(locals()))


    # 多空持仓人数比
    def get_globalLongShortAccountRatio(self,symbol:str = '',period:str = '',limit:int = '',startTime:int = '',endTime:int = '',proxies={},proxy_host:str=None):
        '''
        GET /futures/data/globalLongShortAccountRatio

        

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        period            	ENUM    	YES     	"5m","15m","30m","1h","2h","4h","6h","12h","1d"
        limit             	LONG    	NO      	default 30, max 500
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO
        '''
        return self.send_request(*_UMMarketEndpoints.get_globalLongShortAccountRatio, **to_local(locals()))


    # 合约主动买卖量
    def get_takerlongshortRatio(self,symbol:str = '',period:str = '',limit:int = '',startTime:int = '',endTime:int = '',proxies={},proxy_host:str=None):
        '''
        GET /futures/data/takerlongshortRatio

        

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        period            	ENUM    	YES     	"5m","15m","30m","1h","2h","4h","6h","12h","1d"
        limit             	LONG    	NO      	default 30, max 500
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO
        '''
        return self.send_request(*_UMMarketEndpoints.get_takerlongshortRatio, **to_local(locals()))


    # 基差
    def get_basis(self,pair:str = '',contractType:str = '',period:str = '',limit:int = '',startTime:int = '',endTime:int = '',proxies={},proxy_host:str=None):
        '''
        GET /futures/data/basis

        

        请求参数:
        Parameter         	Type    	Required	Description

        pair              	STRING  	YES     	BTCUSDT
        contractType      	ENUM    	YES     	CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL
        period            	ENUM    	YES     	"5m","15m","30m","1h","2h","4h","6h","12h","1d"
        limit             	LONG    	NO      	Default 30,Max 500
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO
        '''
        return self.send_request(*_UMMarketEndpoints.get_basis, **to_local(locals()))


    # 杠杆代币历史净值K线
    def get_lvtKlines(self,symbol:str = '',interval:str = '',startTime:int = '',endTime:int = '',limit:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/lvtKlines

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	token name, e.g. "BTCDOWN", "BTCUP"
        interval          	ENUM    	YES     	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	默认 500, 最大 1000
        '''
        return self.send_request(*_UMMarketEndpoints.get_lvtKlines, **to_local(locals()))


    # 综合指数交易对信息
    def get_indexInfo(self,symbol:str = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/indexInfo

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO
        '''
        return self.send_request(*_UMMarketEndpoints.get_indexInfo, **to_local(locals()))


    # 多资产模式资产汇率指数
    def get_assetIndex(self,symbol:str = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/assetIndex

        权重:带symbol为1, 不带为10

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	资产对
        '''
        return self.send_request(*_UMMarketEndpoints.get_assetIndex, **to_local(locals()))


    # 查询指数价格成分
    def get_constituents(self,symbol:str = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/constituents

        权重:2

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        '''
        return self.send_request(*_UMMarketEndpoints.get_constituents, **to_local(locals()))