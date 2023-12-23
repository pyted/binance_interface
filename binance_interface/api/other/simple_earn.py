# 赚币接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _SimpleEarnEndpoints():


    get_simple_earn_flexible_list = ['https://api.binance.com', 'GET', '/sapi/v1/simple-earn/flexible/list', True] # 查询赚币活期产品列表 (USER_DATA) 
    get_simple_earn_locked_list = ['https://api.binance.com', 'GET', '/sapi/v1/simple-earn/locked/list', True] # 查询赚币定期产品列表(USER_DATA) 
    set_simple_earn_flexible_subscribe = ['https://api.binance.com', 'POST', '/sapi/v1/simple-earn/flexible/subscribe', True] # 申购活期产品 (TRADE) 
    set_simple_earn_locked_subscribe = ['https://api.binance.com', 'POST', '/sapi/v1/simple-earn/locked/subscribe', True] # 申购定期产品(TRADE) 
    set_simple_earn_flexible_redeem = ['https://api.binance.com', 'POST', '/sapi/v1/simple-earn/flexible/redeem', True] # 赎回活期产品 (TRADE) 
    set_simple_earn_locked_redeem = ['https://api.binance.com', 'POST', '/sapi/v1/simple-earn/locked/redeem', True] # 赎回定期产品(TRADE) 
    get_simple_earn_flexible_position = ['https://api.binance.com', 'GET', '/sapi/v1/simple-earn/flexible/position', True] # 获取活期产品持仓(USER_DATA) 
    get_simple_earn_locked_position = ['https://api.binance.com', 'GET', '/sapi/v1/simple-earn/locked/position', True] # 获取定期产品持仓 (USER_DATA) 
    get_simple_earn_account = ['https://api.binance.com', 'GET', '/sapi/v1/simple-earn/account', True] # 赚币账户(USER_DATA) 
    get_simple_earn_flexible_history_subscriptionRecord = ['https://api.binance.com', 'GET', '/sapi/v1/simple-earn/flexible/history/subscriptionRecord', True] # 查询活期申购记录(USER_DATA) 
    get_simple_earn_locked_history_subscriptionRecord = ['https://api.binance.com', 'GET', '/sapi/v1/simple-earn/locked/history/subscriptionRecord', True] # 查询定期申购记录 (USER_DATA) 
    get_simple_earn_flexible_history_redemptionRecord = ['https://api.binance.com', 'GET', '/sapi/v1/simple-earn/flexible/history/redemptionRecord', True] # 查询活期赎回记录 (USER_DATA) 
    get_simple_earn_locked_history_redemptionRecord = ['https://api.binance.com', 'GET', '/sapi/v1/simple-earn/locked/history/redemptionRecord', True] # 查询定期赎回记录 (USER_DATA) 
    get_simple_earn_flexible_history_rewardsRecord = ['https://api.binance.com', 'GET', '/sapi/v1/simple-earn/flexible/history/rewardsRecord', True] # 查询活期收益记录 (USER_DATA) 
    get_simple_earn_locked_history_rewardsRecord = ['https://api.binance.com', 'GET', '/sapi/v1/simple-earn/locked/history/rewardsRecord', True] # 查询定期收益记录 (USER_DATA) 
    set_simple_earn_flexible_setAutoSubscribe = ['https://api.binance.com', 'POST', '/sapi/v1/simple-earn/flexible/setAutoSubscribe', True] # 设置活期自动申购 (USER_DATA) 
    set_simple_earn_locked_setAutoSubscribe = ['https://api.binance.com', 'POST', '/sapi/v1/simple-earn/locked/setAutoSubscribe', True] # 设置定期自动申购 (USER_DATA) 
    get_simple_earn_flexible_personalLeftQuota = ['https://api.binance.com', 'GET', '/sapi/v1/simple-earn/flexible/personalLeftQuota', True] # 查询活期个人剩余额度 (USER_DATA) 
    get_simple_earn_locked_personalLeftQuota = ['https://api.binance.com', 'GET', '/sapi/v1/simple-earn/locked/personalLeftQuota', True] # 查询定期个人剩余额度 (USER_DATA) 
    get_simple_earn_flexible_subscriptionPreview = ['https://api.binance.com', 'GET', '/sapi/v1/simple-earn/flexible/subscriptionPreview', True] # 活期申购预览(USER_DATA) 
    get_simple_earn_locked_subscriptionPreview = ['https://api.binance.com', 'GET', '/sapi/v1/simple-earn/locked/subscriptionPreview', True] # 定期申购预览(USER_DATA) 
    get_simple_earn_flexible_history_rateHistory = ['https://api.binance.com', 'GET', '/sapi/v1/simple-earn/flexible/history/rateHistory', True] # 获取利率历史(USER_DATA) 
    get_simple_earn_flexible_history_collateralRecord = ['https://api.binance.com', 'GET', '/sapi/v1/simple-earn/flexible/history/collateralRecord', True] # 获取抵押物记录(USER_DATA)  


