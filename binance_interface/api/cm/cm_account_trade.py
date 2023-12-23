# 账户和交易接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _CMAccountTradeEndpoints():


    set_positionSide_dual = ['https://dapi.binance.com', 'POST', '/dapi/v1/positionSide/dual', True] # 更改持仓模式(TRADE) 
    get_positionSide_dual = ['https://dapi.binance.com', 'GET', '/dapi/v1/positionSide/dual', True] # 查询持仓模式(USER_DATA) 
    set_order = ['https://dapi.binance.com', 'POST', '/dapi/v1/order', True] # 下单 (TRADE) 
    set_order_test = ['https://dapi.binance.com', 'POST', '/dapi/v1/order/test', True] # 测试下单接口 (TRADE)
    alter_order = ['https://dapi.binance.com', 'PUT', '/dapi/v1/order', True] # 修改订单 (TRADE) 
    set_batchOrders = ['https://dapi.binance.com', 'POST', '/dapi/v1/batchOrders', True] # 批量下单 (TRADE) 
    alter_batchOrders = ['https://dapi.binance.com', 'PUT', '/dapi/v1/batchOrders', True] # 批量修改订单 (TRADE) 
    get_orderAmendment = ['https://dapi.binance.com', 'GET', '/dapi/v1/orderAmendment', True] # 查询订单修改历史 (USER_DATA) 
    get_order = ['https://dapi.binance.com', 'GET', '/dapi/v1/order', True] # 查询订单 (USER_DATA) 
    cancel_order = ['https://dapi.binance.com', 'DELETE', '/dapi/v1/order', True] # 撤销订单 (TRADE) 
    cancel_allOpenOrders = ['https://dapi.binance.com', 'DELETE', '/dapi/v1/allOpenOrders', True] # 撤销全部订单 (TRADE) 
    cancel_batchOrders = ['https://dapi.binance.com', 'DELETE', '/dapi/v1/batchOrders', True] # 批量撤销订单 (TRADE) 
    set_countdownCancelAll = ['https://dapi.binance.com', 'POST', '/dapi/v1/countdownCancelAll', True] # 倒计时撤销所有订单 (TRADE) 
    get_openOrder = ['https://dapi.binance.com', 'GET', '/dapi/v1/openOrder', True] # 查询当前挂单 (USER_DATA) 
    get_openOrders = ['https://dapi.binance.com', 'GET', '/dapi/v1/openOrders', True] # 查看当前全部挂单 (USER_DATA) 
    get_allOrders = ['https://dapi.binance.com', 'GET', '/dapi/v1/allOrders', True] # 查询所有订单(包括历史订单) (USER_DATA) 
    get_balance = ['https://dapi.binance.com', 'GET', '/dapi/v1/balance', True] # 账户余额 (USER_DATA) 
    get_account = ['https://dapi.binance.com', 'GET', '/dapi/v1/account', True] # 账户信息 (USER_DATA) 
    set_leverage = ['https://dapi.binance.com', 'POST', '/dapi/v1/leverage', True] # 调整开仓杠杆 (TRADE) 
    set_marginType = ['https://dapi.binance.com', 'POST', '/dapi/v1/marginType', True] # 变换逐全仓模式 (TRADE) 
    set_positionMargin = ['https://dapi.binance.com', 'POST', '/dapi/v1/positionMargin', True] # 调整逐仓保证金 (TRADE) 
    get_positionMargin_history = ['https://dapi.binance.com', 'GET', '/dapi/v1/positionMargin/history', True] # 逐仓保证金变动历史 (TRADE) 
    get_positionRisk = ['https://dapi.binance.com', 'GET', '/dapi/v1/positionRisk', False] # 用户持仓风险
    get_userTrades = ['https://dapi.binance.com', 'GET', '/dapi/v1/userTrades', True] # 账户成交历史 (USER_DATA) 
    get_income = ['https://dapi.binance.com', 'GET', '/dapi/v1/income', True] # 获取账户损益资金流水(USER_DATA) 
    get_leverageBracket_by_pair = ['https://dapi.binance.com', 'GET', '/dapi/v2/leverageBracket', True] # 标的交易对默认杠杆分层标准 (USER_DATA)
    get_leverageBracket_by_symbol = ['https://dapi.binance.com', 'GET', '/dapi/v2/leverageBracket', True] # 交易对杠杆分层标准 (USER_DATA)
    get_forceOrders = ['https://dapi.binance.com', 'GET', '/dapi/v1/forceOrders', True] # 用户强平单历史 (USER_DATA) 
    get_adlQuantile = ['https://dapi.binance.com', 'GET', '/dapi/v1/adlQuantile', True] # 持仓ADL队列估算 (USER_DATA) 
    get_commissionRate = ['https://dapi.binance.com', 'GET', '/dapi/v1/commissionRate', True] # 用户手续费率 (USER_DATA) 
    get_income_asyn = ['https://dapi.binance.com', 'GET', '/dapi/v1/income/asyn', True] # 获取合约资金流水下载Id (USER_DATA) 
    get_income_asyn_id = ['https://dapi.binance.com', 'GET', '/dapi/v1/income/asyn/id', True] # 通过下载Id获取合约资金流水下载链接 (USER_DATA)  


