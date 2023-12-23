# 质押借币接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _CryptoLoansEndpoints():


    get_loan_income = ['https://api.binance.com', 'GET', '/sapi/v1/loan/income', True] # 获取质押借币资金流水 (USER_DATA) 
    set_loan_borrow = ['https://api.binance.com', 'POST', '/sapi/v1/loan/borrow', True] # 借币 - 质押借币借贷 (TRADE) 
    get_loan_borrow_history = ['https://api.binance.com', 'GET', '/sapi/v1/loan/borrow/history', True] # 借币 - 查询质押借币历史记录 (USER_DATA) 
    get_loan_ongoing_orders = ['https://api.binance.com', 'GET', '/sapi/v1/loan/ongoing/orders', True] # 借币 - 查询借款中订单列表 (USER_DATA) 
    set_loan_repay = ['https://api.binance.com', 'POST', '/sapi/v1/loan/repay', True] # 还款 - 质押借币还款 (TRADE) 
    get_loan_repay_history = ['https://api.binance.com', 'GET', '/sapi/v1/loan/repay/history', True] # 还款 - 查询还款记录历史 (USER_DATA) 
    set_loan_adjust_ltv = ['https://api.binance.com', 'POST', '/sapi/v1/loan/adjust/ltv', True] # 调整质押率 - 质押借币调整质押率 (TRADE) 
    get_loan_ltv_adjustment_history = ['https://api.binance.com', 'GET', '/sapi/v1/loan/ltv/adjustment/history', True] # 调整质押率 - 查询质押率调整历史 (USER_DATA) 
    get_loan_loanable_data = ['https://api.binance.com', 'GET', '/sapi/v1/loan/loanable/data', True] # 查询可借币种数据 (USER_DATA) 
    get_loan_collateral_data = ['https://api.binance.com', 'GET', '/sapi/v1/loan/collateral/data', True] # 查询抵押币种数据 (USER_DATA) 
    get_loan_repay_collateral_rate = ['https://api.binance.com', 'GET', '/sapi/v1/loan/repay/collateral/rate', True] # 查询抵押币种还款汇率 (USER_DATA) 
    set_loan_customize_margin_call = ['https://api.binance.com', 'POST', '/sapi/v1/loan/customize/margin_call', True] # 质押借币自定义补仓质押率 (TRADE) 
    set_loan_flexible_borrow = ['https://api.binance.com', 'POST', '/sapi/v1/loan/flexible/borrow', True] # 借币 - 活期借币借贷 (TRADE) 
    get_loan_flexible_ongoing_orders = ['https://api.binance.com', 'GET', '/sapi/v1/loan/flexible/ongoing/orders', True] # 借币 - 查询活期借款中订单列表 (USER_DATA) 
    get_loan_flexible_borrow_history = ['https://api.binance.com', 'GET', '/sapi/v1/loan/flexible/borrow/history', True] # 借币 - 查询活期借币历史记录 (USER_DATA) 
    set_loan_flexible_repay = ['https://api.binance.com', 'POST', '/sapi/v1/loan/flexible/repay', True] # 还款 - 活期借币还款 (TRADE) 
    get_loan_flexible_repay_history = ['https://api.binance.com', 'GET', '/sapi/v1/loan/flexible/repay/history', True] # 还款 - 查询活期借币还款记录历史 (USER_DATA) 
    set_loan_flexible_adjust_ltv = ['https://api.binance.com', 'POST', '/sapi/v1/loan/flexible/adjust/ltv', True] # 调整质押率 - 活期借币调整质押率 (TRADE) 
    get_loan_flexible_ltv_adjustment_history = ['https://api.binance.com', 'GET', '/sapi/v1/loan/flexible/ltv/adjustment/history', False] # 调整质押率 - 查询活期借币质押率调整历史 TODO
    get_loan_flexible_loanable_data = ['https://api.binance.com', 'GET', '/sapi/v1/loan/flexible/loanable/data', True] # 查询活期借币可借币种数据 (USER_DATA) 
    get_loan_flexible_collateral_data = ['https://api.binance.com', 'GET', '/sapi/v1/loan/flexible/collateral/data', True] # 查询活期借币抵押币种数据 (USER_DATA)  