class SimpleEarn(Client):

    # 查询赚币活期产品列表 (USER_DATA)
    def get_simple_earn_flexible_list(self,asset:str = '',current:int = '',size:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/simple-earn/flexible/list

        权重(IP): 150

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	NO      	
        current           	LONG    	NO      	当前查询页。 开始值 1，默认:1
        size              	LONG    	NO      	默认：10，最大：100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SimpleEarnEndpoints.get_simple_earn_flexible_list, **to_local(locals()))


    # 查询赚币定期产品列表(USER_DATA)
    def get_simple_earn_locked_list(self,asset:str = '',current:int = '',size:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/simple-earn/locked/list

        权重(IP): 150

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	NO      	
        current           	LONG    	NO      	当前查询页。 开始值 1，默认:1
        size              	LONG    	NO      	默认：10，最大：100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SimpleEarnEndpoints.get_simple_earn_locked_list, **to_local(locals()))


    # 申购活期产品 (TRADE)
    def set_simple_earn_flexible_subscribe(self,productId:str = '',amount:Union[int,float] = '',autoSubscribe:bool = '',sourceAccount:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/simple-earn/flexible/subscribe

        权重(IP): 1

        请求参数:
        Parameter         	Type    	Required	Description

        productId         	STRING  	YES     	
        amount            	DECIMAL 	YES     	
        autoSubscribe     	BOOLEAN 	NO      	true 或者 false, 默认 true.
        sourceAccount     	ENUM    	NO      	SPOT,FUND,ALL, 默认SPOT
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SimpleEarnEndpoints.set_simple_earn_flexible_subscribe, **to_local(locals()))


    # 申购定期产品(TRADE)
    def set_simple_earn_locked_subscribe(self,projectId:str = '',amount:Union[int,float] = '',autoSubscribe:bool = '',sourceAccount:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/simple-earn/locked/subscribe

        权重(IP): 1

        请求参数:
        Parameter         	Type    	Required	Description

        projectId         	STRING  	YES     	
        amount            	DECIMAL 	YES     	
        autoSubscribe     	BOOLEAN 	NO      	true 或者 false, 默认 true.
        sourceAccount     	ENUM    	NO      	SPOT,FUND,ALL, 默认SPOT
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SimpleEarnEndpoints.set_simple_earn_locked_subscribe, **to_local(locals()))


    # 赎回活期产品 (TRADE)
    def set_simple_earn_flexible_redeem(self,productId:str = '',redeemAll:bool = '',amount:Union[int,float] = '',destAccount:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/simple-earn/flexible/redeem

        权重(IP): 1

        请求参数:
        Parameter         	Type    	Required	Description

        productId         	STRING  	YES     	
        redeemAll         	BOOLEAN 	NO      	true 或者 false, 默认 false
        amount            	DECIMAL 	NO      	当redeemAll为false时必填
        destAccount       	ENUM    	NO      	SPOT,FUND,ALL, 默认SPOT
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SimpleEarnEndpoints.set_simple_earn_flexible_redeem, **to_local(locals()))


    # 赎回定期产品(TRADE)
    def set_simple_earn_locked_redeem(self,positionId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/simple-earn/locked/redeem

        权重(IP): 1

        请求参数:
        Parameter         	Type    	Required	Description

        positionId        	STRING  	YES     	"1234"
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SimpleEarnEndpoints.set_simple_earn_locked_redeem, **to_local(locals()))


    # 获取活期产品持仓(USER_DATA)
    def get_simple_earn_flexible_position(self,asset:str = '',productId:str = '',current:int = '',size:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/simple-earn/flexible/position

        权重(IP): 150

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	NO      	
        productId         	STRING  	NO      	
        current           	LONG    	NO      	当前查询页。 开始值 1，默认:1
        size              	LONG    	NO      	默认：10，最大：100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SimpleEarnEndpoints.get_simple_earn_flexible_position, **to_local(locals()))


    # 获取定期产品持仓 (USER_DATA)
    def get_simple_earn_locked_position(self,asset:str = '',positionId:str = '',projectId:str = '',current:int = '',size:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/simple-earn/locked/position

        权重(IP): 150

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	NO      	
        positionId        	STRING  	NO      	
        projectId         	STRING  	NO      	
        current           	LONG    	NO      	当前查询页。 开始值 1，默认:1
        size              	LONG    	NO      	默认：10，最大：100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SimpleEarnEndpoints.get_simple_earn_locked_position, **to_local(locals()))


    # 赚币账户(USER_DATA)
    def get_simple_earn_account(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/simple-earn/account

        权重(IP): 150

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SimpleEarnEndpoints.get_simple_earn_account, **to_local(locals()))


    # 查询活期申购记录(USER_DATA)
    def get_simple_earn_flexible_history_subscriptionRecord(self,productId:str = '',purchaseId:str = '',asset:str = '',startTime:int = '',endTime:int = '',current:int = '',size:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/simple-earn/flexible/history/subscriptionRecord

        权重(IP): 150

        请求参数:
        Parameter         	Type    	Required	Description

        productId         	STRING  	NO      	
        purchaseId        	STRING  	NO      	
        asset             	STRING  	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        current           	LONG    	NO      	当前查询页。 开始值 1， 默认:1
        size              	LONG    	NO      	默认：10，最大：100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SimpleEarnEndpoints.get_simple_earn_flexible_history_subscriptionRecord, **to_local(locals()))


    # 查询定期申购记录 (USER_DATA)
    def get_simple_earn_locked_history_subscriptionRecord(self,purchaseId:str = '',asset:str = '',startTime:int = '',endTime:int = '',current:int = '',size:int = '',recvWindow:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/simple-earn/locked/history/subscriptionRecord

        权重(IP): 150

        请求参数:
        Parameter         	Type    	Required	Description

        purchaseId        	STRING  	NO      	
        asset             	STRING  	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        current           	LONG    	NO      	当前查询页。 开始值 1， 默认:1
        size              	LONG    	NO      	默认：10，最大：100
        recvWindow        	LONG    	NO
        '''
        return self.send_request(*_SimpleEarnEndpoints.get_simple_earn_locked_history_subscriptionRecord, **to_local(locals()))


    # 查询活期赎回记录 (USER_DATA)
    def get_simple_earn_flexible_history_redemptionRecord(self,productId:str = '',redeemId:str = '',asset:str = '',startTime:int = '',endTime:int = '',current:int = '',size:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/simple-earn/flexible/history/redemptionRecord

        权重(IP): 150

        请求参数:
        Parameter         	Type    	Required	Description

        productId         	STRING  	NO      	
        redeemId          	STRING  	NO      	
        asset             	STRING  	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        current           	LONG    	NO      	当前查询页。 开始值 1， 默认:1
        size              	LONG    	NO      	默认：10，最大：100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SimpleEarnEndpoints.get_simple_earn_flexible_history_redemptionRecord, **to_local(locals()))


    # 查询定期赎回记录 (USER_DATA)
    def get_simple_earn_locked_history_redemptionRecord(self,positionId:str = '',redeemId:str = '',asset:str = '',startTime:int = '',endTime:int = '',current:int = '',size:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/simple-earn/locked/history/redemptionRecord

        权重(IP): 150

        请求参数:
        Parameter         	Type    	Required	Description

        positionId        	STRING  	NO      	
        redeemId          	STRING  	NO      	
        asset             	STRING  	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        current           	LONG    	NO      	当前查询页。 开始值 1， 默认:1
        size              	LONG    	NO      	默认：10，最大：100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SimpleEarnEndpoints.get_simple_earn_locked_history_redemptionRecord, **to_local(locals()))


    # 查询活期收益记录 (USER_DATA)
    def get_simple_earn_flexible_history_rewardsRecord(self,productId:str = '',asset:str = '',startTime:int = '',endTime:int = '',type:str = '',current:int = '',size:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/simple-earn/flexible/history/rewardsRecord

        权重(IP): 150

        请求参数:
        Parameter         	Type    	Required	Description

        productId         	STRING  	NO      	
        asset             	STRING  	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        type              	ENUM    	YES     	"BONUS"额外分级收益,"REALTIME"实时收益,"REWARDS"历史收益
        current           	LONG    	NO      	当前查询页。 开始值 1， 默认:1
        size              	LONG    	NO      	默认：10，最大：100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SimpleEarnEndpoints.get_simple_earn_flexible_history_rewardsRecord, **to_local(locals()))


    # 查询定期收益记录 (USER_DATA)
    def get_simple_earn_locked_history_rewardsRecord(self,positionId:str = '',asset:str = '',startTime:int = '',endTime:int = '',current:int = '',size:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/simple-earn/locked/history/rewardsRecord

        权重(IP): 150

        请求参数:
        Parameter         	Type    	Required	Description

        positionId        	STRING  	NO      	
        asset             	STRING  	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        current           	LONG    	NO      	当前查询页。 开始值 1， 默认:1
        size              	LONG    	NO      	默认：10，最大：100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SimpleEarnEndpoints.get_simple_earn_locked_history_rewardsRecord, **to_local(locals()))


    # 设置活期自动申购 (USER_DATA)
    def set_simple_earn_flexible_setAutoSubscribe(self,productId:str = '',autoSubscribe:bool = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/simple-earn/flexible/setAutoSubscribe

        权重(IP): 150

        请求参数:
        Parameter         	Type    	Required	Description

        productId         	STRING  	YES     	
        autoSubscribe     	BOOLEAN 	YES     	true 或者 false
        recvWindow        	LONG    	NO      	
        timestamp         	LONG
        '''
        return self.send_request(*_SimpleEarnEndpoints.set_simple_earn_flexible_setAutoSubscribe, **to_local(locals()))


    # 设置定期自动申购 (USER_DATA)
    def set_simple_earn_locked_setAutoSubscribe(self,positionId:str = '',autoSubscribe:bool = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/simple-earn/locked/setAutoSubscribe

        权重(IP): 150

        请求参数:
        Parameter         	Type    	Required	Description

        positionId        	STRING  	YES     	
        autoSubscribe     	BOOLEAN 	YES     	true  或者 false
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SimpleEarnEndpoints.set_simple_earn_locked_setAutoSubscribe, **to_local(locals()))


    # 查询活期个人剩余额度 (USER_DATA)
    def get_simple_earn_flexible_personalLeftQuota(self,productId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/simple-earn/flexible/personalLeftQuota

        权重(IP): 150

        请求参数:
        Parameter         	Type    	Required	Description

        productId         	STRING  	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SimpleEarnEndpoints.get_simple_earn_flexible_personalLeftQuota, **to_local(locals()))


    # 查询定期个人剩余额度 (USER_DATA)
    def get_simple_earn_locked_personalLeftQuota(self,projectId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/simple-earn/locked/personalLeftQuota

        权重(IP): 150

        请求参数:
        Parameter         	Type    	Required	Description

        projectId         	STRING  	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SimpleEarnEndpoints.get_simple_earn_locked_personalLeftQuota, **to_local(locals()))


    # 活期申购预览(USER_DATA)
    def get_simple_earn_flexible_subscriptionPreview(self,productId:str = '',amount:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/simple-earn/flexible/subscriptionPreview

        权重(IP): 150

        请求参数:
        Parameter         	Type    	Required	Description

        productId         	STRING  	YES     	
        amount            	DECIMAL 	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SimpleEarnEndpoints.get_simple_earn_flexible_subscriptionPreview, **to_local(locals()))


    # 定期申购预览(USER_DATA)
    def get_simple_earn_locked_subscriptionPreview(self,projectId:str = '',amount:Union[int,float] = '',autoSubscribe:bool = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/simple-earn/locked/subscriptionPreview

        权重(IP): 150

        请求参数:
        Parameter         	Type    	Required	Description

        projectId         	STRING  	YES     	
        amount            	DECIMAL 	YES     	
        autoSubscribe     	BOOLEAN 	NO      	true 或者 false，默认true
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SimpleEarnEndpoints.get_simple_earn_locked_subscriptionPreview, **to_local(locals()))


    # 获取利率历史(USER_DATA)
    def get_simple_earn_flexible_history_rateHistory(self,productId:str = '',startTime:int = '',endTime:int = '',current:int = '',size:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/simple-earn/flexible/history/rateHistory

        权重(IP): 150

        请求参数:
        Parameter         	Type    	Required	Description

        productId         	STRING  	YES     	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        current           	LONG    	NO      	当前查询页。 开始值 1， 默认:1
        size              	LONG    	NO      	默认：10，最大：100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SimpleEarnEndpoints.get_simple_earn_flexible_history_rateHistory, **to_local(locals()))


    # 获取抵押物记录(USER_DATA)
    def get_simple_earn_flexible_history_collateralRecord(self,productId:str = '',startTime:int = '',endTime:int = '',current:int = '',size:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/simple-earn/flexible/history/collateralRecord

        权重(IP): 150

        请求参数:
        Parameter         	Type    	Required	Description

        productId         	STRING  	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        current           	LONG    	NO      	当前查询页。 开始值 1， 默认:1
        size              	LONG    	NO      	默认：10，最大：100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SimpleEarnEndpoints.get_simple_earn_flexible_history_collateralRecord, **to_local(locals()))