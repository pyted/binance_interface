# VIP借币接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _VipLoansEndpoints():


    get_loan_vip_ongoing_orders = ['https://api.binance.com', 'GET', '/sapi/v1/loan/vip/ongoing/orders', True] # 查询VIP借币借款中订单 (USER_DATA) 
    set_loan_vip_repay = ['https://api.binance.com', 'POST', '/sapi/v1/loan/vip/repay', True] # VIP借币还款 (TRADE) 
    get_loan_vip_repay_history = ['https://api.binance.com', 'GET', '/sapi/v1/loan/vip/repay/history', True] # 查询VIP借币还款记录历史 (USER_DATA) 
    set_loan_vip_renew = ['https://api.binance.com', 'POST', '/sapi/v1/loan/vip/renew', True] # VIP 借币续期 (TRADE) 
    get_loan_vip_collateral_account = ['https://api.binance.com', 'GET', '/sapi/v1/loan/vip/collateral/account', True] # 查询VIP子账户冻结抵押物金额 (USER_DATA) 
    set_loan_vip_borrow = ['https://api.binance.com', 'POST', '/sapi/v1/loan/vip/borrow', True] # VIP 借币借款 (TRADE) 
    get_loan_vip_loanable_data = ['https://api.binance.com', 'GET', '/sapi/v1/loan/vip/loanable/data', True] # 查询VIP借币可借币种数据(USER_DATA) 
    get_loan_vip_collateral_data = ['https://api.binance.com', 'GET', '/sapi/v1/loan/vip/collateral/data', True] # 查询VIP借币抵押币种数据（USER_DATA） 
    get_loan_vip_request_data = ['https://api.binance.com', 'GET', '/sapi/v1/loan/vip/request/data', True] # 查询申请状态（USER_DATA） 
    get_loan_vip_request_interestRate = ['https://api.binance.com', 'GET', '/sapi/v1/loan/vip/request/interestRate', True] # 查询借款利率（USER_DATA）  


class VipLoans(Client):

    # 查询VIP借币借款中订单 (USER_DATA)
    def get_loan_vip_ongoing_orders(self,orderId:int = '',collateralAccountId:int = '',loanCoin:str = '',collateralCoin:str = '',current:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/loan/vip/ongoing/orders

        权重(IP):400

        请求参数:
        Parameter         	Type    	Required	Description

        orderId           	LONG    	NO      	
        collateralAccountId	LONG    	NO      	
        loanCoin          	STRING  	NO      	
        collateralCoin    	STRING  	NO      	
        current           	LONG    	NO      	当前查询页数，从1开始。默认值：1，最大：1000
        limit             	LONG    	NO      	默认值：10，最大：100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_VipLoansEndpoints.get_loan_vip_ongoing_orders, **to_local(locals()))


    # VIP借币还款 (TRADE)
    def set_loan_vip_repay(self,orderId:int = '',amount:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/loan/vip/repay

        权重(UID):6000

        请求参数:
        Parameter         	Type    	Required	Description

        orderId           	LONG    	YES     	
        amount            	DECIMAL 	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_VipLoansEndpoints.set_loan_vip_repay, **to_local(locals()))


    # 查询VIP借币还款记录历史 (USER_DATA)
    def get_loan_vip_repay_history(self,orderId:int = '',loanCoin:str = '',startTime:int = '',endTime:int = '',current:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/loan/vip/repay/history

        权重(IP):400

        请求参数:
        Parameter         	Type    	Required	Description

        orderId           	LONG    	NO      	
        loanCoin          	STRING  	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        current           	LONG    	NO      	当前查询页数，从1开始。默认值：1，最大：1000
        limit             	LONG    	NO      	默认值：10，最大：100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_VipLoansEndpoints.get_loan_vip_repay_history, **to_local(locals()))


    # VIP 借币续期 (TRADE)
    def set_loan_vip_renew(self,orderId:int = '',loanTerm:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/loan/vip/renew

        权重(UID):6000

        请求参数:
        Parameter         	Type    	Required	Description

        orderId           	LONG    	YES     	
        loanTerm          	INT     	NO      	30/60 天
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_VipLoansEndpoints.set_loan_vip_renew, **to_local(locals()))


    # 查询VIP子账户冻结抵押物金额 (USER_DATA)
    def get_loan_vip_collateral_account(self,orderId:int = '',collateralAccountId:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/loan/vip/collateral/account

        权重(IP):6000

        请求参数:
        Parameter         	Type    	Required	Description

        orderId           	LONG    	NO      	
        collateralAccountId	LONG    	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_VipLoansEndpoints.get_loan_vip_collateral_account, **to_local(locals()))


    # VIP 借币借款 (TRADE)
    def set_loan_vip_borrow(self,loanAccountId:int = '',loanCoin:str = '',loanAmount:Union[int,float] = '',collateralAccountId:str = '',collateralCoin:str = '',isFlexibleRate:bool = '',loanTerm:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/loan/vip/borrow

        权重(UID):6000

        请求参数:
        Parameter         	Type    	Required	Description

        loanAccountId     	LONG    	YES     	
        loanCoin          	STRING  	YES     	
        loanAmount        	DECIMAL 	YES     	
        collateralAccountId	STRING  	YES     	多个用,分割
        collateralCoin    	STRING  	YES     	多个用,分割
        isFlexibleRate    	BOOLEAN 	YES     	
        loanTerm          	INT     	NO      	选择固定利率时此为必填选项；选择浮动利率时选填：30/60 days
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_VipLoansEndpoints.set_loan_vip_borrow, **to_local(locals()))


    # 查询VIP借币可借币种数据(USER_DATA)
    def get_loan_vip_loanable_data(self,loanCoin:str = '',vipLevel:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/loan/vip/loanable/data

        权重(IP):400

        请求参数:
        Parameter         	Type    	Required	Description

        loanCoin          	STRING  	NO      	
        vipLevel          	INT     	NO      	默认值：用户的VIP等级
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_VipLoansEndpoints.get_loan_vip_loanable_data, **to_local(locals()))


    # 查询VIP借币抵押币种数据（USER_DATA）
    def get_loan_vip_collateral_data(self,collateralCoin:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/loan/vip/collateral/data

        权重(IP):400

        请求参数:
        Parameter         	Type    	Required	Description

        collateralCoin    	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_VipLoansEndpoints.get_loan_vip_collateral_data, **to_local(locals()))


    # 查询申请状态（USER_DATA）
    def get_loan_vip_request_data(self,current:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/loan/vip/request/data

        权重(UID):400

        请求参数:
        Parameter         	Type    	Required	Description

        current           	LONG    	NO      	目前查询的页面。从1开始，默认：1，最大：1000
        limit             	LONG    	NO      	默认: 10, 最大: 100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_VipLoansEndpoints.get_loan_vip_request_data, **to_local(locals()))


    # 查询借款利率（USER_DATA）
    def get_loan_vip_request_interestRate(self,loanCoin:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/loan/vip/request/interestRate

        权重(UID):400

        请求参数:
        Parameter         	Type    	Required	Description

        loanCoin          	STRING  	YES     	最多10个币种, 多个用","隔开
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_VipLoansEndpoints.get_loan_vip_request_interestRate, **to_local(locals()))