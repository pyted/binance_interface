# 闪兑接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _ConvertEndpoints():


    get_convert_exchangeInfo = ['https://api.binance.com', 'GET', '/sapi/v1/convert/exchangeInfo', False] # 查询可交易币对信息
    get_convert_assetInfo = ['https://api.binance.com', 'GET', '/sapi/v1/convert/assetInfo', True] # 查询可交易币种精度 (USER_DATA) 
    set_convert_getQuote = ['https://api.binance.com', 'POST', '/sapi/v1/convert/getQuote', True] # 发送获取报价请求 (USER_DATA) 
    set_convert_acceptQuote = ['https://api.binance.com', 'POST', '/sapi/v1/convert/acceptQuote', True] # 接受报价 (TRADE) 
    get_convert_orderStatus = ['https://api.binance.com', 'GET', '/sapi/v1/convert/orderStatus', True] # 查询订单状态 (USER_DATA) 
    get_convert_tradeFlow = ['https://api.binance.com', 'GET', '/sapi/v1/convert/tradeFlow', True] # 获取闪兑交易记录 (USER_DATA)  


class Convert(Client):

    # 查询可交易币对信息
    def get_convert_exchangeInfo(self,fromAsset:str = '',toAsset:str = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/convert/exchangeInfo

        权重(IP):3000

        请求参数:
        Parameter         	Type    	Required	Description

        fromAsset         	STRING  	EITHER OR BOTH	用户售出币种
        toAsset           	STRING  	EITHER OR BOTH	用户买入币种
        '''
        return self.send_request(*_ConvertEndpoints.get_convert_exchangeInfo, **to_local(locals()))


    # 查询可交易币种精度 (USER_DATA)
    def get_convert_assetInfo(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/convert/assetInfo

        权重(IP):100

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	此值不能大于 60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_ConvertEndpoints.get_convert_assetInfo, **to_local(locals()))


    # 发送获取报价请求 (USER_DATA)
    def set_convert_getQuote(self,fromAsset:str = '',toAsset:str = '',fromAmount:Union[int,float] = '',toAmount:Union[int,float] = '',walletType:str = '',validTime:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/convert/getQuote

        权重(UID):200

        请求参数:
        Parameter         	Type    	Required	Description

        fromAsset         	STRING  	YES     	
        toAsset           	STRING  	YES     	
        fromAmount        	DECIMAL 	EITHER  	这是成交后将被扣除的金额
        toAmount          	DECIMAL 	EITHER  	这是成交后将会获得的金额
        walletType        	ENUM    	NO      	可用值为SPOT 或者 FUNDING. 默认值是 SPOT
        validTime         	ENUM    	NO      	可以支持10s、30s、1m、2m等值，默认值为 10s
        recvWindow        	LONG    	NO      	此值不能大于 60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_ConvertEndpoints.set_convert_getQuote, **to_local(locals()))


    # 接受报价 (TRADE)
    def set_convert_acceptQuote(self,quoteId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/convert/acceptQuote

        权重(UID):500

        请求参数:
        Parameter         	Type    	Required	Description

        quoteId           	STRING  	YES     	
        recvWindow        	LONG    	NO      	此值不能大于 60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_ConvertEndpoints.set_convert_acceptQuote, **to_local(locals()))


    # 查询订单状态 (USER_DATA)
    def get_convert_orderStatus(self,orderId:str = '',quoteId:str = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/convert/orderStatus

        权重(UID):100

        请求参数:
        Parameter         	Type    	Required	Description

        orderId           	STRING  	NO      	orderId 和quoteId需要填其中一个
        quoteId           	STRING  	NO      	orderId 和quoteId需要填其中一个
        '''
        return self.send_request(*_ConvertEndpoints.get_convert_orderStatus, **to_local(locals()))


    # 获取闪兑交易记录 (USER_DATA)
    def get_convert_tradeFlow(self,startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/convert/tradeFlow

        权重(UID):3000

        请求参数:
        Parameter         	Type    	Required	Description

        startTime         	LONG    	YES     	
        endTime           	LONG    	YES     	
        limit             	INT     	NO      	默认 100, 最大 1000
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_ConvertEndpoints.get_convert_tradeFlow, **to_local(locals()))