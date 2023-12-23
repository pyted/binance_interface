# 币安挖矿接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _BsWapEndpoints():


    get_bswap_pools = ['https://api.binance.com', 'GET', '/sapi/v1/bswap/pools', False] # 获取所有流动资金池 (MARKET_DATA)
    get_bswap_liquidity = ['https://api.binance.com', 'GET', '/sapi/v1/bswap/liquidity', True] # 获取流动资金池具体信息 (USER_DATA) 
    set_bswap_liquidityAdd = ['https://api.binance.com', 'POST', '/sapi/v1/bswap/liquidityAdd', True] # 添加流动性 (TRADE) 
    set_bswap_liquidityRemove = ['https://api.binance.com', 'POST', '/sapi/v1/bswap/liquidityRemove', True] # 移除流动性 (TRADE) 
    get_bswap_liquidityOps = ['https://api.binance.com', 'GET', '/sapi/v1/bswap/liquidityOps', True] # 获取流动性操作记录 (USER_DATA) 
    get_bswap_quote = ['https://api.binance.com', 'GET', '/sapi/v1/bswap/quote', True] # 获取报价 (USER_DATA) 
    set_bswap_swap = ['https://api.binance.com', 'POST', '/sapi/v1/bswap/swap', True] # 交易 (TRADE) 
    get_bswap_swap = ['https://api.binance.com', 'GET', '/sapi/v1/bswap/swap', True] # 获取交易记录 (USER_DATA) 
    get_bswap_poolConfigure = ['https://api.binance.com', 'GET', '/sapi/v1/bswap/poolConfigure', True] # 获取币对池的配置信息 (USER_DATA) 
    get_bswap_addLiquidityPreview = ['https://api.binance.com', 'GET', '/sapi/v1/bswap/addLiquidityPreview', True] # 添加流动性的试算 (USER_DATA) 
    get_bswap_removeLiquidityPreview = ['https://api.binance.com', 'GET', '/sapi/v1/bswap/removeLiquidityPreview', True] # 移除流动性的试算 (USER_DATA) 
    get_bswap_unclaimedRewards = ['https://api.binance.com', 'GET', '/sapi/v1/bswap/unclaimedRewards', True] # 查询未领取的奖励数量  (USER_DATA) 
    set_bswap_claimRewards = ['https://api.binance.com', 'POST', '/sapi/v1/bswap/claimRewards', True] # 领取奖励 (TRADE) 
    get_bswap_claimedHistory = ['https://api.binance.com', 'GET', '/sapi/v1/bswap/claimedHistory', True] # 获取已领取奖励记录 (USER_DATA)  


