# 账户和交易接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _UMAccountTradeEndpoints():


    set_positionSide_dual = ['https://fapi.binance.com', 'POST', '/fapi/v1/positionSide/dual', True] # 更改持仓模式(TRADE) 
    get_positionSide_dual = ['https://fapi.binance.com', 'GET', '/fapi/v1/positionSide/dual', True] # 查询持仓模式(USER_DATA) 
    set_multiAssetsMargin = ['https://fapi.binance.com', 'POST', '/fapi/v1/multiAssetsMargin', True] # 更改联合保证金模式(TRADE) 
    get_multiAssetsMargin = ['https://fapi.binance.com', 'GET', '/fapi/v1/multiAssetsMargin', True] # 查询联合保证金模式(USER_DATA) 
    set_order = ['https://fapi.binance.com', 'POST', '/fapi/v1/order', True] # 下单 (TRADE) 
    set_order_test = ['https://fapi.binance.com', 'POST', '/fapi/v1/order/test', True] # 测试下单接口 (TRADE)
    alter_order = ['https://fapi.binance.com', 'PUT', '/fapi/v1/order', True] # 修改订单 (TRADE) 
    set_batchOrders = ['https://fapi.binance.com', 'POST', '/fapi/v1/batchOrders', True] # 批量下单 (TRADE) 
    alter_batchOrders = ['https://fapi.binance.com', 'PUT', '/fapi/v1/batchOrders', True] # 批量修改订单 (TRADE) 
    get_orderAmendment = ['https://fapi.binance.com', 'GET', '/fapi/v1/orderAmendment', True] # 查询订单修改历史 (USER_DATA) 
    get_order = ['https://fapi.binance.com', 'GET', '/fapi/v1/order', True] # 查询订单 (USER_DATA) 
    cancel_order = ['https://fapi.binance.com', 'DELETE', '/fapi/v1/order', True] # 撤销订单 (TRADE) 
    cancel_allOpenOrders = ['https://fapi.binance.com', 'DELETE', '/fapi/v1/allOpenOrders', True] # 撤销全部订单 (TRADE) 
    cancel_batchOrders = ['https://fapi.binance.com', 'DELETE', '/fapi/v1/batchOrders', True] # 批量撤销订单 (TRADE) 
    set_countdownCancelAll = ['https://fapi.binance.com', 'POST', '/fapi/v1/countdownCancelAll', True] # 倒计时撤销所有订单 (TRADE) 
    get_openOrder = ['https://fapi.binance.com', 'GET', '/fapi/v1/openOrder', True] # 查询当前挂单 (USER_DATA) 
    get_openOrders = ['https://fapi.binance.com', 'GET', '/fapi/v1/openOrders', True] # 查看当前全部挂单 (USER_DATA) 
    get_allOrders = ['https://fapi.binance.com', 'GET', '/fapi/v1/allOrders', True] # 查询所有订单(包括历史订单) (USER_DATA) 
    get_balance = ['https://fapi.binance.com', 'GET', '/fapi/v2/balance', True] # 账户余额V2 (USER_DATA) 
    get_account = ['https://fapi.binance.com', 'GET', '/fapi/v2/account', True] # 账户信息V2 (USER_DATA) 
    set_leverage = ['https://fapi.binance.com', 'POST', '/fapi/v1/leverage', True] # 调整开仓杠杆 (TRADE) 
    set_marginType = ['https://fapi.binance.com', 'POST', '/fapi/v1/marginType', True] # 变换逐全仓模式 (TRADE) 
    set_positionMargin = ['https://fapi.binance.com', 'POST', '/fapi/v1/positionMargin', True] # 调整逐仓保证金 (TRADE) 
    get_positionMargin_history = ['https://fapi.binance.com', 'GET', '/fapi/v1/positionMargin/history', True] # 逐仓保证金变动历史 (TRADE) 
    get_positionRisk = ['https://fapi.binance.com', 'GET', '/fapi/v2/positionRisk', True] # 用户持仓风险V2 (USER_DATA) 
    get_userTrades = ['https://fapi.binance.com', 'GET', '/fapi/v1/userTrades', True] # 账户成交历史 (USER_DATA) 
    get_income = ['https://fapi.binance.com', 'GET', '/fapi/v1/income', True] # 获取账户损益资金流水 (USER_DATA) 
    get_leverageBracket = ['https://fapi.binance.com', 'GET', '/fapi/v1/leverageBracket', True] # 杠杆分层标准 (USER_DATA) 
    get_adlQuantile = ['https://fapi.binance.com', 'GET', '/fapi/v1/adlQuantile', True] # 持仓ADL队列估算 (USER_DATA) 
    get_forceOrders = ['https://fapi.binance.com', 'GET', '/fapi/v1/forceOrders', True] # 用户强平单历史 (USER_DATA) 
    get_apiTradingStatus = ['https://fapi.binance.com', 'GET', '/fapi/v1/apiTradingStatus', True] # 合约交易量化规则指标 (USER_DATA) 
    get_commissionRate = ['https://fapi.binance.com', 'GET', '/fapi/v1/commissionRate', True] # 用户手续费率 (USER_DATA) 
    get_income_asyn = ['https://fapi.binance.com', 'GET', '/fapi/v1/income/asyn', True] # 获取合约资金流水下载Id (USER_DATA) 
    get_income_asyn_id = ['https://fapi.binance.com', 'GET', '/fapi/v1/income/asyn/id', True] # 通过下载Id获取合约资金流水下载链接 (USER_DATA) 
    get_order_asyn = ['https://fapi.binance.com', 'GET', '/fapi/v1/order/asyn', True] # 获取合约订单历史下载Id (USER_DATA) 
    get_order_asyn_id = ['https://fapi.binance.com', 'GET', '/fapi/v1/order/asyn/id', True] # 通过下载Id获取合约订单下载链接 (USER_DATA) 
    get_trade_asyn = ['https://fapi.binance.com', 'GET', '/fapi/v1/trade/asyn', True] # 获取合约交易历史下载Id (USER_DATA) 
    get_trade_asyn_id = ['https://fapi.binance.com', 'GET', '/fapi/v1/trade/asyn/id', True] # 通过下载Id获取合约交易历史下载链接 (USER_DATA)  