class CryptoLoans(Client):

    # 获取质押借币资金流水 (USER_DATA)
    def get_loan_income(self,asset:str = '',type:str = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/loan/income

        权重(UID):6000

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	NO      	
        type              	STRING  	NO      	默认返回所有类型 枚举值：借入borrowIn,抵押金使用collateralSpent, 还款金额repayAmount, 抵押物返还collateralReturn, 增加抵押物addCollateral, 减少抵押物removeCollateral, 强平后返还抵押物collateralReturnAfterLiquidation
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	默认 20, 最大 100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CryptoLoansEndpoints.get_loan_income, **to_local(locals()))


    # 借币 - 质押借币借贷 (TRADE)
    def set_loan_borrow(self,loanCoin:str = '',loanAmount:Union[int,float] = '',collateralCoin:str = '',collateralAmount:Union[int,float] = '',loanTerm:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/loan/borrow

        权重（UID）：36000

        请求参数:
        Parameter         	Type    	Required	Description

        loanCoin          	STRING  	YES     	
        loanAmount        	DECIMAL 	NO      	当collateralAmount为空时，需必填
        collateralCoin    	STRING  	YES     	
        collateralAmount  	DECIMAL 	NO      	当loanAmount为空时，需必填
        loanTerm          	INT     	YES     	7/30 天
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CryptoLoansEndpoints.set_loan_borrow, **to_local(locals()))


    # 借币 - 查询质押借币历史记录 (USER_DATA)
    def get_loan_borrow_history(self,orderId:int = '',loanCoin:str = '',collateralCoin:str = '',startTime:int = '',endTime:int = '',current:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/loan/borrow/history

        权重（IP）：400

        请求参数:
        Parameter         	Type    	Required	Description

        orderId           	LONG    	NO      	POST /sapi/v1/loan/borrow中的 orderId
        loanCoin          	STRING  	NO      	
        collateralCoin    	STRING  	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        current           	LONG    	NO      	当前查询页数，从1开始。默认值：1；最大：1000。
        limit             	LONG    	NO      	默认值：10；最大：100。
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CryptoLoansEndpoints.get_loan_borrow_history, **to_local(locals()))


    # 借币 - 查询借款中订单列表 (USER_DATA)
    def get_loan_ongoing_orders(self,orderId:int = '',loanCoin:str = '',collateralCoin:str = '',current:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/loan/ongoing/orders

        权重（IP）：:300

        请求参数:
        Parameter         	Type    	Required	Description

        orderId           	LONG    	NO      	
        loanCoin          	STRING  	NO      	
        collateralCoin    	STRING  	NO      	
        current           	LONG    	NO      	当前查询页数，从1开始。默认值：1；最大：1000。
        limit             	LONG    	NO      	默认值：10；最大：100。
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CryptoLoansEndpoints.get_loan_ongoing_orders, **to_local(locals()))


    # 还款 - 质押借币还款 (TRADE)
    def set_loan_repay(self,orderId:int = '',amount:Union[int,float] = '',type:int = '',collateralReturn:bool = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/loan/repay

        权重（UID）：6000

        请求参数:
        Parameter         	Type    	Required	Description

        orderId           	LONG    	YES     	
        amount            	DECIMAL 	YES     	
        type              	INT     	NO      	默认值：1。 1：用借贷币还款；2：用抵押币还款。
        collateralReturn  	BOOLEAN 	NO      	默认值：TRUE。TRUE：多余的抵押金退回现货钱包；FALSE: 多余的抵押金保留在原订单里。
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CryptoLoansEndpoints.set_loan_repay, **to_local(locals()))


    # 还款 - 查询还款记录历史 (USER_DATA)
    def get_loan_repay_history(self,orderId:int = '',loanCoin:str = '',collateralCoin:str = '',startTime:int = '',endTime:int = '',current:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/loan/repay/history

        权重（IP）：400

        请求参数:
        Parameter         	Type    	Required	Description

        orderId           	LONG    	NO      	
        loanCoin          	STRING  	NO      	
        collateralCoin    	STRING  	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        current           	LONG    	NO      	当前查询页数，从1开始。默认值：1；最大：1000。
        limit             	LONG    	NO      	默认值：10；最大：100。
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CryptoLoansEndpoints.get_loan_repay_history, **to_local(locals()))


    # 调整质押率 - 质押借币调整质押率 (TRADE)
    def set_loan_adjust_ltv(self,orderId:int = '',amount:Union[int,float] = '',direction:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/loan/adjust/ltv

        权重（UID）：6000

        请求参数:
        Parameter         	Type    	Required	Description

        orderId           	LONG    	YES     	
        amount            	DECIMAL 	YES     	
        direction         	ENUM    	YES     	"ADDITIONAL", "REDUCED"
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CryptoLoansEndpoints.set_loan_adjust_ltv, **to_local(locals()))


    # 调整质押率 - 查询质押率调整历史 (USER_DATA)
    def get_loan_ltv_adjustment_history(self,orderId:int = '',loanCoin:str = '',collateralCoin:str = '',startTime:int = '',endTime:int = '',current:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/loan/ltv/adjustment/history

        权重（IP）：400

        请求参数:
        Parameter         	Type    	Required	Description

        orderId           	LONG    	NO      	
        loanCoin          	STRING  	NO      	
        collateralCoin    	STRING  	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        current           	LONG    	NO      	当前查询页数，从1开始。默认值：1；最大：1000。
        limit             	LONG    	NO      	默认值：10；最大：100。
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CryptoLoansEndpoints.get_loan_ltv_adjustment_history, **to_local(locals()))


    # 查询可借币种数据 (USER_DATA)
    def get_loan_loanable_data(self,loanCoin:str = '',vipLevel:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/loan/loanable/data

        权重（IP）：400

        请求参数:
        Parameter         	Type    	Required	Description

        loanCoin          	STRING  	NO      	
        vipLevel          	INT     	NO      	默认：用户当前VIP登记。如有特殊配置，则填“-1”查询
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CryptoLoansEndpoints.get_loan_loanable_data, **to_local(locals()))


    # 查询抵押币种数据 (USER_DATA)
    def get_loan_collateral_data(self,collateralCoin:str = '',vipLevel:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/loan/collateral/data

        权重（IP）：400

        请求参数:
        Parameter         	Type    	Required	Description

        collateralCoin    	STRING  	NO      	
        vipLevel          	INT     	NO      	默认：用户当前VIP登记。如有特殊配置，则填“-1”查询
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CryptoLoansEndpoints.get_loan_collateral_data, **to_local(locals()))


    # 查询抵押币种还款汇率 (USER_DATA)
    def get_loan_repay_collateral_rate(self,loanCoin:str = '',collateralCoin:str = '',repayAmount:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/loan/repay/collateral/rate

        权重（IP）：6000

        请求参数:
        Parameter         	Type    	Required	Description

        loanCoin          	STRING  	YES     	
        collateralCoin    	STRING  	YES     	
        repayAmount       	DECIMAL 	YES     	以借贷币种为单位的还款金额
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CryptoLoansEndpoints.get_loan_repay_collateral_rate, **to_local(locals()))


    # 质押借币自定义补仓质押率 (TRADE)
    def set_loan_customize_margin_call(self,orderId:int = '',collateralCoin:str = '',marginCall:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/loan/customize/margin_call

        权重（UID）：6000

        请求参数:
        Parameter         	Type    	Required	Description

        orderId           	LONG    	NO      	当collateralCoin为空时，需必填。orderId或collateralCoin只需传一个，如果两个参数同时传，以orderId为准。
        collateralCoin    	STRING  	NO      	当orderID为空时，需必填。orderId或collateralCoin只需传一个，如果两个参数同时传，以orderId为准。
        marginCall        	DECIMAL 	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CryptoLoansEndpoints.set_loan_customize_margin_call, **to_local(locals()))


    # 借币 - 活期借币借贷 (TRADE)
    def set_loan_flexible_borrow(self,loanCoin:str = '',loanAmount:Union[int,float] = '',collateralCoin:str = '',collateralAmount:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/loan/flexible/borrow

        权重(UID):6000

        请求参数:
        Parameter         	Type    	Required	Description

        loanCoin          	STRING  	YES     	
        loanAmount        	DECIMAL 	NO      	当collateralAmount为空时，需必填
        collateralCoin    	STRING  	YES     	
        collateralAmount  	DECIMAL 	NO      	当loanAmount为空时，需必填
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CryptoLoansEndpoints.set_loan_flexible_borrow, **to_local(locals()))


    # 借币 - 查询活期借款中订单列表 (USER_DATA)
    def get_loan_flexible_ongoing_orders(self,loanCoin:str = '',collateralCoin:str = '',current:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/loan/flexible/ongoing/orders

        权重(IP):300

        请求参数:
        Parameter         	Type    	Required	Description

        loanCoin          	STRING  	NO      	
        collateralCoin    	STRING  	NO      	
        current           	LONG    	NO      	当前查询页数，从1开始。默认值：1；最大：1000。
        limit             	LONG    	NO      	默认值：10；最大：100。
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CryptoLoansEndpoints.get_loan_flexible_ongoing_orders, **to_local(locals()))


    # 借币 - 查询活期借币历史记录 (USER_DATA)
    def get_loan_flexible_borrow_history(self,loanCoin:str = '',collateralCoin:str = '',startTime:int = '',endTime:int = '',current:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/loan/flexible/borrow/history

        权重(IP):400

        请求参数:
        Parameter         	Type    	Required	Description

        loanCoin          	STRING  	NO      	
        collateralCoin    	STRING  	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        current           	LONG    	NO      	当前查询页数，从1开始。默认值：1；最大：1000。
        limit             	LONG    	NO      	默认值：10；最大：100。
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CryptoLoansEndpoints.get_loan_flexible_borrow_history, **to_local(locals()))


    # 还款 - 活期借币还款 (TRADE)
    def set_loan_flexible_repay(self,loanCoin:str = '',collateralCoin:Union[int,float] = '',repayAmount:Union[int,float] = '',collateralReturn:bool = '',fullRepayment:bool = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/loan/flexible/repay

        权重(UID):6000

        请求参数:
        Parameter         	Type    	Required	Description

        loanCoin          	STRING  	YES     	
        collateralCoin    	DECIMAL 	YES     	
        repayAmount       	DECIMAL 	YES     	
        collateralReturn  	BOOLEAN 	NO      	默认: TRUE. TRUE: 多余的抵押金退回理财钱包；FALSE: 多余的抵押金保留在原订单里，降低LTV
        fullRepayment     	BOOLEAN 	NO      	默认: FALSE. TRUE: 全部偿还; FALSE: 按照loanAmount金额部分偿还
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CryptoLoansEndpoints.set_loan_flexible_repay, **to_local(locals()))


    # 还款 - 查询活期借币还款记录历史 (USER_DATA)
    def get_loan_flexible_repay_history(self,loanCoin:str = '',collateralCoin:str = '',startTime:int = '',endTime:int = '',current:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/loan/flexible/repay/history

        权重(IP):400

        请求参数:
        Parameter         	Type    	Required	Description

        loanCoin          	STRING  	NO      	
        collateralCoin    	STRING  	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        current           	LONG    	NO      	当前查询页数，从1开始。默认值：1；最大：1000。
        limit             	LONG    	NO      	默认值：10；最大：100。
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CryptoLoansEndpoints.get_loan_flexible_repay_history, **to_local(locals()))


    # 调整质押率 - 活期借币调整质押率 (TRADE)
    def set_loan_flexible_adjust_ltv(self,loanCoin:str = '',collateralCoin:str = '',adjustmentAmount:Union[int,float] = '',direction:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/loan/flexible/adjust/ltv

        权重(UID):6000

        请求参数:
        Parameter         	Type    	Required	Description

        loanCoin          	STRING  	YES     	
        collateralCoin    	STRING  	YES     	
        adjustmentAmount  	DECIMAL 	YES     	
        direction         	ENUM    	YES     	"ADDITIONAL", "REDUCED"
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CryptoLoansEndpoints.set_loan_flexible_adjust_ltv, **to_local(locals()))


    # 调整质押率 - 查询活期借币质押率调整历史
    def get_loan_flexible_ltv_adjustment_history(self,loanCoin:str = '',collateralCoin:str = '',startTime:int = '',endTime:int = '',current:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/loan/flexible/ltv/adjustment/history

        权重(UID):400

        请求参数:
        Parameter         	Type    	Required	Description

        loanCoin          	STRING  	NO      	
        collateralCoin    	STRING  	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        current           	LONG    	NO      	Current querying page. Start from 1; default: 1; max: 1000
        limit             	LONG    	NO      	Default: 10; max: 100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CryptoLoansEndpoints.get_loan_flexible_ltv_adjustment_history, **to_local(locals()))


    # 查询活期借币可借币种数据 (USER_DATA)
    def get_loan_flexible_loanable_data(self,loanCoin:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/loan/flexible/loanable/data

        权重(IP):400

        请求参数:
        Parameter         	Type    	Required	Description

        loanCoin          	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CryptoLoansEndpoints.get_loan_flexible_loanable_data, **to_local(locals()))


    # 查询活期借币抵押币种数据 (USER_DATA)
    def get_loan_flexible_collateral_data(self,collateralCoin:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/loan/flexible/collateral/data

        权重(IP):400

        请求参数:
        Parameter         	Type    	Required	Description

        collateralCoin    	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_CryptoLoansEndpoints.get_loan_flexible_collateral_data, **to_local(locals()))