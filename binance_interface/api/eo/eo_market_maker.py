# 做市商接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _EOMarketMakerEndpoints():


    get_marginAccount = ['https://eapi.binance.com', 'GET', '/eapi/v1/marginAccount', False] # 保证金账户信息
    set_mmpSet = ['https://eapi.binance.com', 'POST', '/eapi/v1/mmpSet', False] # 设置MMP规则
    get_mmpSet = ['https://eapi.binance.com', 'GET', '/eapi/v1/mmpSet', False] # 获取MMP规则
    set_mmpReset = ['https://eapi.binance.com', 'POST', '/eapi/v1/mmpReset', False] # 重置MMP状态
    set_countdownCancelAll = ['https://eapi.binance.com', 'POST', '/eapi/v1/countdownCancelAll', True] # 设置倒计时取消所有订单配置 (TRADE) 
    get_countdownCancelAll = ['https://eapi.binance.com', 'GET', '/eapi/v1/countdownCancelAll', True] # 获得倒计时自动取消所有订单配置 (TRADE) 
    set_countdownCancelAllHeartBeat = ['https://eapi.binance.com', 'POST', '/eapi/v1/countdownCancelAllHeartBeat', True] # 重置倒计时取消所有订单心跳 (TRADE)  


class EOMarketMaker(Client):

    # 保证金账户信息
    def get_marginAccount(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /eapi/v1/marginAccount

        权重:3

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	NO
        '''
        return self.send_request(*_EOMarketMakerEndpoints.get_marginAccount, **to_local(locals()))


    # 设置MMP规则
    def set_mmpSet(self,underlying:str = '',windowTimeInMilliseconds:int = '',frozenTimeInMilliseconds:int = '',qtyLimit:Union[int,float] = '',deltaLimit:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /eapi/v1/mmpSet

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        underlying        	STRING  	YES     	标的资产如BTCUSDT
        windowTimeInMilliseconds	LONG    	YES     	MMP监控时间窗口（毫秒），在(0,5000]之间
        frozenTimeInMilliseconds	LONG    	NO      	MMP冻结时间（毫秒），设置为0后代表账号为冻结状态，需要手动重置
        qtyLimit          	DECIMAL 	NO      	数量限制
        deltaLimit        	DECIMAL 	NO      	净delta限制
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	NO
        '''
        return self.send_request(*_EOMarketMakerEndpoints.set_mmpSet, **to_local(locals()))


    # 获取MMP规则
    def get_mmpSet(self,underlying:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /eapi/v1/mmpSet

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        underlying        	STRING  	YES     	标的资产如BTCUSDT
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	NO
        '''
        return self.send_request(*_EOMarketMakerEndpoints.get_mmpSet, **to_local(locals()))


    # 重置MMP状态
    def set_mmpReset(self,underlying:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /eapi/v1/mmpReset

        

        请求参数:
        Parameter         	Type    	Required	Description

        underlying        	STRING  	YES     	标的资产如BTCUSDT
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	NO
        '''
        return self.send_request(*_EOMarketMakerEndpoints.set_mmpReset, **to_local(locals()))


    # 设置倒计时取消所有订单配置 (TRADE)
    def set_countdownCancelAll(self,underlying:str = '',countdownTime:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /eapi/v1/countdownCancelAll

        此接口用于设置倒计时取消所有订单（包括做市商保护订单与普通订单）配置，即在倒计时结束前心跳没有更新，特定标的资产的所有订单会被取消。若倒计时结束前心跳没有更新，所有的订单将会被取消，同时新订单会返回错误代码-2010。可以通过设置countdownTime为0取消此功能。权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        underlying        	STRING  	YES     	期权标的资产， 如 BTCUSDT
        countdownTime     	LONG    	YES     	以毫秒计量倒计时长 (1000代表1秒)。 设为0时关闭倒计时。最小设为5000（负值无效）
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_EOMarketMakerEndpoints.set_countdownCancelAll, **to_local(locals()))


    # 获得倒计时自动取消所有订单配置 (TRADE)
    def get_countdownCancelAll(self,underlying:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /eapi/v1/countdownCancelAll

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        underlying        	STRING  	YES     	期权标的资产， 如BTCUSDT
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_EOMarketMakerEndpoints.get_countdownCancelAll, **to_local(locals()))


    # 重置倒计时取消所有订单心跳 (TRADE)
    def set_countdownCancelAllHeartBeat(self,underlyings:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /eapi/v1/countdownCancelAllHeartBeat

        权重:10

        请求参数:
        Parameter         	Type    	Required	Description

        underlyings       	STRING  	YES     	期权标的资产， 如BTCUSDT
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_EOMarketMakerEndpoints.set_countdownCancelAllHeartBeat, **to_local(locals()))