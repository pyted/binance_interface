# 合约策略交易接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _FuturesAlgoEndpoints():


    set_algo_futures_newOrderVp = ['https://api.binance.com', 'POST', '/sapi/v1/algo/futures/newOrderVp', True] # 成交量份额参与算法(VP)下单 (TRADE) 
    set_algo_futures_newOrderTwap = ['https://api.binance.com', 'POST', '/sapi/v1/algo/futures/newOrderTwap', True] # 时间加权平均价格策略(Twap)下单 (TRADE) 
    cancel_algo_futures_order = ['https://api.binance.com', 'DELETE', '/sapi/v1/algo/futures/order', True] # 取消策略订单 (TRADE) 
    get_algo_futures_openOrders = ['https://api.binance.com', 'GET', '/sapi/v1/algo/futures/openOrders', True] # 查询当前策略订单挂单 (USER_DATA) 
    get_algo_futures_historicalOrders = ['https://api.binance.com', 'GET', '/sapi/v1/algo/futures/historicalOrders', True] # 查询历史策略订单 (USER_DATA) 
    get_algo_futures_subOrders = ['https://api.binance.com', 'GET', '/sapi/v1/algo/futures/subOrders', True] # 查询执行子订单 (USER_DATA)  


class FuturesAlgo(Client):

    # 成交量份额参与算法(VP)下单 (TRADE)
    def set_algo_futures_newOrderVp(self,symbol:str = '',side:str = '',positionSide:str = '',quantity:Union[int,float] = '',urgency:str = '',clientAlgoId:str = '',reduceOnly:bool = '',limitPrice:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/algo/futures/newOrderVp

        权重(UID):3000

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对 eg. BTCUSDT
        side              	ENUM    	YES     	买卖方向 ( BUY or SELL )
        positionSide      	ENUM    	NO      	持仓方向，单向持仓模式下非必填，默认且仅可填BOTH;在双向持仓模式下必填,且仅可选择 LONG 或 SHORT
        quantity          	DECIMAL 	YES     	下单数量， 以合约币种（base asset）个数下单; 名义价值 (quantity*标记价格(base asset)) 需要大于 1,000 USDT，且不超过 1,000,000 USDT
        urgency           	ENUM    	YES     	代表当前执行的相对速率; ENUM: LOW（慢）, MEDIUM（中等）, HIGH（快）
        clientAlgoId      	STRING  	NO      	必须传入32位，如果未发送，则自动生成
        reduceOnly        	BOOLEAN 	NO      	true, false; 非双开模式下默认false；双开模式下不接受此参数； 开仓不接受此参数
        limitPrice        	DECIMAL 	NO      	限价单价格; 若未发送，则以市场价下单
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_FuturesAlgoEndpoints.set_algo_futures_newOrderVp, **to_local(locals()))


    # 时间加权平均价格策略(Twap)下单 (TRADE)
    def set_algo_futures_newOrderTwap(self,symbol:str = '',side:str = '',positionSide:str = '',quantity:Union[int,float] = '',duration:int = '',clientAlgoId:str = '',reduceOnly:bool = '',limitPrice:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/algo/futures/newOrderTwap

        权重(UID):3000

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对 eg. BTCUSDT
        side              	ENUM    	YES     	买卖方向 ( BUY or SELL )
        positionSide      	ENUM    	NO      	持仓方向，单向持仓模式下非必填，默认且仅可填BOTH;在双向持仓模式下必填,且仅可选择 LONG 或 SHORT
        quantity          	DECIMAL 	YES     	下单数量， 以合约币种（base asset）个数下单; 名义价值 (quantity*标记价格(base asset)) 需要大于 10,000 USDT，且不超过 1,000,000 USDT
        duration          	LONG    	YES     	请以秒为单位发送[300,86400]；少于 5 分钟 => 默认为 5 分钟；大于 24h => 默认为 24h
        clientAlgoId      	STRING  	NO      	必须传入32位，如果未发送，则自动生成
        reduceOnly        	BOOLEAN 	NO      	true, false; 非双开模式下默认false；双开模式下不接受此参数； 开仓不接受此参数
        limitPrice        	DECIMAL 	NO      	限价单价格; 若未发送，则以市场价下单
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_FuturesAlgoEndpoints.set_algo_futures_newOrderTwap, **to_local(locals()))


    # 取消策略订单 (TRADE)
    def cancel_algo_futures_order(self,algoId:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /sapi/v1/algo/futures/order

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        algoId            	LONG    	YES     	eg. 14511
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_FuturesAlgoEndpoints.cancel_algo_futures_order, **to_local(locals()))


    # 查询当前策略订单挂单 (USER_DATA)
    def get_algo_futures_openOrders(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/algo/futures/openOrders

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_FuturesAlgoEndpoints.get_algo_futures_openOrders, **to_local(locals()))


    # 查询历史策略订单 (USER_DATA)
    def get_algo_futures_historicalOrders(self,symbol:str = '',side:str = '',startTime:int = '',endTime:int = '',page:int = '',pageSize:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/algo/futures/historicalOrders

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	交易对 eg. BTCUSDT
        side              	ENUM    	NO      	BUY 或者 SELL
        startTime         	LONG    	NO      	毫秒级时间戳  eg.1641522717552
        endTime           	LONG    	NO      	毫秒级时间戳  eg.1641522526562
        page              	INT     	NO      	默认 1
        pageSize          	INT     	NO      	最小 1, 最大 100; 默认 100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_FuturesAlgoEndpoints.get_algo_futures_historicalOrders, **to_local(locals()))


    # 查询执行子订单 (USER_DATA)
    def get_algo_futures_subOrders(self,algoId:int = '',page:int = '',pageSize:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/algo/futures/subOrders

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        algoId            	LONG    	YES     	
        page              	INT     	NO      	默认1
        pageSize          	INT     	NO      	最小 1， 最大 100; 默认 100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_FuturesAlgoEndpoints.get_algo_futures_subOrders, **to_local(locals()))