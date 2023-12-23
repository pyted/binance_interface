# 币安礼品卡接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _GiftCardEndpoints():


    set_giftcard_createCode = ['https://api.binance.com', 'POST', '/sapi/v1/giftcard/createCode', True] # 创建单币种礼品卡 (USER_DATA) 
    set_giftcard_buyCode = ['https://api.binance.com', 'POST', '/sapi/v1/giftcard/buyCode', True] # 创建双币种礼品卡（固定价值，设置折扣） (TRADE) 
    set_giftcard_redeemCode = ['https://api.binance.com', 'POST', '/sapi/v1/giftcard/redeemCode', True] # 兑现币安礼品卡 (USER_DATA) 
    get_giftcard_verify = ['https://api.binance.com', 'GET', '/sapi/v1/giftcard/verify', True] # 通过礼品卡卡号验证币安礼品卡 (USER_DATA) 
    get_giftcard_cryptography_rsa_public_key = ['https://api.binance.com', 'GET', '/sapi/v1/giftcard/cryptography/rsa-public-key', True] # 获取RSA Public Key (USER_DATA) 
    get_giftcard_buyCode_token_limit = ['https://api.binance.com', 'GET', '/sapi/v1/giftcard/buyCode/token-limit', True] # 获取货币使用限制 (USER_DATA)  


class GiftCard(Client):

    # 创建单币种礼品卡 (USER_DATA)
    def set_giftcard_createCode(self,token:str = '',amount:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/giftcard/createCode

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        token             	STRING  	YES     	币安礼品卡中的数字货币币种
        amount            	DOUBLE  	YES     	币安礼品卡中的数字货币数量
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_GiftCardEndpoints.set_giftcard_createCode, **to_local(locals()))


    # 创建双币种礼品卡（固定价值，设置折扣） (TRADE)
    def set_giftcard_buyCode(self,baseToken:str = '',faceToken:str = '',baseTokenAmount:Union[int,float] = '',discount:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/giftcard/buyCode

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        baseToken         	STRING  	YES     	你用来支付的货币，例如：BUSD
        faceToken         	STRING  	YES     	你创建的礼品卡面额，例如：BNB。如果 faceToken = baseToken, 将等同于使用 createCode API
        baseTokenAmount   	DOUBLE  	YES     	支付的货币数量，例如：1.002
        discount          	DOUBLE  	NO      	稳定币定值礼品卡的折扣百分比，例如：1 代表 1% 的折扣。小数点精度需小于 6。
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_GiftCardEndpoints.set_giftcard_buyCode, **to_local(locals()))


    # 兑现币安礼品卡 (USER_DATA)
    def set_giftcard_redeemCode(self,code:str = '',externalUid:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/giftcard/redeemCode

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        code              	STRING  	YES     	用于赎回的币安礼品卡，支持加密&未加密两种方式
        externalUid       	String  	NO      	每个外部用户 ID 代表合作伙伴平台上的某个用户。该功能帮助您识别不同用户的兑现行为，例如兑现频次和金额。它还有助于对单个账户进行风险和限额控制，例如设置单个账户每日兑现金额、频次和卡密输错次数的上限。这也将防止单个帐户突破合作伙伴的每日兑现限额从而导致合作伙伴的账户在当日无法继续制码或者兑现。如果您有外部的网站且有不同的用户在您的平台上兑现 币安礼品卡，我们强烈建议您使用此功能并将您用户的用户 ID 传输给我们来进行风控。为保护用户的信息安全，您可以选择以任何格式（上限为 400 个字符）传输用户 ID。
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_GiftCardEndpoints.set_giftcard_redeemCode, **to_local(locals()))


    # 通过礼品卡卡号验证币安礼品卡 (USER_DATA)
    def get_giftcard_verify(self,referenceNo:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/giftcard/verify

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        referenceNo       	STRING  	YES     	输入礼品卡卡号
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_GiftCardEndpoints.get_giftcard_verify, **to_local(locals()))


    # 获取RSA Public Key (USER_DATA)
    def get_giftcard_cryptography_rsa_public_key(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/giftcard/cryptography/rsa-public-key

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_GiftCardEndpoints.get_giftcard_cryptography_rsa_public_key, **to_local(locals()))


    # 获取货币使用限制 (USER_DATA)
    def get_giftcard_buyCode_token_limit(self,baseToken:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/giftcard/buyCode/token-limit

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        baseToken         	STRING  	YES     	你用来支付的货币，例如：BUSD
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_GiftCardEndpoints.get_giftcard_buyCode_token_limit, **to_local(locals()))