class UMAccountTrade(Client):

    # 更改持仓模式(TRADE)
    def set_positionSide_dual(self,dualSidePosition:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /fapi/v1/positionSide/dual

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        dualSidePosition  	STRING  	YES     	"true": 双向持仓模式；"false": 单向持仓模式
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.set_positionSide_dual, **to_local(locals()))


    # 查询持仓模式(USER_DATA)
    def get_positionSide_dual(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/positionSide/dual

        权重:30

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.get_positionSide_dual, **to_local(locals()))


    # 更改联合保证金模式(TRADE)
    def set_multiAssetsMargin(self,multiAssetsMargin:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /fapi/v1/multiAssetsMargin

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        multiAssetsMargin 	STRING  	YES     	"true": 联合保证金模式开启；"false": 联合保证金模式关闭
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.set_multiAssetsMargin, **to_local(locals()))


    # 查询联合保证金模式(USER_DATA)
    def get_multiAssetsMargin(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/multiAssetsMargin

        权重:30

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.get_multiAssetsMargin, **to_local(locals()))


    # 下单 (TRADE)
    def set_order(self,symbol:str = '',side:str = '',positionSide:str = '',type:str = '',reduceOnly:str = '',quantity:Union[int,float] = '',price:Union[int,float] = '',newClientOrderId:str = '',stopPrice:Union[int,float] = '',closePosition:str = '',activationPrice:Union[int,float] = '',callbackRate:Union[int,float] = '',timeInForce:str = '',workingType:str = '',priceProtect:str = '',newOrderRespType:str = '',priceMatch:str = '',selfTradePreventionMode:str = '',goodTillDate:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /fapi/v1/order

        权重:0

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        side              	ENUM    	YES     	买卖方向SELL,BUY
        positionSide      	ENUM    	NO      	持仓方向，单向持仓模式下非必填，默认且仅可填BOTH;在双向持仓模式下必填,且仅可选择LONG或SHORT
        type              	ENUM    	YES     	订单类型LIMIT,MARKET,STOP,TAKE_PROFIT,STOP_MARKET,TAKE_PROFIT_MARKET,TRAILING_STOP_MARKET
        reduceOnly        	STRING  	NO      	true,false; 非双开模式下默认false；双开模式下不接受此参数； 使用closePosition不支持此参数。
        quantity          	DECIMAL 	NO      	下单数量,使用closePosition不支持此参数。
        price             	DECIMAL 	NO      	委托价格
        newClientOrderId  	STRING  	NO      	用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则^[\.A-Z\:/a-z0-9_-]{1,36}$
        stopPrice         	DECIMAL 	NO      	触发价, 仅STOP,STOP_MARKET,TAKE_PROFIT,TAKE_PROFIT_MARKET需要此参数
        closePosition     	STRING  	NO      	true,false；触发后全部平仓，仅支持STOP_MARKET和TAKE_PROFIT_MARKET；不与quantity合用；自带只平仓效果，不与reduceOnly合用
        activationPrice   	DECIMAL 	NO      	追踪止损激活价格，仅TRAILING_STOP_MARKET需要此参数, 默认为下单当前市场价格(支持不同workingType)
        callbackRate      	DECIMAL 	NO      	追踪止损回调比例，可取值范围[0.1, 5],其中 1代表1% ,仅TRAILING_STOP_MARKET需要此参数
        timeInForce       	ENUM    	NO      	有效方法
        workingType       	ENUM    	NO      	stopPrice 触发类型:MARK_PRICE(标记价格),CONTRACT_PRICE(合约最新价). 默认CONTRACT_PRICE
        priceProtect      	STRING  	NO      	条件单触发保护："TRUE","FALSE", 默认"FALSE". 仅STOP,STOP_MARKET,TAKE_PROFIT,TAKE_PROFIT_MARKET需要此参数
        newOrderRespType  	ENUM    	NO      	"ACK", "RESULT", 默认 "ACK"
        symbol            	STRING  	YES     	交易对
        priceMatch        	ENUM    	NO      	OPPONENT/OPPONENT_5/OPPONENT_10/OPPONENT_20/QUEUE/QUEUE_5/QUEUE_10/QUEUE_20；不能与price同时传
        selfTradePreventionMode	ENUM    	NO      	NONE/EXPIRE_TAKER/EXPIRE_MAKER/EXPIRE_BOTH； 默认NONE
        goodTillDate      	LONG    	NO      	TIF为GTD时订单的自动取消时间， 当timeInforce为GTD时必传；传入的时间戳仅保留秒级精度，毫秒级部分会被自动忽略，时间戳需大于当前时间+600s且小于253402300799000
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.set_order, **to_local(locals()))


    # 测试下单接口 (TRADE)
    def set_order_test(self,symbol:str = '',side:str = '',positionSide:str = '',type:str = '',reduceOnly:str = '',quantity:Union[int,float] = '',price:Union[int,float] = '',newClientOrderId:str = '',stopPrice:Union[int,float] = '',closePosition:str = '',activationPrice:Union[int,float] = '',callbackRate:Union[int,float] = '',timeInForce:str = '',workingType:str = '',priceProtect:str = '',newOrderRespType:str = '',priceMatch:str = '',selfTradePreventionMode:str = '',goodTillDate:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /fapi/v1/order/test

        权重:0

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        side              	ENUM    	YES     	买卖方向SELL,BUY
        positionSide      	ENUM    	NO      	持仓方向，单向持仓模式下非必填，默认且仅可填BOTH;在双向持仓模式下必填,且仅可选择LONG或SHORT
        type              	ENUM    	YES     	订单类型LIMIT,MARKET,STOP,TAKE_PROFIT,STOP_MARKET,TAKE_PROFIT_MARKET,TRAILING_STOP_MARKET
        reduceOnly        	STRING  	NO      	true,false; 非双开模式下默认false；双开模式下不接受此参数； 使用closePosition不支持此参数。
        quantity          	DECIMAL 	NO      	下单数量,使用closePosition不支持此参数。
        price             	DECIMAL 	NO      	委托价格
        newClientOrderId  	STRING  	NO      	用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则^[\.A-Z\:/a-z0-9_-]{1,36}$
        stopPrice         	DECIMAL 	NO      	触发价, 仅STOP,STOP_MARKET,TAKE_PROFIT,TAKE_PROFIT_MARKET需要此参数
        closePosition     	STRING  	NO      	true,false；触发后全部平仓，仅支持STOP_MARKET和TAKE_PROFIT_MARKET；不与quantity合用；自带只平仓效果，不与reduceOnly合用
        activationPrice   	DECIMAL 	NO      	追踪止损激活价格，仅TRAILING_STOP_MARKET需要此参数, 默认为下单当前市场价格(支持不同workingType)
        callbackRate      	DECIMAL 	NO      	追踪止损回调比例，可取值范围[0.1, 5],其中 1代表1% ,仅TRAILING_STOP_MARKET需要此参数
        timeInForce       	ENUM    	NO      	有效方法
        workingType       	ENUM    	NO      	stopPrice 触发类型:MARK_PRICE(标记价格),CONTRACT_PRICE(合约最新价). 默认CONTRACT_PRICE
        priceProtect      	STRING  	NO      	条件单触发保护："TRUE","FALSE", 默认"FALSE". 仅STOP,STOP_MARKET,TAKE_PROFIT,TAKE_PROFIT_MARKET需要此参数
        newOrderRespType  	ENUM    	NO      	"ACK", "RESULT", 默认 "ACK"
        symbol            	STRING  	YES     	交易对
        priceMatch        	ENUM    	NO      	OPPONENT/OPPONENT_5/OPPONENT_10/OPPONENT_20/QUEUE/QUEUE_5/QUEUE_10/QUEUE_20；不能与price同时传
        selfTradePreventionMode	ENUM    	NO      	NONE/EXPIRE_TAKER/EXPIRE_MAKER/EXPIRE_BOTH； 默认NONE
        goodTillDate      	LONG    	NO      	TIF为GTD时订单的自动取消时间， 当timeInforce为GTD时必传；传入的时间戳仅保留秒级精度，毫秒级部分会被自动忽略，时间戳需大于当前时间+600s且小于253402300799000
        recvWindow        	LONG    	NO
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.set_order_test, **to_local(locals()))


    # 修改订单 (TRADE)
    def alter_order(self,orderId:int = '',origClientOrderId:str = '',symbol:str = '',side:str = '',quantity:Union[int,float] = '',price:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        PUT /fapi/v1/order

        权重:10s order rate limit(X-MBX-ORDER-COUNT-10S)为1
1min order rate limit(X-MBX-ORDER-COUNT-1M)为1
IP rate limit(x-mbx-used-weight-1m)为0

        请求参数:
        Parameter         	Type    	Required	Description

        orderId           	LONG    	NO      	系统订单号
        origClientOrderId 	STRING  	NO      	用户自定义的订单号
        symbol            	STRING  	YES     	交易对
        side              	ENUM    	YES     	买卖方向SELL,BUY;side需要和原订单相同
        quantity          	DECIMAL 	YES     	下单数量,使用closePosition不支持此参数。
        price             	DECIMAL 	YES     	委托价格
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.alter_order, **to_local(locals()))


    # 批量下单 (TRADE)
    def set_batchOrders(self,batchOrders:list = [],recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /fapi/v1/batchOrders

        权重:10s order rate limit(X-MBX-ORDER-COUNT-10S)为5
1min order rate limit(X-MBX-ORDER-COUNT-1M)为1
IP rate limit(x-mbx-used-weight-1m)为5

        请求参数:
        Parameter         	Type    	Required	Description

        batchOrders       	list<JSON>	YES     	订单列表，最多支持5个订单
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.set_batchOrders, **to_local(locals()))


    # 批量修改订单 (TRADE)
    def alter_batchOrders(self,batchOrders:list = [],recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        PUT /fapi/v1/batchOrders

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        batchOrders       	list<JSON>	YES     	订单列表,最多支持5个订单
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.alter_batchOrders, **to_local(locals()))


    # 查询订单修改历史 (USER_DATA)
    def get_orderAmendment(self,symbol:str = '',orderId:int = '',origClientOrderId:str = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/orderAmendment

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        orderId           	LONG    	NO      	系统订单号
        origClientOrderId 	STRING  	NO      	用户自定义的订单号
        startTime         	LONG    	NO      	起始时间
        endTime           	LONG    	NO      	结束时间
        limit             	INT     	NO      	返回的结果集数量 默认值:50 最大值:100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.get_orderAmendment, **to_local(locals()))


    # 查询订单 (USER_DATA)
    def get_order(self,symbol:str = '',orderId:int = '',origClientOrderId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/order

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        orderId           	LONG    	NO      	系统订单号
        origClientOrderId 	STRING  	NO      	用户自定义的订单号
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.get_order, **to_local(locals()))


    # 撤销订单 (TRADE)
    def cancel_order(self,symbol:str = '',orderId:int = '',origClientOrderId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /fapi/v1/order

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        orderId           	LONG    	NO      	系统订单号
        origClientOrderId 	STRING  	NO      	用户自定义的订单号
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.cancel_order, **to_local(locals()))


    # 撤销全部订单 (TRADE)
    def cancel_allOpenOrders(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /fapi/v1/allOpenOrders

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.cancel_allOpenOrders, **to_local(locals()))


    # 批量撤销订单 (TRADE)
    def cancel_batchOrders(self,symbol:str = '',orderIdList:list = [],origClientOrderIdList:list = [],recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /fapi/v1/batchOrders

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        orderIdList       	LIST<LONG>	NO      	系统订单号, 最多支持10个订单比如[1234567,2345678]
        origClientOrderIdList	LIST<STRING>	NO      	用户自定义的订单号, 最多支持10个订单比如["my_id_1","my_id_2"]需要encode双引号。逗号后面没有空格。
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.cancel_batchOrders, **to_local(locals()))


    # 倒计时撤销所有订单 (TRADE)
    def set_countdownCancelAll(self,symbol:str = '',countdownTime:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /fapi/v1/countdownCancelAll

        权重:10

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        countdownTime     	LONG    	YES     	倒计时。 1000 表示 1 秒； 0 表示取消倒计时撤单功能。
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.set_countdownCancelAll, **to_local(locals()))


    # 查询当前挂单 (USER_DATA)
    def get_openOrder(self,symbol:str = '',orderId:int = '',origClientOrderId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/openOrder

        权重: 1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        orderId           	LONG    	NO      	系统订单号
        origClientOrderId 	STRING  	NO      	用户自定义的订单号
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.get_openOrder, **to_local(locals()))


    # 查看当前全部挂单 (USER_DATA)
    def get_openOrders(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/openOrders

        权重:- 带symbol1- 不带40

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	交易对
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.get_openOrders, **to_local(locals()))


    # 查询所有订单(包括历史订单) (USER_DATA)
    def get_allOrders(self,symbol:str = '',orderId:int = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/allOrders

        权重:5

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
        return self.send_request(*_UMAccountTradeEndpoints.get_allOrders, **to_local(locals()))


    # 账户余额V2 (USER_DATA)
    def get_balance(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v2/balance

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.get_balance, **to_local(locals()))


    # 账户信息V2 (USER_DATA)
    def get_account(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v2/account

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.get_account, **to_local(locals()))


    # 调整开仓杠杆 (TRADE)
    def set_leverage(self,symbol:str = '',leverage:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /fapi/v1/leverage

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        leverage          	INT     	YES     	目标杠杆倍数：1 到 125 整数
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.set_leverage, **to_local(locals()))


    # 变换逐全仓模式 (TRADE)
    def set_marginType(self,symbol:str = '',marginType:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /fapi/v1/marginType

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        marginType        	ENUM    	YES     	保证金模式 ISOLATED(逐仓), CROSSED(全仓)
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.set_marginType, **to_local(locals()))


    # 调整逐仓保证金 (TRADE)
    def set_positionMargin(self,symbol:str = '',positionSide:str = '',amount:Union[int,float] = '',type:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /fapi/v1/positionMargin

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        positionSide      	ENUM    	NO      	持仓方向，单向持仓模式下非必填，默认且仅可填BOTH;在双向持仓模式下必填,且仅可选择LONG或SHORT
        amount            	DECIMAL 	YES     	保证金资金
        type              	INT     	YES     	调整方向 1: 增加逐仓保证金，2: 减少逐仓保证金
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.set_positionMargin, **to_local(locals()))


    # 逐仓保证金变动历史 (TRADE)
    def get_positionMargin_history(self,symbol:str = '',type:int = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/positionMargin/history

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        type              	INT     	NO      	调整方向 1: 增加逐仓保证金，2: 减少逐仓保证金
        startTime         	LONG    	NO      	起始时间
        endTime           	LONG    	NO      	结束时间，默认为当前时间
        limit             	INT     	NO      	返回的结果集数量 默认值: 500
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.get_positionMargin_history, **to_local(locals()))


    # 用户持仓风险V2 (USER_DATA)
    def get_positionRisk(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v2/positionRisk

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.get_positionRisk, **to_local(locals()))


    # 账户成交历史 (USER_DATA)
    def get_userTrades(self,symbol:str = '',orderId:int = '',startTime:int = '',endTime:int = '',fromId:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/userTrades

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        orderId           	LONG    	NO      	必须要和参数symbol一起使用
        startTime         	LONG    	NO      	起始时间
        endTime           	LONG    	NO      	结束时间
        fromId            	LONG    	NO      	返回该fromId及之后的成交，缺省返回最近的成交
        limit             	INT     	NO      	返回的结果集数量 默认值:500 最大值:1000.
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.get_userTrades, **to_local(locals()))


    # 获取账户损益资金流水 (USER_DATA)
    def get_income(self,symbol:str = '',incomeType:str = '',startTime:int = '',endTime:int = '',page:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/income

        权重:30

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	交易对
        incomeType        	STRING  	NO      	收益类型： TRANSFER 转账, WELCOME_BONUS 欢迎奖金, REALIZED_PNL 已实现盈亏, FUNDING_FEE 资金费用, COMMISSION 手续费, INSURANCE_CLEAR 强平, REFERRAL_KICKBACK 推荐人返佣, COMMISSION_REBATE 被推荐人返佣, API_REBATE API佣金回扣, CONTEST_REWARD 交易大赛奖金, CROSS_COLLATERAL_TRANSFER cc转账, OPTIONS_PREMIUM_FEE 期权购置手续费, OPTIONS_SETTLE_PROFIT 期权行权收益, INTERNAL_TRANSFER 内部账户，给普通用户划转, AUTO_EXCHANGE 自动兑换, DELIVERED_SETTELMENT 下架结算, COIN_SWAP_DEPOSIT 闪兑转入, COIN_SWAP_WITHDRAW 闪兑转出, POSITION_LIMIT_INCREASE_FEE 仓位限制上调费用
        startTime         	LONG    	NO      	起始时间
        endTime           	LONG    	NO      	结束时间
        page              	INT     	NO      	分页数
        limit             	INT     	NO      	返回的结果集数量 默认值:100 最大值:1000
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.get_income, **to_local(locals()))


    # 杠杆分层标准 (USER_DATA)
    def get_leverageBracket(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/leverageBracket

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.get_leverageBracket, **to_local(locals()))


    # 持仓ADL队列估算 (USER_DATA)
    def get_adlQuantile(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/adlQuantile

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.get_adlQuantile, **to_local(locals()))


    # 用户强平单历史 (USER_DATA)
    def get_forceOrders(self,symbol:str = '',autoCloseType:str = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/forceOrders

        权重:带symbol 20, 不带symbol 50

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        autoCloseType     	ENUM    	NO      	"LIQUIDATION": 强平单, "ADL": ADL减仓单.
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	Default 50; max 100.
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.get_forceOrders, **to_local(locals()))


    # 合约交易量化规则指标 (USER_DATA)
    def get_apiTradingStatus(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/apiTradingStatus

        权重:

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.get_apiTradingStatus, **to_local(locals()))


    # 用户手续费率 (USER_DATA)
    def get_commissionRate(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/commissionRate

        权重:20

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.get_commissionRate, **to_local(locals()))


    # 获取合约资金流水下载Id (USER_DATA)
    def get_income_asyn(self,startTime:int = '',endTime:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/income/asyn

        权重:1000

        请求参数:
        Parameter         	Type    	Required	Description

        startTime         	LONG    	YES     	起始时间，ms格式时间戳
        endTime           	LONG    	YES     	结束时间，ms格式时间戳
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.get_income_asyn, **to_local(locals()))


    # 通过下载Id获取合约资金流水下载链接 (USER_DATA)
    def get_income_asyn_id(self,downloadId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/income/asyn/id

        权重:10

        请求参数:
        Parameter         	Type    	Required	Description

        downloadId        	STRING  	YES     	通过下载id 接口获取
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.get_income_asyn_id, **to_local(locals()))


    # 获取合约订单历史下载Id (USER_DATA)
    def get_order_asyn(self,startTime:int = '',endTime:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/order/asyn

        权重:1000

        请求参数:
        Parameter         	Type    	Required	Description

        startTime         	LONG    	YES     	起始时间，ms格式时间戳
        endTime           	LONG    	YES     	结束时间，ms格式时间戳
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.get_order_asyn, **to_local(locals()))


    # 通过下载Id获取合约订单下载链接 (USER_DATA)
    def get_order_asyn_id(self,downloadId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/order/asyn/id

        权重:10

        请求参数:
        Parameter         	Type    	Required	Description

        downloadId        	STRING  	YES     	通过下载id 接口获取
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.get_order_asyn_id, **to_local(locals()))


    # 获取合约交易历史下载Id (USER_DATA)
    def get_trade_asyn(self,startTime:int = '',endTime:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/trade/asyn

        权重:1000

        请求参数:
        Parameter         	Type    	Required	Description

        startTime         	LONG    	YES     	起始时间，ms格式时间戳
        endTime           	LONG    	YES     	结束时间，ms格式时间戳
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.get_trade_asyn, **to_local(locals()))


    # 通过下载Id获取合约交易历史下载链接 (USER_DATA)
    def get_trade_asyn_id(self,downloadId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /fapi/v1/trade/asyn/id

        权重:10

        请求参数:
        Parameter         	Type    	Required	Description

        downloadId        	STRING  	YES     	通过下载id 接口获取
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_UMAccountTradeEndpoints.get_trade_asyn_id, **to_local(locals()))