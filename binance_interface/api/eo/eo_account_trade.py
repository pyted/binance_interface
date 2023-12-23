# 账户和交易接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _EOAccountTradeEndpoints():


    get_account = ['https://eapi.binance.com', 'GET', '/eapi/v1/account', True] # 账户信息 (TRADE) 
    set_order = ['https://eapi.binance.com', 'POST', '/eapi/v1/order', True] # 下单 (TRADE) 
    set_batchOrders = ['https://eapi.binance.com', 'POST', '/eapi/v1/batchOrders', True] # 批量下单 (TRADE) 
    get_order = ['https://eapi.binance.com', 'GET', '/eapi/v1/order', True] # 查询单个订单 (TRADE) 
    cancel_order = ['https://eapi.binance.com', 'DELETE', '/eapi/v1/order', True] # 撤销订单 (TRADE) 
    cancel_batchOrders = ['https://eapi.binance.com', 'DELETE', '/eapi/v1/batchOrders', True] # 批量撤销订单 (TRADE) 
    cancel_allOpenOrders = ['https://eapi.binance.com', 'DELETE', '/eapi/v1/allOpenOrders', True] # 撤销单交易对全部订单 (TRADE) 
    cancel_allOpenOrdersByUnderlying = ['https://eapi.binance.com', 'DELETE', '/eapi/v1/allOpenOrdersByUnderlying', True] # 撤销特定标的全部订单 (TRADE) 
    get_openOrders = ['https://eapi.binance.com', 'GET', '/eapi/v1/openOrders', True] # 查询当前挂单 (USER_DATA) 
    get_historyOrders = ['https://eapi.binance.com', 'GET', '/eapi/v1/historyOrders', True] # 查询历史订单 (USER_DATA) 
    get_position = ['https://eapi.binance.com', 'GET', '/eapi/v1/position', True] # 仓位信息 (USER_DATA) 
    get_userTrades = ['https://eapi.binance.com', 'GET', '/eapi/v1/userTrades', True] # 账户成交历史 (USER_DATA) 
    get_exerciseRecord = ['https://eapi.binance.com', 'GET', '/eapi/v1/exerciseRecord', True] # 用户行权历史(USER_DATA) 
    get_bill = ['https://eapi.binance.com', 'GET', '/eapi/v1/bill', True] # 获取账户资金流水(USER_DATA) 
    get_income_asyn = ['https://eapi.binance.com', 'GET', '/eapi/v1/income/asyn', True] # 获取期权资金流水下载Id (USER_DATA) 
    get_income_asyn_id = ['https://eapi.binance.com', 'GET', '/eapi/v1/income/asyn/id', True] # 通过下载Id获取合约资金流水下载链接 (USER_DATA)  


