# 杠杆账户和交易接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _MarginAccountTradeEndpoints():


    set_margin_transfer = ['https://api.binance.com', 'POST', '/sapi/v1/margin/transfer', True] # 全仓杠杆账户划转 (MARGIN) 
    set_margin_loan = ['https://api.binance.com', 'POST', '/sapi/v1/margin/loan', True] # 杠杆账户借贷 (MARGIN) 
    set_margin_repay = ['https://api.binance.com', 'POST', '/sapi/v1/margin/repay', True] # 杠杆账户归还借贷 (MARGIN) 
    get_margin_asset = ['https://api.binance.com', 'GET', '/sapi/v1/margin/asset', False] # 查询杠杆资产 (MARKET_DATA) 
    get_margin_pair = ['https://api.binance.com', 'GET', '/sapi/v1/margin/pair', False] # 查询全仓杠杆交易对 (MARKET_DATA) 
    get_margin_allAssets = ['https://api.binance.com', 'GET', '/sapi/v1/margin/allAssets', False] # 获取所有杠杆资产信息 (MARKET_DATA)
    get_margin_allPairs = ['https://api.binance.com', 'GET', '/sapi/v1/margin/allPairs', False] # 获取所有全仓杠杆交易对(MARKET_DATA)
    get_margin_priceIndex = ['https://api.binance.com', 'GET', '/sapi/v1/margin/priceIndex', False] # 查询杠杆价格指数 (MARKET_DATA) 
    set_margin_order = ['https://api.binance.com', 'POST', '/sapi/v1/margin/order', True] # 杠杆账户下单 (TRADE) 
    cancel_margin_order = ['https://api.binance.com', 'DELETE', '/sapi/v1/margin/order', True] # 杠杆账户撤销订单 (TRADE) 
    cancel_margin_openOrders = ['https://api.binance.com', 'DELETE', '/sapi/v1/margin/openOrders', True] # 杠杆账户撤销单一交易对的所有挂单 (TRADE) 
    set_margin_max_leverage = ['https://api.binance.com', 'POST', '/sapi/v1/margin/max-leverage', True] # 调整全仓最大杠杆 (USER_DATA) 
    get_margin_transfer = ['https://api.binance.com', 'GET', '/sapi/v1/margin/transfer', True] # 获取全仓杠杆划转历史 (USER_DATA) 
    get_margin_loan = ['https://api.binance.com', 'GET', '/sapi/v1/margin/loan', True] # 查询借贷记录 (USER_DATA) 
    get_margin_repay = ['https://api.binance.com', 'GET', '/sapi/v1/margin/repay', True] # 查询还贷记录 (USER_DATA) 
    get_margin_interestHistory = ['https://api.binance.com', 'GET', '/sapi/v1/margin/interestHistory', True] # 获取利息历史 (USER_DATA) 
    get_margin_forceLiquidationRec = ['https://api.binance.com', 'GET', '/sapi/v1/margin/forceLiquidationRec', True] # 获取账户强制平仓记录(USER_DATA) 
    get_margin_account = ['https://api.binance.com', 'GET', '/sapi/v1/margin/account', True] # 查询全仓杠杆账户详情 (USER_DATA) 
    get_margin_order = ['https://api.binance.com', 'GET', '/sapi/v1/margin/order', True] # 查询杠杆账户订单 (USER_DATA) 
    get_margin_openOrders = ['https://api.binance.com', 'GET', '/sapi/v1/margin/openOrders', True] # 查询杠杆账户挂单记录 (USER_DATA) 
    get_margin_allOrders = ['https://api.binance.com', 'GET', '/sapi/v1/margin/allOrders', True] # 查询杠杆账户的所有订单 (USER_DATA) 
    set_margin_order_oco = ['https://api.binance.com', 'POST', '/sapi/v1/margin/order/oco', True] # 杠杆账户 OCO 下单(TRADE) 
    cancel_margin_orderList = ['https://api.binance.com', 'DELETE', '/sapi/v1/margin/orderList', True] # 取消杠杆账户 OCO 订单(TRADE) 
    get_margin_orderList = ['https://api.binance.com', 'GET', '/sapi/v1/margin/orderList', True] # 查询杠杆账户 OCO (USER_DATA) 
    get_margin_allOrderList = ['https://api.binance.com', 'GET', '/sapi/v1/margin/allOrderList', True] # 查询特定杠杆账户所有 OCO (USER_DATA) 
    get_margin_openOrderList = ['https://api.binance.com', 'GET', '/sapi/v1/margin/openOrderList', True] # 查询杠杆账户 OCO 挂单 (USER_DATA) 
    get_margin_myTrades = ['https://api.binance.com', 'GET', '/sapi/v1/margin/myTrades', True] # 查询杠杆账户交易历史 (USER_DATA) 
    get_margin_maxBorrowable = ['https://api.binance.com', 'GET', '/sapi/v1/margin/maxBorrowable', True] # 查询账户最大可借贷额度(USER_DATA) 
    get_margin_maxTransferable = ['https://api.binance.com', 'GET', '/sapi/v1/margin/maxTransferable', True] # 查询最大可转出额 (USER_DATA) 
    get_margin_tradeCoeff = ['https://api.binance.com', 'GET', '/sapi/v1/margin/tradeCoeff', True] # 查询Margin账户信息汇总 (USER_DATA) 
    set_margin_isolated_transfer = ['https://api.binance.com', 'POST', '/sapi/v1/margin/isolated/transfer', True] # 杠杆逐仓账户划转 (MARGIN) 
    get_margin_isolated_transfer = ['https://api.binance.com', 'GET', '/sapi/v1/margin/isolated/transfer', True] # 获取杠杆逐仓划转历史 (USER_DATA) 
    get_margin_isolated_account = ['https://api.binance.com', 'GET', '/sapi/v1/margin/isolated/account', True] # 查询杠杆逐仓账户信息 (USER_DATA) 
    cancel_margin_isolated_account = ['https://api.binance.com', 'DELETE', '/sapi/v1/margin/isolated/account', True] # 杠杆逐仓账户停用 (TRADE) 
    set_margin_isolated_account = ['https://api.binance.com', 'POST', '/sapi/v1/margin/isolated/account', True] # 杠杆逐仓账户启用 (TRADE) 
    get_margin_isolated_accountLimit = ['https://api.binance.com', 'GET', '/sapi/v1/margin/isolated/accountLimit', True] # 查询杠杆逐仓账户启用限制 (USER_DATA) 
    get_margin_isolated_pair = ['https://api.binance.com', 'GET', '/sapi/v1/margin/isolated/pair', True] # 查询逐仓杠杆交易对 (USER_DATA) 
    get_margin_isolated_allPairs = ['https://api.binance.com', 'GET', '/sapi/v1/margin/isolated/allPairs', True] # 获取所有逐仓杠杆交易对(USER_DATA) 
    set_bnbBurn = ['https://api.binance.com', 'POST', '/sapi/v1/bnbBurn', True] # 现货交易和杠杆利息BNB抵扣开关(USER_DATA) 
    get_bnbBurn = ['https://api.binance.com', 'GET', '/sapi/v1/bnbBurn', True] # 获取BNB抵扣开关状态 (USER_DATA) 
    get_margin_interestRateHistory = ['https://api.binance.com', 'GET', '/sapi/v1/margin/interestRateHistory', True] # 获取杠杆利率历史 (USER_DATA) 
    get_margin_crossMarginData = ['https://api.binance.com', 'GET', '/sapi/v1/margin/crossMarginData', True] # 获取全仓杠杆利率及限额 (USER_DATA) 
    get_margin_isolatedMarginData = ['https://api.binance.com', 'GET', '/sapi/v1/margin/isolatedMarginData', True] # 获取逐仓杠杆利率及限额 (USER_DATA) 
    get_margin_isolatedMarginTier = ['https://api.binance.com', 'GET', '/sapi/v1/margin/isolatedMarginTier', True] # 获取逐仓档位信息 (USER_DATA) 
    get_margin_rateLimit_order = ['https://api.binance.com', 'GET', '/sapi/v1/margin/rateLimit/order', True] # 查询目前杠杆账户下单数 (TRADE) 
    get_margin_dribblet = ['https://api.binance.com', 'GET', '/sapi/v1/margin/dribblet', True] # 杠杆小额资产转换BNB历史 (USER_DATA) 
    get_margin_dust = ['https://api.binance.com', 'GET', '/sapi/v1/margin/dust', True] # 获取可以转换成BNB的小额资产 (USER_DATA) 
    set_margin_dust = ['https://api.binance.com', 'POST', '/sapi/v1/margin/dust', True] # 杠杆小额资产转换 (TRADE) 
    get_margin_crossMarginCollateralRatio = ['https://api.binance.com', 'GET', '/sapi/v1/margin/crossMarginCollateralRatio', False] # 全仓币种质押率 (MARKET_DATA)
    get_margin_exchange_small_liability = ['https://api.binance.com', 'GET', '/sapi/v1/margin/exchange-small-liability', True] # 查询可小额负债转换的资产 (USER_DATA) 
    set_margin_exchange_small_liability = ['https://api.binance.com', 'POST', '/sapi/v1/margin/exchange-small-liability', True] # 全仓杠杆小额负债转换 (MARGIN) 
    get_margin_exchange_small_liability_history = ['https://api.binance.com', 'GET', '/sapi/v1/margin/exchange-small-liability-history', True] # 查询全仓杠杆小额负债转换历史  (USER_DATA) 
    get_margin_next_hourly_interest_rate = ['https://api.binance.com', 'GET', '/sapi/v1/margin/next-hourly-interest-rate', True] # 查询下小时预估利率 (USER_DATA) 
    get_margin_capital_flow = ['https://api.binance.com', 'GET', '/sapi/v1/margin/capital-flow', True] # 查询全仓/逐仓资金流水(USER_DATA) 
    get_margin_delist_schedule = ['https://api.binance.com', 'GET', '/sapi/v1/margin/delist-schedule', False] # 查询全仓和逐仓的币种或币对的下架计划 (MARKET_DATA) 
    get_margin_available_inventory = ['https://api.binance.com', 'GET', '/sapi/v1/margin/available-inventory', True] # 杠杆可用放贷库存查询(USER_DATA) 
    set_margin_manual_liquidation = ['https://api.binance.com', 'POST', '/sapi/v1/margin/manual-liquidation', True] # 杠杆手动强平(MARGIN) 
    get_margin_leverageBracket = ['https://api.binance.com', 'GET', '/sapi/v1/margin/leverageBracket', False] # 查询全仓杠杆Pro模式下的负债币种杠杆与保证金率(MARKET_DATA) 


