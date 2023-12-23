# 经典统一账户接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _PortfolioEndpoints():


    get_portfolio_account = ['https://api.binance.com', 'GET', '/sapi/v1/portfolio/account', True] # 查询经典统一账户信息 (USER_DATA) 
    get_portfolio_collateralRate = ['https://api.binance.com', 'GET', '/sapi/v1/portfolio/collateralRate', False] # 经典统一账户资产质押率 (MARKET_DATA)
    get_portfolio_pmLoan = ['https://api.binance.com', 'GET', '/sapi/v1/portfolio/pmLoan', True] # 查询经典统一账户穿仓借贷金额 (USER_DATA) 
    set_portfolio_repay = ['https://api.binance.com', 'POST', '/sapi/v1/portfolio/repay', False] # 偿还经典统一账户穿仓负债
    get_portfolio_interest_history = ['https://api.binance.com', 'GET', '/sapi/v1/portfolio/interest-history', True] # 查询经典统一账户期货负余额收息历史(USER_DATA) 
    get_portfolio_asset_index_price = ['https://api.binance.com', 'GET', '/sapi/v1/portfolio/asset-index-price', False] # 查询统一账户资产价格指数(MARKET_DATA) 
    set_portfolio_auto_collection = ['https://api.binance.com', 'POST', '/sapi/v1/portfolio/auto-collection', True] # 资金归集(USER_DATA) 
    set_portfolio_asset_collection = ['https://api.binance.com', 'POST', '/sapi/v1/portfolio/asset-collection', True] # 特定资产资金归集(USER_DATA) 
    set_portfolio_bnb_transfer = ['https://api.binance.com', 'POST', '/sapi/v1/portfolio/bnb-transfer', True] # BNB划转(USER_DATA) 
    set_portfolio_repay_futures_switch = ['https://api.binance.com', 'POST', '/sapi/v1/portfolio/repay-futures-switch', True] # 更改自动清还合约负余额模式(TRADE) 
    get_portfolio_repay_futures_switch = ['https://api.binance.com', 'GET', '/sapi/v1/portfolio/repay-futures-switch', True] # 查询自动清还合约负余额模式(USER_DATA) 
    set_portfolio_repay_futures_negative_balance = ['https://api.binance.com', 'POST', '/sapi/v1/portfolio/repay-futures-negative-balance', True] # 清还合约负余额(USER_DATA) 
    get_portfolio_margin_asset_leverage = ['https://api.binance.com', 'GET', '/sapi/v1/portfolio/margin-asset-leverage', True] # 查询统一账户资产支持杠杆倍数(USER_DATA)


class Portfolio(Client):

    # 查询经典统一账户信息 (USER_DATA)
    def get_portfolio_account(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/portfolio/account

        权重(IP):5

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PortfolioEndpoints.get_portfolio_account, **to_local(locals()))


    # 经典统一账户资产质押率 (MARKET_DATA)
    def get_portfolio_collateralRate(self,proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/portfolio/collateralRate

        权重(IP):50
        '''
        return self.send_request(*_PortfolioEndpoints.get_portfolio_collateralRate, **to_local(locals()))


    # 查询经典统一账户穿仓借贷金额 (USER_DATA)
    def get_portfolio_pmLoan(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/portfolio/pmLoan

        权重(UID):500

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PortfolioEndpoints.get_portfolio_pmLoan, **to_local(locals()))


    # 偿还经典统一账户穿仓负债
    def set_portfolio_repay(self,from_:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/portfolio/repay

        权重(UID):3000

        请求参数:
        Parameter         	Type    	Required	Description

        from              	STRING  	NO      	SPOT或MARGIN，默认SPOT
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        data = to_local(locals())
        data['from'] = data['from_']
        del data['from_']
        return self.send_request(*_PortfolioEndpoints.set_portfolio_repay, **data)


    # 查询经典统一账户期货负余额收息历史(USER_DATA)
    def get_portfolio_interest_history(self,asset:str = '',startTime:int = '',endTime:int = '',size:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/portfolio/interest-history

        权重(IP):50

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	NO      	
        startTime         	LONG    	NO      	起始时间
        endTime           	LONG    	NO      	结束时间
        size              	LONG    	NO      	返回的结果集数量 默认值:10 最大值:100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PortfolioEndpoints.get_portfolio_interest_history, **to_local(locals()))


    # 查询统一账户资产价格指数(MARKET_DATA)
    def get_portfolio_asset_index_price(self,asset:str = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/portfolio/asset-index-price

        权重(IP):

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	NO
        '''
        return self.send_request(*_PortfolioEndpoints.get_portfolio_asset_index_price, **to_local(locals()))


    # 资金归集(USER_DATA)
    def set_portfolio_auto_collection(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/portfolio/auto-collection

        权重(IP):

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PortfolioEndpoints.set_portfolio_auto_collection, **to_local(locals()))


    # 特定资产资金归集(USER_DATA)
    def set_portfolio_asset_collection(self,asset:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/portfolio/asset-collection

        权重(IP):

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PortfolioEndpoints.set_portfolio_asset_collection, **to_local(locals()))


    # BNB划转(USER_DATA)
    def set_portfolio_bnb_transfer(self,amount:Union[int,float] = '',transferSide:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/portfolio/bnb-transfer

        权重(IP):

        请求参数:
        Parameter         	Type    	Required	Description

        amount            	DECIMAL 	YES     	
        transferSide      	STRING  	YES     	"TO_UM","FROM_UM"
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PortfolioEndpoints.set_portfolio_bnb_transfer, **to_local(locals()))


    # 更改自动清还合约负余额模式(TRADE)
    def set_portfolio_repay_futures_switch(self,autoRepay:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/portfolio/repay-futures-switch

        权重(IP):

        请求参数:
        Parameter         	Type    	Required	Description

        autoRepay         	STRING  	YES     	默认为true;false代表关闭自动清还合约负余额
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PortfolioEndpoints.set_portfolio_repay_futures_switch, **to_local(locals()))


    # 查询自动清还合约负余额模式(USER_DATA)
    def get_portfolio_repay_futures_switch(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/portfolio/repay-futures-switch

        权重(IP):

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PortfolioEndpoints.get_portfolio_repay_futures_switch, **to_local(locals()))


    # 清还合约负余额(USER_DATA)
    def set_portfolio_repay_futures_negative_balance(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/portfolio/repay-futures-negative-balance

        权重(IP):

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PortfolioEndpoints.set_portfolio_repay_futures_negative_balance, **to_local(locals()))


    # 查询统一账户资产支持杠杆倍数(USER_DATA)
    def get_portfolio_margin_asset_leverage(self,proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/portfolio/margin-asset-leverage

        权重(IP):
        '''
        return self.send_request(*_PortfolioEndpoints.get_portfolio_margin_asset_leverage, **to_local(locals()))