class EOAccountTrade(Client):

    # 账户信息 (TRADE)
    def get_account(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /eapi/v1/account

        权重:3

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_EOAccountTradeEndpoints.get_account, **to_local(locals()))


    # 下单 (TRADE)
    def set_order(self,symbol:str = '',side:str = '',type:str = '',quantity:Union[int,float] = '',price:Union[int,float] = '',timeInForce:str = '',reduceOnly:str = '',postOnly:str = '',newOrderRespType:str = '',clientOrderId:str = '',isMmp:bool = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /eapi/v1/order

        

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        side              	ENUM    	YES     	买卖方向SELL,BUY
        type              	ENUM    	YES     	订单类型LIMIT
        quantity          	DECIMAL 	YES     	下单数量
        price             	DECIMAL 	NO      	委托价格
        timeInForce       	ENUM    	NO      	有效时间
        reduceOnly        	STRING  	NO      	仅减仓true,false
        postOnly          	STRING  	NO      	仅做makertrue,false
        newOrderRespType  	ENUM    	NO      	"ACK", "RESULT", 默认 "ACK"
        clientOrderId     	STRING  	NO      	用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。
        isMmp             	BOOLEAN 	NO      	是否为MMP订单true/false
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_EOAccountTradeEndpoints.set_order, **to_local(locals()))


    # 批量下单 (TRADE)
    def set_batchOrders(self,orders:list = [],recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /eapi/v1/batchOrders

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        orders            	LIST    	YES     	订单列表，最多支持5个订单
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_EOAccountTradeEndpoints.set_batchOrders, **to_local(locals()))


    # 查询单个订单 (TRADE)
    def get_order(self,symbol:str = '',orderId:int = '',clientOrderId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /eapi/v1/order

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对如：BTC-200730-9000-C
        orderId           	LONG    	NO      	订单id
        clientOrderId     	STRING  	NO      	用户自定义的订单号
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_EOAccountTradeEndpoints.get_order, **to_local(locals()))


    # 撤销订单 (TRADE)
    def cancel_order(self,symbol:str = '',orderId:int = '',clientOrderId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /eapi/v1/order

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        orderId           	LONG    	NO      	系统订单号
        clientOrderId     	STRING  	NO      	用户自定义的订单号
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_EOAccountTradeEndpoints.cancel_order, **to_local(locals()))


    # 批量撤销订单 (TRADE)
    def cancel_batchOrders(self,symbol:str = '',orderIds:list = [],clientOrderIds:list = [],recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /eapi/v1/batchOrders

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        orderIds          	LIST<LONG>	NO      	系统订单号比如 [4611875134427365377,4611875134427365378]
        clientOrderIds    	LIST<STRING>	NO      	用户自定义的订单号比如["my_id_1","my_id_2"] 需要encode双引号。逗号后面没有空格。
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_EOAccountTradeEndpoints.cancel_batchOrders, **to_local(locals()))


    # 撤销单交易对全部订单 (TRADE)
    def cancel_allOpenOrders(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /eapi/v1/allOpenOrders

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_EOAccountTradeEndpoints.cancel_allOpenOrders, **to_local(locals()))


    # 撤销特定标的全部订单 (TRADE)
    def cancel_allOpenOrdersByUnderlying(self,underlying:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /eapi/v1/allOpenOrdersByUnderlying

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        underlying        	STRING  	YES     	标的资产如BTCUSDT
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_EOAccountTradeEndpoints.cancel_allOpenOrdersByUnderlying, **to_local(locals()))


    # 查询当前挂单 (USER_DATA)
    def get_openOrders(self,symbol:str = '',orderId:int = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /eapi/v1/openOrders

        权重:带symbol 1，不带40

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	交易对(不传返回所有订单)
        orderId           	LONG    	NO      	只返回此orderID及之后的订单，缺省返回最近的订单
        startTime         	LONG    	NO      	开始时间
        endTime           	LONG    	NO      	结束时间
        limit             	INT     	NO      	返回数量，默认100 最大1000
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_EOAccountTradeEndpoints.get_openOrders, **to_local(locals()))


    # 查询历史订单 (USER_DATA)
    def get_historyOrders(self,symbol:str = '',orderId:int = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /eapi/v1/historyOrders

        权重:3

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        orderId           	LONG    	NO      	只返回此orderID及之后的订单，缺省返回最近的订单
        startTime         	LONG    	NO      	起始时间
        endTime           	LONG    	NO      	结束时间
        limit             	INT     	NO      	返回的结果集数量 默认值:500 最大值:1000
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_EOAccountTradeEndpoints.get_historyOrders, **to_local(locals()))


    # 仓位信息 (USER_DATA)
    def get_position(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /eapi/v1/position

        

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	交易对如BTC-200730-9000-C
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_EOAccountTradeEndpoints.get_position, **to_local(locals()))


    # 账户成交历史 (USER_DATA)
    def get_userTrades(self,symbol:str = '',fromId:int = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /eapi/v1/userTrades

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	交易对
        fromId            	LONG    	NO      	返回该fromId及之后的成交，缺省返回最近的成交
        startTime         	LONG    	NO      	起始时间
        endTime           	LONG    	NO      	结束时间
        limit             	INT     	NO      	返回的结果集数量 默认值:100 最大值:1000.
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_EOAccountTradeEndpoints.get_userTrades, **to_local(locals()))


    # 用户行权历史(USER_DATA)
    def get_exerciseRecord(self,symbol:str = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /eapi/v1/exerciseRecord

        

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	交易对如 BTC-200730-9000-C
        startTime         	LONG    	NO      	起始时间如1593511200000
        endTime           	LONG    	NO      	结束时间如1593512200000
        limit             	INT     	NO      	默认1000, 最大1000
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_EOAccountTradeEndpoints.get_exerciseRecord, **to_local(locals()))


    # 获取账户资金流水(USER_DATA)
    def get_bill(self,currency:str = '',recordId:int = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /eapi/v1/bill

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        currency          	STRING  	YES     	资产类型如USDT
        recordId          	LONG    	NO      	返回该recordId及之后的成交，缺省返回最近的成交
        startTime         	LONG    	NO      	起始时间如1593511200000
        endTime           	LONG    	NO      	结束时间如1593512200000
        limit             	INT     	NO      	默认100 最大1000
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_EOAccountTradeEndpoints.get_bill, **to_local(locals()))


    # 获取期权资金流水下载Id (USER_DATA)
    def get_income_asyn(self,startTime:int = '',endTime:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /eapi/v1/income/asyn

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        startTime         	LONG    	YES     	起始时间，ms格式时间戳
        endTime           	LONG    	YES     	结束时间，ms格式时间戳
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_EOAccountTradeEndpoints.get_income_asyn, **to_local(locals()))


    # 通过下载Id获取合约资金流水下载链接 (USER_DATA)
    def get_income_asyn_id(self,downloadId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /eapi/v1/income/asyn/id

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        downloadId        	STRING  	YES     	通过下载id 接口获取
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_EOAccountTradeEndpoints.get_income_asyn_id, **to_local(locals()))