class BsWap(Client):

    # 获取所有流动资金池 (MARKET_DATA)
    def get_bswap_pools(self,proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/bswap/pools

        权重(IP):1
        '''
        return self.send_request(*_BsWapEndpoints.get_bswap_pools, **to_local(locals()))


    # 获取流动资金池具体信息 (USER_DATA)
    def get_bswap_liquidity(self,poolId:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/bswap/liquidity

        权重(IP):

        请求参数:
        Parameter         	Type    	Required	Description

        poolId            	LONG    	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_BsWapEndpoints.get_bswap_liquidity, **to_local(locals()))


    # 添加流动性 (TRADE)
    def set_bswap_liquidityAdd(self,poolId:int = '',type:str = '',asset:str = '',quantity:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/bswap/liquidityAdd

        权重(UID):1000（额外限制：每个账户每个池子最多每2秒1次）

        请求参数:
        Parameter         	Type    	Required	Description

        poolId            	LONG    	YES     	
        type              	STRING  	NO      	"SINGLE" 为单币添加资产; "COMBINATION" 为双币添加资产。 默认 "SINGLE"
        asset             	STRING  	YES     	
        quantity          	DECIMAL 	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_BsWapEndpoints.set_bswap_liquidityAdd, **to_local(locals()))


    # 移除流动性 (TRADE)
    def set_bswap_liquidityRemove(self,poolId:int = '',type:str = '',asset:list = [],shareAmount:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/bswap/liquidityRemove

        权重(UID):1000（额外限制：每个账户每个池子最多每2秒1次）

        请求参数:
        Parameter         	Type    	Required	Description

        poolId            	LONG    	YES     	
        type              	STRING  	YES     	SINGLE为以单币种移出,COMBINATION为以池中所有币种按比例移出
        asset             	LIST    	NO      	如果是单币种移除则asset参数为必需
        shareAmount       	DECIMAL 	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_BsWapEndpoints.set_bswap_liquidityRemove, **to_local(locals()))


    # 获取流动性操作记录 (USER_DATA)
    def get_bswap_liquidityOps(self,operationId:int = '',poolId:int = '',operation:str = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/bswap/liquidityOps

        权重(UID):3000

        请求参数:
        Parameter         	Type    	Required	Description

        operationId       	LONG    	NO      	
        poolId            	LONG    	NO      	
        operation         	ENUM    	NO      	ADD或REMOVE
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	LONG    	NO      	默认 3, 最大 100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_BsWapEndpoints.get_bswap_liquidityOps, **to_local(locals()))


    # 获取报价 (USER_DATA)
    def get_bswap_quote(self,quoteAsset:str = '',baseAsset:str = '',quoteQty:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/bswap/quote

        权重(UID):150

        请求参数:
        Parameter         	Type    	Required	Description

        quoteAsset        	STRING  	YES     	
        baseAsset         	STRING  	YES     	
        quoteQty          	DECIMAL 	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_BsWapEndpoints.get_bswap_quote, **to_local(locals()))


    # 交易 (TRADE)
    def set_bswap_swap(self,quoteAsset:str = '',baseAsset:str = '',quoteQty:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/bswap/swap

        权重(UID):100（额外限制：每个池子每2秒一次）

        请求参数:
        Parameter         	Type    	Required	Description

        quoteAsset        	STRING  	YES     	
        baseAsset         	STRING  	YES     	
        quoteQty          	DECIMAL 	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_BsWapEndpoints.set_bswap_swap, **to_local(locals()))


    # 获取交易记录 (USER_DATA)
    def get_bswap_swap(self,swapId:int = '',startTime:int = '',endTime:int = '',status:int = '',quoteAsset:str = '',baseAsset:str = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/bswap/swap

        权重(UID):3000

        请求参数:
        Parameter         	Type    	Required	Description

        swapId            	LONG    	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        status            	INT     	NO      	0: 交易中, 1: 交易成功, 2: 交易失败
        quoteAsset        	STRING  	NO      	
        baseAsset         	STRING  	NO      	
        limit             	LONG    	NO      	默认 3, 最大 100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_BsWapEndpoints.get_bswap_swap, **to_local(locals()))


    # 获取币对池的配置信息 (USER_DATA)
    def get_bswap_poolConfigure(self,poolId:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/bswap/poolConfigure

        权重(IP):150

        请求参数:
        Parameter         	Type    	Required	Description

        poolId            	LONG    	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_BsWapEndpoints.get_bswap_poolConfigure, **to_local(locals()))


    # 添加流动性的试算 (USER_DATA)
    def get_bswap_addLiquidityPreview(self,poolId:int = '',type:str = '',quoteAsset:str = '',quoteQty:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/bswap/addLiquidityPreview

        权重(IP):150

        请求参数:
        Parameter         	Type    	Required	Description

        poolId            	LONG    	YES     	
        type              	STRING  	YES     	类型为"SINGLE"意思为单币添加;类型为"COMBINATION"意思为双币添加
        quoteAsset        	STRING  	YES     	
        quoteQty          	DECIMAL 	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_BsWapEndpoints.get_bswap_addLiquidityPreview, **to_local(locals()))


    # 移除流动性的试算 (USER_DATA)
    def get_bswap_removeLiquidityPreview(self,poolId:int = '',type:str = '',quoteAsset:str = '',shareAmount:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/bswap/removeLiquidityPreview

        权重(IP):150

        请求参数:
        Parameter         	Type    	Required	Description

        poolId            	LONG    	YES     	
        type              	STRING  	YES     	类型为"SINGLE"意思为移除获得单币；类型为"COMBINATION"意思为移除获得双币
        quoteAsset        	STRING  	YES     	
        shareAmount       	DECIMAL 	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_BsWapEndpoints.get_bswap_removeLiquidityPreview, **to_local(locals()))


    # 查询未领取的奖励数量  (USER_DATA)
    def get_bswap_unclaimedRewards(self,type:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/bswap/unclaimedRewards

        权重(UID):1000

        请求参数:
        Parameter         	Type    	Required	Description

        type              	INT     	NO      	0:交易挖矿奖励，1:流动性挖矿奖励，默认为0
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_BsWapEndpoints.get_bswap_unclaimedRewards, **to_local(locals()))


    # 领取奖励 (TRADE)
    def set_bswap_claimRewards(self,type:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/bswap/claimRewards

        权重(UID):1000

        请求参数:
        Parameter         	Type    	Required	Description

        type              	INT     	NO      	0:交易挖矿奖励，1:流动性挖矿奖励，默认为0
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_BsWapEndpoints.set_bswap_claimRewards, **to_local(locals()))


    # 获取已领取奖励记录 (USER_DATA)
    def get_bswap_claimedHistory(self,poolId:int = '',assetRewards:str = '',type:int = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/bswap/claimedHistory

        权重(UID):1000

        请求参数:
        Parameter         	Type    	Required	Description

        poolId            	LONG    	NO      	
        assetRewards      	STRING  	NO      	
        type              	INT     	NO      	0:交易挖矿奖励，1:流动性挖矿奖励，默认为0
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	LONG    	NO      	Default 3, max 100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_BsWapEndpoints.get_bswap_claimedHistory, **to_local(locals()))