class CMAccountTrade(Client):

    # 更改持仓模式(TRADE)
    def set_positionSide_dual(self,dualSidePosition:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /dapi/v1/positionSide/dual

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        dualSidePosition  	STRING  	YES     	"true": 双向持仓模式；"false": 单向持仓模式
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.set_positionSide_dual, **to_local(locals()))


    # 查询持仓模式(USER_DATA)
    def get_positionSide_dual(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /dapi/v1/positionSide/dual

        权重:30

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.get_positionSide_dual, **to_local(locals()))


    # 下单 (TRADE)
    def set_order(self,symbol:str = '',side:str = '',positionSide:str = '',type:str = '',reduceOnly:str = '',quantity:Union[int,float] = '',price:Union[int,float] = '',newClientOrderId:str = '',stopPrice:Union[int,float] = '',closePosition:str = '',activationPrice:Union[int,float] = '',callbackRate:Union[int,float] = '',timeInForce:str = '',workingType:str = '',priceProtect:str = '',newOrderRespType:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /dapi/v1/order

        权重:0

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        side              	ENUM    	YES     	买卖方向SELL,BUY
        positionSide      	ENUM    	NO      	持仓方向,单向持仓模式下非必填,默认且仅可填BOTH;在双向持仓模式下必填,且仅可选择LONG或SHORT
        type              	ENUM    	YES     	订单类型LIMIT,MARKET,STOP,TAKE_PROFIT,STOP_MARKET,TAKE_PROFIT_MARKET,TRAILING_STOP_MARKET
        reduceOnly        	STRING  	NO      	true,false; 非双开模式下默认false；双开模式下不接受此参数； 使用closePosition不支持此参数。
        quantity          	DECIMAL 	NO      	以合约数量计量的下单数量，使用closePosition不支持此参数。
        price             	DECIMAL 	NO      	委托价格
        newClientOrderId  	STRING  	NO      	用户自定义的订单号,不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则^[\.A-Z\:/a-z0-9_-]{1,36}$
        stopPrice         	DECIMAL 	NO      	触发价, 仅STOP,STOP_MARKET,TAKE_PROFIT,TAKE_PROFIT_MARKET需要此参数
        closePosition     	STRING  	NO      	true,false；触发后全部平仓,仅支持STOP_MARKET和TAKE_PROFIT_MARKET；不与quantity合用；自带只平仓效果,不与reduceOnly合用
        activationPrice   	DECIMAL 	NO      	追踪止损激活价格,仅TRAILING_STOP_MARKET需要此参数, 默认为下单当前市场价格(支持不同workingType)
        callbackRate      	DECIMAL 	NO      	追踪止损回调比例,可取值范围[0.1, 4],其中 1代表1% ,仅TRAILING_STOP_MARKET需要此参数
        timeInForce       	ENUM    	NO      	有效方法
        workingType       	ENUM    	NO      	stopPrice 触发类型:MARK_PRICE(标记价格),CONTRACT_PRICE(合约最新价). 默认CONTRACT_PRICE
        priceProtect      	STRING  	NO      	条件单触发保护："TRUE","FALSE", 默认"FALSE". 仅STOP,STOP_MARKET,TAKE_PROFIT,TAKE_PROFIT_MARKET需要此参数
        newOrderRespType  	ENUM    	NO      	"ACK", "RESULT", 默认 "ACK"
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.set_order, **to_local(locals()))


    # 测试下单接口 (TRADE)
    def set_order_test(self,symbol:str = '',side:str = '',positionSide:str = '',type:str = '',reduceOnly:str = '',quantity:Union[int,float] = '',price:Union[int,float] = '',newClientOrderId:str = '',stopPrice:Union[int,float] = '',closePosition:str = '',activationPrice:Union[int,float] = '',callbackRate:Union[int,float] = '',timeInForce:str = '',workingType:str = '',priceProtect:str = '',newOrderRespType:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /dapi/v1/order/test

        权重:0

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        side              	ENUM    	YES     	买卖方向SELL,BUY
        positionSide      	ENUM    	NO      	持仓方向,单向持仓模式下非必填,默认且仅可填BOTH;在双向持仓模式下必填,且仅可选择LONG或SHORT
        type              	ENUM    	YES     	订单类型LIMIT,MARKET,STOP,TAKE_PROFIT,STOP_MARKET,TAKE_PROFIT_MARKET,TRAILING_STOP_MARKET
        reduceOnly        	STRING  	NO      	true,false; 非双开模式下默认false；双开模式下不接受此参数； 使用closePosition不支持此参数。
        quantity          	DECIMAL 	NO      	以合约数量计量的下单数量，使用closePosition不支持此参数。
        price             	DECIMAL 	NO      	委托价格
        newClientOrderId  	STRING  	NO      	用户自定义的订单号,不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则^[\.A-Z\:/a-z0-9_-]{1,36}$
        stopPrice         	DECIMAL 	NO      	触发价, 仅STOP,STOP_MARKET,TAKE_PROFIT,TAKE_PROFIT_MARKET需要此参数
        closePosition     	STRING  	NO      	true,false；触发后全部平仓,仅支持STOP_MARKET和TAKE_PROFIT_MARKET；不与quantity合用；自带只平仓效果,不与reduceOnly合用
        activationPrice   	DECIMAL 	NO      	追踪止损激活价格,仅TRAILING_STOP_MARKET需要此参数, 默认为下单当前市场价格(支持不同workingType)
        callbackRate      	DECIMAL 	NO      	追踪止损回调比例,可取值范围[0.1, 4],其中 1代表1% ,仅TRAILING_STOP_MARKET需要此参数
        timeInForce       	ENUM    	NO      	有效方法
        workingType       	ENUM    	NO      	stopPrice 触发类型:MARK_PRICE(标记价格),CONTRACT_PRICE(合约最新价). 默认CONTRACT_PRICE
        priceProtect      	STRING  	NO      	条件单触发保护："TRUE","FALSE", 默认"FALSE". 仅STOP,STOP_MARKET,TAKE_PROFIT,TAKE_PROFIT_MARKET需要此参数
        newOrderRespType  	ENUM    	NO      	"ACK", "RESULT", 默认 "ACK"
        recvWindow        	LONG    	NO
        timestamp         	LONG    	YES
        '''

        return self.send_request(*_CMAccountTradeEndpoints.set_order_test, **to_local(locals()))


    # 修改订单 (TRADE)
    def alter_order(self,orderId:int = '',origClientOrderId:str = '',symbol:str = '',side:str = '',quantity:Union[int,float] = '',price:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        PUT /dapi/v1/order

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        orderId           	LONG    	NO      	系统订单号
        origClientOrderId 	STRING  	NO      	用户自定义的订单号
        symbol            	STRING  	YES     	交易对
        side              	ENUM    	YES     	买卖方向SELL,BUY
        quantity          	DECIMAL 	NO      	下单数量,使用closePosition不支持此参数。
        price             	DECIMAL 	NO      	委托价格
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.alter_order, **to_local(locals()))


    # 批量下单 (TRADE)
    def set_batchOrders(self,batchOrders:list = [],recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /dapi/v1/batchOrders

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        batchOrders       	list<JSON>	YES     	订单列表,最多支持5个订单
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.set_batchOrders, **to_local(locals()))


    # 批量修改订单 (TRADE)
    def alter_batchOrders(self,batchOrders:list = [],recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        PUT /dapi/v1/batchOrders

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        batchOrders       	list<JSON>	YES     	订单列表,最多支持5个订单
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.alter_batchOrders, **to_local(locals()))


    # 查询订单修改历史 (USER_DATA)
    def get_orderAmendment(self,symbol:str = '',orderId:int = '',origClientOrderId:str = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /dapi/v1/orderAmendment

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
        return self.send_request(*_CMAccountTradeEndpoints.get_orderAmendment, **to_local(locals()))


    # 查询订单 (USER_DATA)
    def get_order(self,symbol:str = '',orderId:int = '',origClientOrderId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /dapi/v1/order

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        orderId           	LONG    	NO      	系统订单号
        origClientOrderId 	STRING  	NO      	用户自定义的订单号
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.get_order, **to_local(locals()))


    # 撤销订单 (TRADE)
    def cancel_order(self,symbol:str = '',orderId:int = '',origClientOrderId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /dapi/v1/order

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        orderId           	LONG    	NO      	系统订单号
        origClientOrderId 	STRING  	NO      	用户自定义的订单号
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.cancel_order, **to_local(locals()))


    # 撤销全部订单 (TRADE)
    def cancel_allOpenOrders(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /dapi/v1/allOpenOrders

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.cancel_allOpenOrders, **to_local(locals()))


    # 批量撤销订单 (TRADE)
    def cancel_batchOrders(self,symbol:str = '',orderIdList:list = [],origClientOrderIdList:list = [],recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /dapi/v1/batchOrders

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        orderIdList       	LIST<LONG>	NO      	系统订单号, 最多支持10个订单比如[1234567,2345678]
        origClientOrderIdList	LIST<STRING>	NO      	用户自定义的订单号, 最多支持10个订单比如["my_id_1","my_id_2"]需要encode双引号。逗号后面没有空格。
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.cancel_batchOrders, **to_local(locals()))


    # 倒计时撤销所有订单 (TRADE)
    def set_countdownCancelAll(self,symbol:str = '',countdownTime:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /dapi/v1/countdownCancelAll

        权重:10

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        countdownTime     	LONG    	YES     	倒计时。 1000 表示 1 秒； 0 表示取消倒计时撤单功能。
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.set_countdownCancelAll, **to_local(locals()))


    # 查询当前挂单 (USER_DATA)
    def get_openOrder(self,symbol:str = '',orderId:int = '',origClientOrderId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /dapi/v1/openOrder

        权重: 1*

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        orderId           	LONG    	NO      	系统订单号
        origClientOrderId 	STRING  	NO      	用户自定义的订单号
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.get_openOrder, **to_local(locals()))


    # 查看当前全部挂单 (USER_DATA)
    def get_openOrders(self,symbol:str = '',pair:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /dapi/v1/openOrders

        权重:

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	交易对
        pair              	STRING  	NO      	标的交易对
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.get_openOrders, **to_local(locals()))


    # 查询所有订单(包括历史订单) (USER_DATA)
    def get_allOrders(self,symbol:str = '',pair:str = '',orderId:int = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /dapi/v1/allOrders

        权重:传symbol20传pairs40

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	交易对
        pair              	STRING  	NO      	标的交易对
        orderId           	LONG    	NO      	只返回此orderID及之后的订单,缺省返回最近的订单, 仅支持配合symbol使用
        startTime         	LONG    	NO      	起始时间
        endTime           	LONG    	NO      	结束时间
        limit             	INT     	NO      	返回的结果集数量 默认值:50 最大值:100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.get_allOrders, **to_local(locals()))


    # 账户余额 (USER_DATA)
    def get_balance(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /dapi/v1/balance

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.get_balance, **to_local(locals()))


    # 账户信息 (USER_DATA)
    def get_account(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /dapi/v1/account

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.get_account, **to_local(locals()))


    # 调整开仓杠杆 (TRADE)
    def set_leverage(self,symbol:str = '',leverage:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /dapi/v1/leverage

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        leverage          	INT     	YES     	目标杠杆倍数
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.set_leverage, **to_local(locals()))


    # 变换逐全仓模式 (TRADE)
    def set_marginType(self,symbol:str = '',marginType:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /dapi/v1/marginType

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        marginType        	ENUM    	YES     	保证金模式 ISOLATED(逐仓), CROSSED(全仓)
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.set_marginType, **to_local(locals()))


    # 调整逐仓保证金 (TRADE)
    def set_positionMargin(self,symbol:str = '',positionSide:str = '',amount:Union[int,float] = '',type:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /dapi/v1/positionMargin

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        positionSide      	ENUM    	NO      	持仓方向,单向持仓模式下非必填,默认且仅可填BOTH;在双向持仓模式下必填,且仅可选择LONG或SHORT
        amount            	DECIMAL 	YES     	保证金资金
        type              	INT     	YES     	调整方向 1: 增加逐仓保证金,2: 减少逐仓保证金
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.set_positionMargin, **to_local(locals()))


    # 逐仓保证金变动历史 (TRADE)
    def get_positionMargin_history(self,symbol:str = '',type:int = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /dapi/v1/positionMargin/history

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        type              	INT     	NO      	调整方向 1: 增加逐仓保证金,2: 减少逐仓保证金
        startTime         	LONG    	NO      	起始时间
        endTime           	LONG    	NO      	结束时间
        limit             	INT     	NO      	返回的结果集数量 默认值: 50
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.get_positionMargin_history, **to_local(locals()))


    # 用户持仓风险
    def get_positionRisk(self,marginAsset:str = '',pair:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /dapi/v1/positionRisk

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        marginAsset       	STRING  	NO      	
        pair              	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.get_positionRisk, **to_local(locals()))


    # 账户成交历史 (USER_DATA)
    def get_userTrades(self,symbol:str = '',pair:str = '',orderId:str = '',startTime:int = '',endTime:int = '',fromId:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /dapi/v1/userTrades

        权重:

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	交易对
        pair              	STRING  	NO      	标的交易对
        orderId           	STRING  	NO      	订单号
        startTime         	LONG    	NO      	起始时间
        endTime           	LONG    	NO      	结束时间
        fromId            	LONG    	NO      	返回该fromId及之后的成交,缺省返回最近的成交,仅支持配合symbol使用
        limit             	INT     	NO      	返回的结果集数量 默认值:50 最大值:1000
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.get_userTrades, **to_local(locals()))


    # 获取账户损益资金流水(USER_DATA)
    def get_income(self,symbol:str = '',incomeType:str = '',startTime:int = '',endTime:int = '',page:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /dapi/v1/income

        权重:20

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	交易对
        incomeType        	STRING  	NO      	收益类型 "TRANSFER","WELCOME_BONUS", "FUNDING_FEE", "REALIZED_PNL", "COMMISSION", "INSURANCE_CLEAR", "API_REBATE", "DELIVERED_SETTELMENT"
        startTime         	LONG    	NO      	起始时间
        endTime           	LONG    	NO      	结束时间
        page              	INT     	NO      	分页数
        limit             	INT     	NO      	返回的结果集数量 默认值:100 最大值:1000
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.get_income, **to_local(locals()))


    # 标的交易对默认杠杆分层标准 (USER_DATA)
    def get_leverageBracket_by_pair(self,pair:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /dapi/v2/leverageBracket

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        pair              	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.get_leverageBracket_by_pair, **to_local(locals()))


    # 交易对杠杆分层标准 (USER_DATA)
    def get_leverageBracket_by_symbol(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /dapi/v2/leverageBracket

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.get_leverageBracket_by_symbol, **to_local(locals()))


    # 用户强平单历史 (USER_DATA)
    def get_forceOrders(self,symbol:str = '',autoCloseType:str = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /dapi/v1/forceOrders

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
        return self.send_request(*_CMAccountTradeEndpoints.get_forceOrders, **to_local(locals()))


    # 持仓ADL队列估算 (USER_DATA)
    def get_adlQuantile(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /dapi/v1/adlQuantile

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.get_adlQuantile, **to_local(locals()))


    # 用户手续费率 (USER_DATA)
    def get_commissionRate(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /dapi/v1/commissionRate

        权重:20

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.get_commissionRate, **to_local(locals()))


    # 获取合约资金流水下载Id (USER_DATA)
    def get_income_asyn(self,startTime:int = '',endTime:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /dapi/v1/income/asyn

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        startTime         	LONG    	YES     	起始时间，ms格式时间戳
        endTime           	LONG    	YES     	结束时间，ms格式时间戳
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.get_income_asyn, **to_local(locals()))


    # 通过下载Id获取合约资金流水下载链接 (USER_DATA)
    def get_income_asyn_id(self,downloadId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /dapi/v1/income/asyn/id

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        downloadId        	STRING  	YES     	通过下载id 接口获取
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CMAccountTradeEndpoints.get_income_asyn_id, **to_local(locals()))