class MarginAccountTrade(Client):

    # 全仓杠杆账户划转 (MARGIN)
    def set_margin_transfer(self,asset:str = '',amount:Union[int,float] = '',type:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/margin/transfer

        权重(UID):600

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	YES     	被划转的资产, 比如, BTC
        amount            	DECIMAL 	YES     	划转数量
        type              	INT     	YES     	1: 主账户向全仓杠杆账户划转 2: 全仓杠杆账户向主账户划转
        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.set_margin_transfer, **to_local(locals()))


    # 杠杆账户借贷 (MARGIN)
    def set_margin_loan(self,asset:str = '',isIsolated:str = '',symbol:str = '',amount:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/margin/loan

        权重(UID):3000

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	YES     	
        isIsolated        	STRING  	NO      	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        symbol            	STRING  	NO      	逐仓交易对，配合逐仓使用
        amount            	DECIMAL 	YES     	
        recvWindow        	LONG    	NO      	赋值不能超过60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.set_margin_loan, **to_local(locals()))


    # 杠杆账户归还借贷 (MARGIN)
    def set_margin_repay(self,asset:str = '',isIsolated:str = '',symbol:str = '',amount:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/margin/repay

        权重(UID):3000

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	YES     	
        isIsolated        	STRING  	NO      	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        symbol            	STRING  	NO      	逐仓交易对，配合逐仓使用
        amount            	DECIMAL 	YES     	
        recvWindow        	LONG    	NO      	赋值不能超过60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.set_margin_repay, **to_local(locals()))


    # 查询杠杆资产 (MARKET_DATA)
    def get_margin_asset(self,asset:str = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/asset

        权重(IP):10

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_asset, **to_local(locals()))


    # 查询全仓杠杆交易对 (MARKET_DATA)
    def get_margin_pair(self,symbol:str = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/pair

        权重(IP):10

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_pair, **to_local(locals()))


    # 获取所有杠杆资产信息 (MARKET_DATA)
    def get_margin_allAssets(self,proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/allAssets

        权重(IP):1
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_allAssets, **to_local(locals()))


    # 获取所有全仓杠杆交易对(MARKET_DATA)
    def get_margin_allPairs(self,proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/allPairs

        权重(IP):1
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_allPairs, **to_local(locals()))


    # 查询杠杆价格指数 (MARKET_DATA)
    def get_margin_priceIndex(self,symbol:str = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/priceIndex

        权重(IP):10

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_priceIndex, **to_local(locals()))


    # 杠杆账户下单 (TRADE)
    def set_margin_order(self,symbol:str = '',isIsolated:str = '',side:str = '',type:str = '',quantity:Union[int,float] = '',quoteOrderQty:Union[int,float] = '',price:Union[int,float] = '',stopPrice:Union[int,float] = '',newClientOrderId:str = '',icebergQty:Union[int,float] = '',newOrderRespType:str = '',sideEffectType:str = '',timeInForce:str = '',selfTradePreventionMode:str = '',autoRepayAtCancel:bool = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/margin/order

        权重(UID):6

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        isIsolated        	STRING  	NO      	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        side              	ENUM    	YES     	BUYSELL
        type              	ENUM    	YES     	详见枚举定义：订单类型
        quantity          	DECIMAL 	NO      	
        quoteOrderQty     	DECIMAL 	NO      	
        price             	DECIMAL 	NO      	
        stopPrice         	DECIMAL 	NO      	与STOP_LOSS,STOP_LOSS_LIMIT,TAKE_PROFIT, 和TAKE_PROFIT_LIMIT订单一起使用.
        newClientOrderId  	STRING  	NO      	客户自定义的唯一订单ID。若未发送自动生成。
        icebergQty        	DECIMAL 	NO      	与LIMIT,STOP_LOSS_LIMIT, 和TAKE_PROFIT_LIMIT一起使用创建 iceberg 订单.
        newOrderRespType  	ENUM    	NO      	设置响应: JSON. ACK, RESULT, 或 FULL; MARKET 和 LIMIT 订单类型默认为 FULL, 所有其他订单默认为 ACK.
        sideEffectType    	ENUM    	NO      	NO_SIDE_EFFECT, MARGIN_BUY, AUTO_REPAY,AUTO_BORROW_REPAY;默认为 NO_SIDE_EFFECT.
        timeInForce       	ENUM    	NO      	GTC,IOC,FOK
        selfTradePreventionMode	ENUM    	NO      	允许的 ENUM 取决于交易对的配置。支持的值有 EXPIRE_TAKER，EXPIRE_MAKER，EXPIRE_BOTH，NONE
        autoRepayAtCancel 	BOOLEAN 	NO      	只有在自动借款单或者自动借还单生效，true表示的是撤单后需要把订单产生的借款归还，默认为true
        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.set_margin_order, **to_local(locals()))


    # 杠杆账户撤销订单 (TRADE)
    def cancel_margin_order(self,symbol:str = '',isIsolated:str = '',orderId:int = '',origClientOrderId:str = '',newClientOrderId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /sapi/v1/margin/order

        权重(IP):10

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        isIsolated        	STRING  	NO      	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        orderId           	LONG    	NO      	
        origClientOrderId 	STRING  	NO      	
        newClientOrderId  	STRING  	NO      	用于唯一识别此撤销订单，默认自动生成。
        recvWindow        	LONG    	NO      	T赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.cancel_margin_order, **to_local(locals()))


    # 杠杆账户撤销单一交易对的所有挂单 (TRADE)
    def cancel_margin_openOrders(self,symbol:str = '',isIsolated:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /sapi/v1/margin/openOrders

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        isIsolated        	STRING  	NO      	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.cancel_margin_openOrders, **to_local(locals()))


    # 调整全仓最大杠杆 (USER_DATA)
    def set_margin_max_leverage(self,maxLeverage:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/margin/max-leverage

        权重(UID):3000

        请求参数:
        Parameter         	Type    	Required	Description

        maxLeverage       	Integer 	YES     	只能调整3, 5 或者10,举例: maxLeverage=10 就是选择切换成全仓 Pro 模式，maxLeverage = 5 或者3是选择全仓Classic模式
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.set_margin_max_leverage, **to_local(locals()))


    # 获取全仓杠杆划转历史 (USER_DATA)
    def get_margin_transfer(self,asset:str = '',type:str = '',startTime:int = '',endTime:int = '',current:int = '',size:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/transfer

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	NO      	
        type              	STRING  	NO      	划转类型: ROLL_IN, ROLL_OUT
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        current           	LONG    	NO      	当前查询页。 从 1开始。 默认:1
        size              	LONG    	NO      	默认:10 最大:100
        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_transfer, **to_local(locals()))


    # 查询借贷记录 (USER_DATA)
    def get_margin_loan(self,asset:str = '',isolatedSymbol:str = '',txId:int = '',startTime:int = '',endTime:int = '',current:int = '',size:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/loan

        权重(IP):10

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	NO      	
        isolatedSymbol    	STRING  	NO      	如果不发送，会返回全仓数据
        txId              	LONG    	NO      	tranIdin POST /sapi/v1/margin/loan
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        current           	LONG    	NO      	当前查询页。 开始值 1。 默认:1
        size              	LONG    	NO      	默认:10 最大:100
        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_loan, **to_local(locals()))


    # 查询还贷记录 (USER_DATA)
    def get_margin_repay(self,asset:str = '',isolatedSymbol:str = '',txId:int = '',startTime:int = '',endTime:int = '',current:int = '',size:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/repay

        权重(IP)10

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	NO      	
        isolatedSymbol    	STRING  	NO      	逐仓symbol
        txId              	LONG    	NO      	返回 /sapi/v1/margin/repay
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        current           	LONG    	NO      	当前查询页。开始值 1. 默认:1
        size              	LONG    	NO      	默认:10 最大:100
        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_repay, **to_local(locals()))


    # 获取利息历史 (USER_DATA)
    def get_margin_interestHistory(self,asset:str = '',isolatedSymbol:str = '',startTime:int = '',endTime:int = '',current:int = '',size:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/interestHistory

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	NO      	
        isolatedSymbol    	STRING  	NO      	逐仓symbol
        startTime         	LONG    	NO      	精确到秒，忽略毫秒的数值
        endTime           	LONG    	NO      	精确到秒，忽略毫秒的数值
        current           	LONG    	NO      	当前查询页。 开始值 1. 默认:1
        size              	LONG    	NO      	默认:10 最大:100
        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_interestHistory, **to_local(locals()))


    # 获取账户强制平仓记录(USER_DATA)
    def get_margin_forceLiquidationRec(self,startTime:int = '',endTime:int = '',isolatedSymbol:str = '',current:int = '',size:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/forceLiquidationRec

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        isolatedSymbol    	STRING  	NO      	
        current           	LONG    	NO      	当前查询页。 开始值 1. 默认:1
        size              	LONG    	NO      	默认:10 最大:100
        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_forceLiquidationRec, **to_local(locals()))


    # 查询全仓杠杆账户详情 (USER_DATA)
    def get_margin_account(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/account

        权重(IP):10

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_account, **to_local(locals()))


    # 查询杠杆账户订单 (USER_DATA)
    def get_margin_order(self,symbol:str = '',isIsolated:str = '',orderId:int = '',origClientOrderId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/order

        权重(IP):10

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        isIsolated        	STRING  	NO      	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        orderId           	LONG    	NO      	
        origClientOrderId 	STRING  	NO      	
        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_order, **to_local(locals()))


    # 查询杠杆账户挂单记录 (USER_DATA)
    def get_margin_openOrders(self,symbol:str = '',isIsolated:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/openOrders

        权重(IP):10

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        isIsolated        	STRING  	NO      	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_openOrders, **to_local(locals()))


    # 查询杠杆账户的所有订单 (USER_DATA)
    def get_margin_allOrders(self,symbol:str = '',isIsolated:str = '',orderId:int = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/allOrders

        权重(IP):200

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        isIsolated        	STRING  	NO      	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        orderId           	LONG    	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	默认 500;最大500.
        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_allOrders, **to_local(locals()))


    # 杠杆账户 OCO 下单(TRADE)
    def set_margin_order_oco(self,symbol:str = '',isIsolated:str = '',listClientOrderId:str = '',side:str = '',quantity:Union[int,float] = '',limitClientOrderId:str = '',price:Union[int,float] = '',limitIcebergQty:Union[int,float] = '',stopClientOrderId:str = '',stopPrice:Union[int,float] = '',stopLimitPrice:Union[int,float] = '',stopIcebergQty:Union[int,float] = '',stopLimitTimeInForce:str = '',newOrderRespType:str = '',sideEffectType:str = '',selfTradePreventionMode:str = '',autoRepayAtCancel:bool = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/margin/order/oco

        权重(UID): 6

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        isIsolated        	STRING  	NO      	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        listClientOrderId 	STRING  	NO      	整个orderList的唯一ID
        side              	ENUM    	YES     	详见枚举定义：订单方向
        quantity          	DECIMAL 	YES     	
        limitClientOrderId	STRING  	NO      	限价单的唯一ID
        price             	DECIMAL 	YES     	
        limitIcebergQty   	DECIMAL 	NO      	
        stopClientOrderId 	STRING  	NO      	止损/止损限价单的唯一ID
        stopPrice         	DECIMAL 	YES     	
        stopLimitPrice    	DECIMAL 	NO      	如果提供，须配合提交stopLimitTimeInForce
        stopIcebergQty    	DECIMAL 	NO      	
        stopLimitTimeInForce	ENUM    	NO      	有效值GTC/FOK/IOC
        newOrderRespType  	ENUM    	NO      	详见枚举定义：订单返回类型
        sideEffectType    	ENUM    	NO      	NO_SIDE_EFFECT, MARGIN_BUY, AUTO_REPAY,AUTO_BORROW_REPAY; 默认为 NO_SIDE_EFFECT
        selfTradePreventionMode	ENUM    	NO      	允许的 ENUM 取决于交易对的配置。支持的值有 EXPIRE_TAKER，EXPIRE_MAKER，EXPIRE_BOTH，NONE
        autoRepayAtCancel 	BOOLEAN 	NO      	只有在自动借款单或者自动借还单生效，true表示的是撤单后需要把订单产生的借款归还，默认为true
        recvWindow        	LONG    	NO      	不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.set_margin_order_oco, **to_local(locals()))


    # 取消杠杆账户 OCO 订单(TRADE)
    def cancel_margin_orderList(self,symbol:str = '',isIsolated:str = '',orderListId:int = '',listClientOrderId:str = '',newClientOrderId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /sapi/v1/margin/orderList

        权重(UID): 1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        isIsolated        	STRING  	NO      	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        orderListId       	LONG    	NO      	orderListId或listClientOrderId必须被提供
        listClientOrderId 	STRING  	NO      	orderListId或listClientOrderId必须被提供
        newClientOrderId  	STRING  	NO      	用户自定义的本次撤销操作的ID(注意不是被撤销的订单的自定义ID)。如无指定会自动赋值。
        recvWindow        	LONG    	NO      	不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.cancel_margin_orderList, **to_local(locals()))


    # 查询杠杆账户 OCO (USER_DATA)
    def get_margin_orderList(self,isIsolated:str = '',symbol:str = '',orderListId:int = '',origClientOrderId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/orderList

        权重(IP): 10

        请求参数:
        Parameter         	Type    	Required	Description

        isIsolated        	STRING  	NO      	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        symbol            	STRING  	NO      	逐仓杠杆必填，全仓杠杆不支持该参数
        orderListId       	LONG    	NO      	orderListId或origClientOrderId必须提供一个。
        origClientOrderId 	STRING  	NO      	orderListId或origClientOrderId必须提供一个。
        recvWindow        	LONG    	NO      	赋值不得大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_orderList, **to_local(locals()))


    # 查询特定杠杆账户所有 OCO (USER_DATA)
    def get_margin_allOrderList(self,isIsolated:str = '',symbol:str = '',fromId:int = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/allOrderList

        权重(IP): 200

        请求参数:
        Parameter         	Type    	Required	Description

        isIsolated        	STRING  	NO      	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        symbol            	STRING  	NO      	逐仓杠杆必填，全仓杠杆不支持该参数
        fromId            	LONG    	NO      	提供该项后,startTime和endTime都不可提供
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	默认值: 500; 最大值: 1000
        recvWindow        	LONG    	NO      	赋值不能超过60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_allOrderList, **to_local(locals()))


    # 查询杠杆账户 OCO 挂单 (USER_DATA)
    def get_margin_openOrderList(self,isIsolated:str = '',symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/openOrderList

        权重(IP): 10

        请求参数:
        Parameter         	Type    	Required	Description

        isIsolated        	STRING  	NO      	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        symbol            	STRING  	NO      	逐仓杠杆必填，全仓杠杆不支持该参数
        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_openOrderList, **to_local(locals()))


    # 查询杠杆账户交易历史 (USER_DATA)
    def get_margin_myTrades(self,symbol:str = '',isIsolated:str = '',orderId:int = '',startTime:int = '',endTime:int = '',fromId:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/myTrades

        权重(IP):10

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        isIsolated        	STRING  	NO      	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        orderId           	LONG    	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        fromId            	LONG    	NO      	获取TradeId，默认获取近期交易历史。
        limit             	INT     	NO      	默认 500; 最大 1000.
        recvWindow        	LONG    	NO      	默认值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_myTrades, **to_local(locals()))


    # 查询账户最大可借贷额度(USER_DATA)
    def get_margin_maxBorrowable(self,asset:str = '',isolatedSymbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/maxBorrowable

        权重(IP):50

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	YES     	
        isolatedSymbol    	STRING  	NO      	逐仓交易对，适用于逐仓查询
        recvWindow        	LONG    	NO      	默认值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_maxBorrowable, **to_local(locals()))


    # 查询最大可转出额 (USER_DATA)
    def get_margin_maxTransferable(self,asset:str = '',isolatedSymbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/maxTransferable

        权重(IP):50

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	YES     	
        isolatedSymbol    	STRING  	NO      	逐仓交易对，适用于逐仓查询
        recvWindow        	LONG    	NO      	默认值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_maxTransferable, **to_local(locals()))


    # 查询Margin账户信息汇总 (USER_DATA)
    def get_margin_tradeCoeff(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/tradeCoeff

        权重（IP）：10

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_tradeCoeff, **to_local(locals()))


    # 杠杆逐仓账户划转 (MARGIN)
    def set_margin_isolated_transfer(self,asset:str = '',symbol:str = '',transFrom:str = '',transTo:str = '',amount:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/margin/isolated/transfer

        权重(UID):600

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	YES     	被划转的资产, 比如, BTC
        symbol            	STRING  	YES     	逐仓 symbol
        transFrom         	STRING  	YES     	"SPOT", "ISOLATED_MARGIN"
        transTo           	STRING  	YES     	"SPOT", "ISOLATED_MARGIN"
        amount            	DECIMAL 	YES     	划转数量
        recvWindow        	LONG    	NO      	赋值不能大于 60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.set_margin_isolated_transfer, **to_local(locals()))


    # 获取杠杆逐仓划转历史 (USER_DATA)
    def get_margin_isolated_transfer(self,asset:str = '',symbol:str = '',type:str = '',startTime:int = '',endTime:int = '',current:int = '',size:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/isolated/transfer

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	NO      	
        symbol            	STRING  	YES     	逐仓 symbol
        type              	STRING  	NO      	划转类型: ROLL_IN, ROLL_OUT
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        current           	LONG    	NO      	当前查询页。 从 1开始。 默认:1
        size              	LONG    	NO      	默认:10 最大:100
        recvWindow        	LONG    	NO  赋值不能大于 60000	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_isolated_transfer, **to_local(locals()))


    # 查询杠杆逐仓账户信息 (USER_DATA)
    def get_margin_isolated_account(self,symbols:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/isolated/account

        权重(IP):10

        请求参数:
        Parameter         	Type    	Required	Description

        symbols           	STRING  	NO      	最多可以传5个symbol; 由","分隔的字符串表示. e.g. "BTCUSDT,BNBUSDT,ADAUSDT"
        recvWindow        	LONG    	NO      	赋值不能大于 60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_isolated_account, **to_local(locals()))


    # 杠杆逐仓账户停用 (TRADE)
    def cancel_margin_isolated_account(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /sapi/v1/margin/isolated/account

        权重(UID):300

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        recvWindow        	LONG    	NO      	不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.cancel_margin_isolated_account, **to_local(locals()))


    # 杠杆逐仓账户启用 (TRADE)
    def set_margin_isolated_account(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/margin/isolated/account

        权重(UID):300

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        recvWindow        	LONG    	NO      	不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.set_margin_isolated_account, **to_local(locals()))


    # 查询杠杆逐仓账户启用限制 (USER_DATA)
    def get_margin_isolated_accountLimit(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/isolated/accountLimit

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_isolated_accountLimit, **to_local(locals()))


    # 查询逐仓杠杆交易对 (USER_DATA)
    def get_margin_isolated_pair(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/isolated/pair

        权重(IP):10

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        recvWindow        	LONG    	NO      	赋值不能大于 60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_isolated_pair, **to_local(locals()))


    # 获取所有逐仓杠杆交易对(USER_DATA)
    def get_margin_isolated_allPairs(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/isolated/allPairs

        权重(IP):10

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	赋值不能大于 60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_isolated_allPairs, **to_local(locals()))


    # 现货交易和杠杆利息BNB抵扣开关(USER_DATA)
    def set_bnbBurn(self,spotBNBBurn:str = '',interestBNBBurn:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/bnbBurn

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        spotBNBBurn       	STRING  	NO      	"true" or "false", 是否使用BNB支付现货交易的手续费
        interestBNBBurn   	STRING  	NO      	"true" or "false", 是否使用BNB支付杠杆贷款的利息
        recvWindow        	LONG    	NO      	赋值不能大于 60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.set_bnbBurn, **to_local(locals()))


    # 获取BNB抵扣开关状态 (USER_DATA)
    def get_bnbBurn(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/bnbBurn

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	赋值不能大于 60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_bnbBurn, **to_local(locals()))


    # 获取杠杆利率历史 (USER_DATA)
    def get_margin_interestRateHistory(self,asset:str = '',vipLevel:int = '',startTime:int = '',endTime:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/interestRateHistory

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	YES     	
        vipLevel          	INT     	NO      	默认用户当前等级
        startTime         	LONG    	NO      	默认7天前
        endTime           	LONG    	NO      	默认当天，时间间隔最大为1个月
        recvWindow        	LONG    	NO      	赋值不能大于 60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_interestRateHistory, **to_local(locals()))


    # 获取全仓杠杆利率及限额 (USER_DATA)
    def get_margin_crossMarginData(self,vipLevel:int = '',coin:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/crossMarginData

        权重:1 指定币种; 5 币种参数缺失

        请求参数:
        Parameter         	Type    	Required	Description

        vipLevel          	INT     	NO      	当未发送参数vipLevel时，将返回用户当前vip等级的数据；当发送参数vipLevel时，将返回对应vip等级的数据
        coin              	STRING  	NO      	
        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_crossMarginData, **to_local(locals()))


    # 获取逐仓杠杆利率及限额 (USER_DATA)
    def get_margin_isolatedMarginData(self,vipLevel:int = '',symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/isolatedMarginData

        权重(IP):1 指定交易对; 10 交易对参数缺失

        请求参数:
        Parameter         	Type    	Required	Description

        vipLevel          	INT     	NO      	默认为用户当前VIP等级
        symbol            	STRING  	NO      	
        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_isolatedMarginData, **to_local(locals()))


    # 获取逐仓档位信息 (USER_DATA)
    def get_margin_isolatedMarginTier(self,symbol:str = '',tier:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/isolatedMarginTier

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        tier              	INTEGER 	NO      	不传则返回所有逐仓杠杆档位
        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_isolatedMarginTier, **to_local(locals()))


    # 查询目前杠杆账户下单数 (TRADE)
    def get_margin_rateLimit_order(self,isIsolated:str = '',symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/rateLimit/order

        权重(IP):20

        请求参数:
        Parameter         	Type    	Required	Description

        isIsolated        	STRING  	NO      	是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"
        symbol            	STRING  	NO      	逐仓交易对，查询逐仓杠杆账户必需
        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_rateLimit_order, **to_local(locals()))


    # 杠杆小额资产转换BNB历史 (USER_DATA)
    def get_margin_dribblet(self,startTime:int = '',endTime:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/dribblet

        权重(IP):100

        请求参数:
        Parameter         	Type    	Required	Description

        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_dribblet, **to_local(locals()))


    # 获取可以转换成BNB的小额资产 (USER_DATA)
    def get_margin_dust(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/dust

        权重(IP):100

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_dust, **to_local(locals()))


    # 杠杆小额资产转换 (TRADE)
    def set_margin_dust(self,asset:list = [],recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/margin/dust

        权重(UID):3000

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	ARRAY   	YES     	正在转换的资产。 例如：asset=BTC,USDT
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.set_margin_dust, **to_local(locals()))


    # 全仓币种质押率 (MARKET_DATA)
    def get_margin_crossMarginCollateralRatio(self,proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/crossMarginCollateralRatio

        权重(IP):100
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_crossMarginCollateralRatio, **to_local(locals()))


    # 查询可小额负债转换的资产 (USER_DATA)
    def get_margin_exchange_small_liability(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/exchange-small-liability

        权重(IP):100

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_exchange_small_liability, **to_local(locals()))


    # 全仓杠杆小额负债转换 (MARGIN)
    def set_margin_exchange_small_liability(self,assetNames:list = [],recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/margin/exchange-small-liability

        权重(UID):3000

        请求参数:
        Parameter         	Type    	Required	Description

        assetNames        	ARRAY   	YES     	小额转换的资产列表，举例: assetNames = BTC,ETH
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.set_margin_exchange_small_liability, **to_local(locals()))


    # 查询全仓杠杆小额负债转换历史  (USER_DATA)
    def get_margin_exchange_small_liability_history(self,current:int = '',size:int = '',startTime:int = '',endTime:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/exchange-small-liability-history

        权重(UID):100

        请求参数:
        Parameter         	Type    	Required	Description

        current           	INT     	YES     	当前页面，默认1，最小值为1
        size              	INT     	YES     	页面大小，默认10，最大值为100
        startTime         	LONG    	NO      	默认当前时间30天前的时间戳
        endTime           	LONG    	NO      	默认当前时间戳
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_exchange_small_liability_history, **to_local(locals()))


    # 查询下小时预估利率 (USER_DATA)
    def get_margin_next_hourly_interest_rate(self,assets:str = '',isIsolated:bool = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/next-hourly-interest-rate

        权重(IP):100

        请求参数:
        Parameter         	Type    	Required	Description

        assets            	String  	YES     	资产列表，以逗号分隔，最多20个
        isIsolated        	Boolean 	YES     	是否逐仓杠杆，"TRUE", "FALSE"
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_next_hourly_interest_rate, **to_local(locals()))


    # 查询全仓/逐仓资金流水(USER_DATA)
    def get_margin_capital_flow(self,asset:str = '',symbol:str = '',type:str = '',startTime:int = '',endTime:int = '',fromId:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/capital-flow

        权重(IP):100

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	NO      	
        symbol            	STRING  	NO      	查询逐仓数据时必填
        type              	STRING  	NO      	
        startTime         	LONG    	NO      	只支持查询最近90天的数据
        endTime           	LONG    	NO      	
        fromId            	LONG    	NO      	如设置fromId, 将返回id > fromId的数据。否则将返回最新数据
        limit             	LONG    	NO      	每次返回的数据条数限制。默认 500; 最大 1000.
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_capital_flow, **to_local(locals()))


    # 查询全仓和逐仓的币种或币对的下架计划 (MARKET_DATA)
    def get_margin_delist_schedule(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/delist-schedule

        权重(IP):100

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_delist_schedule, **to_local(locals()))


    # 杠杆可用放贷库存查询(USER_DATA)
    def get_margin_available_inventory(self,type:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/available-inventory

        权重(UID):50

        请求参数:
        Parameter         	Type    	Required	Description

        type              	STRING  	YES     	MARGIN,ISOLATED
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_available_inventory, **to_local(locals()))


    # 杠杆手动强平(MARGIN)
    def set_margin_manual_liquidation(self,type:str = '',symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/margin/manual-liquidation

        权重(UID):3000

        请求参数:
        Parameter         	Type    	Required	Description

        type              	STRING  	YES     	MARGIN,ISOLATED
        symbol            	STRING  	NO      	type选择ISOLATED后，symbol需要填入
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.set_margin_manual_liquidation, **to_local(locals()))


    # 查询全仓杠杆Pro模式下的负债币种杠杆与保证金率(MARKET_DATA)
    def get_margin_leverageBracket(self,proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/margin/leverageBracket

        权重(IP):1
        '''
        return self.send_request(*_MarginAccountTradeEndpoints.get_margin_leverageBracket, **to_local(locals()))