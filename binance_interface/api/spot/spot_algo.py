# 现货策略交易接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _SPOTAlgoEndpoints():


    set_algo_spot_newOrderTwap = ['https://api.binance.com', 'POST', '/sapi/v1/algo/spot/newOrderTwap', True] # 时间加权平均价格策略(Twap)下单 (TRADE) 
    cancel_algo_spot_order = ['https://api.binance.com', 'DELETE', '/sapi/v1/algo/spot/order', True] # 取消TWAP策略订单 (TRADE) 
    get_algo_spot_openOrders = ['https://api.binance.com', 'GET', '/sapi/v1/algo/spot/openOrders', True] # 查询当前策略订单挂单 (USER_DATA) 
    get_algo_spot_historicalOrders = ['https://api.binance.com', 'GET', '/sapi/v1/algo/spot/historicalOrders', True] # 查询历史策略订单 (USER_DATA) 
    get_algo_spot_subOrders = ['https://api.binance.com', 'GET', '/sapi/v1/algo/spot/subOrders', True] # 查询执行子订单 (USER_DATA)  


class SPOTAlgo(Client):

    # 时间加权平均价格策略(Twap)下单 (TRADE)
    def set_algo_spot_newOrderTwap(self,symbol:str = '',side:str = '',quantity:Union[int,float] = '',duration:int = '',clientAlgoId:str = '',limitPrice:Union[int,float] = '',stpMode:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/algo/spot/newOrderTwap

        权重(UID):3000

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对 eg. BTCUSDT
        side              	ENUM    	YES     	买卖方向 ( BUY or SELL )
        quantity          	DECIMAL 	YES     	下单数量， 以Base资产个数下单; 名义价值 (quantity* 最新价格(base asset)) 需要大于 1,000 USDT，且不超过 100,000 USDT
        duration          	LONG    	YES     	请以秒为单位发送[300,86400]；少于 5 分钟 => 默认为 5 分钟；大于 24h => 默认为 24h
        clientAlgoId      	STRING  	NO      	必须传入32位，如果未发送，则自动生成
        limitPrice        	DECIMAL 	NO      	限价单价格; 若未发送，则以市场价下单
        stpMode           	ENUM    	NO      	允许的 ENUM 取决于交易对的配置。支持的值有EXPIRE_TAKER,EXPIRE_MAKER,EXPIRE_BOTH,NONE
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SPOTAlgoEndpoints.set_algo_spot_newOrderTwap, **to_local(locals()))


    # 取消TWAP策略订单 (TRADE)
    def cancel_algo_spot_order(self,algoId:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /sapi/v1/algo/spot/order

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        algoId            	LONG    	YES     	eg. 14511
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SPOTAlgoEndpoints.cancel_algo_spot_order, **to_local(locals()))


    # 查询当前策略订单挂单 (USER_DATA)
    def get_algo_spot_openOrders(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/algo/spot/openOrders

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SPOTAlgoEndpoints.get_algo_spot_openOrders, **to_local(locals()))


    # 查询历史策略订单 (USER_DATA)
    def get_algo_spot_historicalOrders(self,symbol:str = '',side:str = '',startTime:int = '',endTime:int = '',page:int = '',pageSize:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/algo/spot/historicalOrders

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
        return self.send_request(*_SPOTAlgoEndpoints.get_algo_spot_historicalOrders, **to_local(locals()))


    # 查询执行子订单 (USER_DATA)
    def get_algo_spot_subOrders(self,algoId:int = '',page:int = '',pageSize:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/algo/spot/subOrders

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        algoId            	LONG    	YES     	
        page              	INT     	NO      	默认1
        pageSize          	INT     	NO      	最小 1， 最大 100; 默认 100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SPOTAlgoEndpoints.get_algo_spot_subOrders, **to_local(locals()))