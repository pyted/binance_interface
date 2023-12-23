# NFT 接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _NftEndpoints():


    get_nft_history_transactions = ['https://api.binance.com', 'GET', '/sapi/v1/nft/history/transactions', True] # 获取 NFT 资金流水记录 (USER_DATA) 
    get_nft_history_deposit = ['https://api.binance.com', 'GET', '/sapi/v1/nft/history/deposit', True] # 获取 NFT 充值记录 (USER_DATA) 
    get_nft_history_withdraw = ['https://api.binance.com', 'GET', '/sapi/v1/nft/history/withdraw', True] # 获取 NFT 提现记录 (USER_DATA) 
    get_nft_user_getAsset = ['https://api.binance.com', 'GET', '/sapi/v1/nft/user/getAsset', True] # 获取 NFT 资产 (USER_DATA)  


class Nft(Client):

    # 获取 NFT 资金流水记录 (USER_DATA)
    def get_nft_history_transactions(self,orderType:int = '',startTime:int = '',endTime:int = '',limit:int = '',page:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/nft/history/transactions

        权重(UID):3000

        请求参数:
        Parameter         	Type    	Required	Description

        orderType         	INT     	YES     	0:买单，1:卖单，2:版税收入，3:一级市场买单，4:mint 费用
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	默认 50, 最大 50
        page              	INT     	NO      	默认 1
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_NftEndpoints.get_nft_history_transactions, **to_local(locals()))


    # 获取 NFT 充值记录 (USER_DATA)
    def get_nft_history_deposit(self,startTime:int = '',endTime:int = '',limit:int = '',page:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/nft/history/deposit

        权重(UID):3000

        请求参数:
        Parameter         	Type    	Required	Description

        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	默认 50, 最大 50
        page              	INT     	NO      	默认 1
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_NftEndpoints.get_nft_history_deposit, **to_local(locals()))


    # 获取 NFT 提现记录 (USER_DATA)
    def get_nft_history_withdraw(self,startTime:int = '',endTime:int = '',limit:int = '',page:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/nft/history/withdraw

        权重(UID):3000

        请求参数:
        Parameter         	Type    	Required	Description

        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	默认 50, 最大 50
        page              	INT     	NO      	默认 1
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_NftEndpoints.get_nft_history_withdraw, **to_local(locals()))


    # 获取 NFT 资产 (USER_DATA)
    def get_nft_user_getAsset(self,limit:int = '',page:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/nft/user/getAsset

        权重(UID):3000

        请求参数:
        Parameter         	Type    	Required	Description

        limit             	INT     	NO      	默认 50, 最大 50
        page              	INT     	NO      	默认 1
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_NftEndpoints.get_nft_user_getAsset, **to_local(locals()))