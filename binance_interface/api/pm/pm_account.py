# 账户信息
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _PMAccountEndpoints():


    get_balance = ['https://papi.binance.com', 'GET', '/papi/v1/balance', True] # 查询账户余额(USER_DATA) 
    get_account = ['https://papi.binance.com', 'GET', '/papi/v1/account', True] # 查询账户信息 (USER_DATA) 
    get_margin_maxBorrowable = ['https://papi.binance.com', 'GET', '/papi/v1/margin/maxBorrowable', True] # 查询账户最大可借贷额度 (USER_DATA) 
    get_margin_maxWithdraw = ['https://papi.binance.com', 'GET', '/papi/v1/margin/maxWithdraw', True] # 查询账户最大可转出额度(USER_DATA) 
    get_um_positionRisk = ['https://papi.binance.com', 'GET', '/papi/v1/um/positionRisk', True] # 用户UM持仓风险(USER_DATA) 
    get_cm_positionRisk = ['https://papi.binance.com', 'GET', '/papi/v1/cm/positionRisk', True] # 用户CM持仓风险(USER_DATA) 
    set_um_leverage = ['https://papi.binance.com', 'POST', '/papi/v1/um/leverage', True] # 调整UM开仓杠杆 (TRADE) 
    set_cm_leverage = ['https://papi.binance.com', 'POST', '/papi/v1/cm/leverage', True] # 调整CM开仓杠杆 (TRADE) 
    set_um_positionSide_dual = ['https://papi.binance.com', 'POST', '/papi/v1/um/positionSide/dual', True] # 更改UM持仓模式(TRADE) 
    set_cm_positionSide_dual = ['https://papi.binance.com', 'POST', '/papi/v1/cm/positionSide/dual', True] # 更改CM持仓模式(TRADE) 
    get_um_positionSide_dual = ['https://papi.binance.com', 'GET', '/papi/v1/um/positionSide/dual', True] # 查询UM持仓模式(USER_DATA) 
    get_cm_positionSide_dual = ['https://papi.binance.com', 'GET', '/papi/v1/cm/positionSide/dual', True] # 查询CM持仓模式(USER_DATA) 
    get_um_userTrades = ['https://papi.binance.com', 'GET', '/papi/v1/um/userTrades', True] # UM账户成交历史 (USER_DATA) 
    get_cm_userTrades = ['https://papi.binance.com', 'GET', '/papi/v1/cm/userTrades', True] # CM账户成交历史 (USER_DATA) 
    get_um_leverageBracket = ['https://papi.binance.com', 'GET', '/papi/v1/um/leverageBracket', True] # 查询UM杠杆分层标准 (USER_DATA) 
    get_cm_leverageBracket = ['https://papi.binance.com', 'GET', '/papi/v1/cm/leverageBracket', True] # 查询CM杠杆分层标准 (USER_DATA) 
    get_margin_forceOrders = ['https://papi.binance.com', 'GET', '/papi/v1/margin/forceOrders', True] # 获取账户杠杆强制平仓记录 (USER_DATA) 
    get_um_forceOrders = ['https://papi.binance.com', 'GET', '/papi/v1/um/forceOrders', True] # 用户强平单历史(USER_DATA) 
    get_cm_forceOrders = ['https://papi.binance.com', 'GET', '/papi/v1/cm/forceOrders', True] # 用户CM强平单历史 (USER_DATA) 
    get_um_apiTradingStatus = ['https://papi.binance.com', 'GET', '/papi/v1/um/apiTradingStatus', True] # 统一账户UM合约交易量化规则指标 (USER_DATA) 
    get_um_commissionRate = ['https://papi.binance.com', 'GET', '/papi/v1/um/commissionRate', True] # 查询用户UM手续费率 (USER_DATA) 
    get_cm_commissionRate = ['https://papi.binance.com', 'GET', '/papi/v1/cm/commissionRate', True] # 查询用户CM手续费率 (USER_DATA) 
    get_margin_marginLoan = ['https://papi.binance.com', 'GET', '/papi/v1/margin/marginLoan', True] # 查询杠杆借贷记录 (USER_DATA) 
    get_margin_repayLoan = ['https://papi.binance.com', 'GET', '/papi/v1/margin/repayLoan', True] # 查询杠杆还贷记录(USER_DATA) 
    get_margin_marginInterestHistory = ['https://papi.binance.com', 'GET', '/papi/v1/margin/marginInterestHistory', True] # 获取杠杆利息历史 (USER_DATA) 
    get_portfolio_interest_history = ['https://papi.binance.com', 'GET', '/papi/v1/portfolio/interest-history', True] # 查询统一账户期货负余额收息历史(USER_DATA) 
    set_auto_collection = ['https://papi.binance.com', 'POST', '/papi/v1/auto-collection', True] # 统一账户资金归集(TRADE) 
    set_asset_collection = ['https://papi.binance.com', 'POST', '/papi/v1/asset-collection', True] # 特定资产资金归集(TRADE) 
    set_bnb_transfer = ['https://papi.binance.com', 'POST', '/papi/v1/bnb-transfer', True] # BNB划转(TRADE) 
    get_um_income = ['https://papi.binance.com', 'GET', '/papi/v1/um/income', True] # 获取UM损益资金流水 (USER_DATA) 
    get_cm_income = ['https://papi.binance.com', 'GET', '/papi/v1/cm/income', True] # 获取CM损益资金流水(USER_DATA) 
    get_um_account = ['https://papi.binance.com', 'GET', '/papi/v1/um/account', True] # 获取UM账户信息 (USER_DATA) 
    get_cm_account = ['https://papi.binance.com', 'GET', '/papi/v1/cm/account', True] # 获取CM账户信息 (USER_DATA) 
    set_repay_futures_switch = ['https://papi.binance.com', 'POST', '/papi/v1/repay-futures-switch', True] # 更改自动清还合约负余额模式(TRADE) 
    get_repay_futures_switch = ['https://papi.binance.com', 'GET', '/papi/v1/repay-futures-switch', True] # 查询自动清还合约负余额模式(USER_DATA) 
    set_repay_futures_negative_balance = ['https://papi.binance.com', 'POST', '/papi/v1/repay-futures-negative-balance', True] # 清还合约负余额(USER_DATA) 
    get_um_adlQuantile = ['https://papi.binance.com', 'GET', '/papi/v1/um/adlQuantile', True] # UM持仓ADL队列估算 (USER_DATA) 
    get_cm_adlQuantile = ['https://papi.binance.com', 'GET', '/papi/v1/cm/adlQuantile', True] # CM持仓ADL队列估算 (USER_DATA)  


class PMAccount(Client):

    # 查询账户余额(USER_DATA)
    def get_balance(self,asset:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/balance

        权重:20

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_balance, **to_local(locals()))


    # 查询账户信息 (USER_DATA)
    def get_account(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/account

        权重:20

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_account, **to_local(locals()))


    # 查询账户最大可借贷额度 (USER_DATA)
    def get_margin_maxBorrowable(self,asset:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/margin/maxBorrowable

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	YES     	
        recvWindow        	LONG    	NO      	赋值不能超过60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_margin_maxBorrowable, **to_local(locals()))


    # 查询账户最大可转出额度(USER_DATA)
    def get_margin_maxWithdraw(self,asset:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/margin/maxWithdraw

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	YES     	
        recvWindow        	LONG    	NO      	赋值不能超过60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_margin_maxWithdraw, **to_local(locals()))


    # 用户UM持仓风险(USER_DATA)
    def get_um_positionRisk(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/um/positionRisk

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_um_positionRisk, **to_local(locals()))


    # 用户CM持仓风险(USER_DATA)
    def get_cm_positionRisk(self,marginAsset:str = '',pair:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/cm/positionRisk

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        marginAsset       	STRING  	NO      	
        pair              	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_cm_positionRisk, **to_local(locals()))


    # 调整UM开仓杠杆 (TRADE)
    def set_um_leverage(self,symbol:str = '',leverage:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /papi/v1/um/leverage

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        leverage          	INT     	YES     	target initial leverage: int from 1 to 125
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.set_um_leverage, **to_local(locals()))


    # 调整CM开仓杠杆 (TRADE)
    def set_cm_leverage(self,symbol:str = '',leverage:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /papi/v1/cm/leverage

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        leverage          	INT     	YES     	target initial leverage: int from 1 to 125
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.set_cm_leverage, **to_local(locals()))


    # 更改UM持仓模式(TRADE)
    def set_um_positionSide_dual(self,dualSidePosition:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /papi/v1/um/positionSide/dual

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        dualSidePosition  	STRING  	YES     	"true": 双向持仓模式；"false": 单向持仓模式
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.set_um_positionSide_dual, **to_local(locals()))


    # 更改CM持仓模式(TRADE)
    def set_cm_positionSide_dual(self,dualSidePosition:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /papi/v1/cm/positionSide/dual

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        dualSidePosition  	STRING  	YES     	"true": 双向持仓模式；"false": 单向持仓模式
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.set_cm_positionSide_dual, **to_local(locals()))


    # 查询UM持仓模式(USER_DATA)
    def get_um_positionSide_dual(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/um/positionSide/dual

        权重:30

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_um_positionSide_dual, **to_local(locals()))


    # 查询CM持仓模式(USER_DATA)
    def get_cm_positionSide_dual(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/cm/positionSide/dual

        权重:30

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_cm_positionSide_dual, **to_local(locals()))


    # UM账户成交历史 (USER_DATA)
    def get_um_userTrades(self,symbol:str = '',startTime:int = '',endTime:int = '',fromId:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/um/userTrades

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	交易对
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        fromId            	LONG    	NO      	返回该fromId及之后的成交，缺省返回最近的成交
        limit             	INT     	NO      	返回的结果集数量 默认值:50 最大值:1000
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_um_userTrades, **to_local(locals()))


    # CM账户成交历史 (USER_DATA)
    def get_cm_userTrades(self,symbol:str = '',pair:str = '',startTime:int = '',endTime:int = '',fromId:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/cm/userTrades

        权重:

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        pair              	STRING  	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        fromId            	LONG    	NO      	返回该fromId及之后的成交,缺省返回最近的成交,仅支持配合symbol使用
        limit             	INT     	NO      	返回的结果集数量 默认值:50 最大值:1000
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_cm_userTrades, **to_local(locals()))


    # 查询UM杠杆分层标准 (USER_DATA)
    def get_um_leverageBracket(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/um/leverageBracket

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_um_leverageBracket, **to_local(locals()))


    # 查询CM杠杆分层标准 (USER_DATA)
    def get_cm_leverageBracket(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/cm/leverageBracket

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_cm_leverageBracket, **to_local(locals()))


    # 获取账户杠杆强制平仓记录 (USER_DATA)
    def get_margin_forceOrders(self,startTime:int = '',endTime:int = '',current:int = '',size:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/margin/forceOrders

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        current           	LONG    	NO      	当前查询页。 开始值 1. 默认:1
        size              	LONG    	NO      	默认:10 最大:100
        recvWindow        	LONG    	NO      	赋值不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_margin_forceOrders, **to_local(locals()))


    # 用户强平单历史(USER_DATA)
    def get_um_forceOrders(self,symbol:str = '',autoCloseType:str = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/um/forceOrders

        权重:带symbol20, 不带symbol50

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        autoCloseType     	ENUM    	NO      	LIQUIDATION: 强平单,ADL: ADL减仓单.
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	默认50；最大100.
        recvWindow        	LONG    	NO      	赋值不能超过 60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_um_forceOrders, **to_local(locals()))


    # 用户CM强平单历史 (USER_DATA)
    def get_cm_forceOrders(self,symbol:str = '',autoCloseType:str = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/cm/forceOrders

        权重:

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        autoCloseType     	ENUM    	NO      	LIQUIDATION: 强平单,ADL: ADL减仓单.
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	默认50；最大100.
        recvWindow        	LONG    	NO      	赋值不能超过 60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_cm_forceOrders, **to_local(locals()))


    # 统一账户UM合约交易量化规则指标 (USER_DATA)
    def get_um_apiTradingStatus(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/um/apiTradingStatus

        权重：1for a single symbol10when the symbol parameter is omitted

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_um_apiTradingStatus, **to_local(locals()))


    # 查询用户UM手续费率 (USER_DATA)
    def get_um_commissionRate(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/um/commissionRate

        权重:20

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_um_commissionRate, **to_local(locals()))


    # 查询用户CM手续费率 (USER_DATA)
    def get_cm_commissionRate(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/cm/commissionRate

        权重:20

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_cm_commissionRate, **to_local(locals()))


    # 查询杠杆借贷记录 (USER_DATA)
    def get_margin_marginLoan(self,asset:str = '',txId:int = '',startTime:int = '',endTime:int = '',current:int = '',size:int = '',archived:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/margin/marginLoan

        权重:10

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	YES     	
        txId              	LONG    	NO      	tranIdinPOST/papi/v1/marginLoan
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        current           	LONG    	NO      	当前查询页。 开始值 1。 默认:1
        size              	LONG    	NO      	Default:10 Max:100
        archived          	STRING  	NO      	默认:false. 查询6个月以前的数据，需要设为true
        recvWindow        	LONG    	NO      	赋值不能超过 60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_margin_marginLoan, **to_local(locals()))


    # 查询杠杆还贷记录(USER_DATA)
    def get_margin_repayLoan(self,asset:str = '',txId:int = '',startTime:int = '',endTime:int = '',current:int = '',size:int = '',archived:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/margin/repayLoan

        权重:10

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	YES     	
        txId              	LONG    	NO      	thetranIdinPOST/papi/v1/repayLoan
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        current           	LONG    	NO      	当前查询页。 开始值 1。 默认:1
        size              	LONG    	NO      	Default:10 Max:100
        archived          	STRING  	NO      	Default:false. Set totruefor archived data from 6 months ago
        recvWindow        	LONG    	NO      	赋值不能超过 60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_margin_repayLoan, **to_local(locals()))


    # 获取杠杆利息历史 (USER_DATA)
    def get_margin_marginInterestHistory(self,asset:str = '',startTime:int = '',endTime:int = '',current:int = '',size:int = '',archived:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/margin/marginInterestHistory

        权重:1

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        current           	LONG    	NO      	当前查询页。 开始值 1. 默认:1
        size              	LONG    	NO      	默认:10 最大:100
        archived          	STRING  	NO      	默认:false. 查询6个月以前的数据，需要设为true
        recvWindow        	LONG    	NO      	赋值不能超过60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_margin_marginInterestHistory, **to_local(locals()))


    # 查询统一账户期货负余额收息历史(USER_DATA)
    def get_portfolio_interest_history(self,asset:str = '',startTime:int = '',endTime:int = '',size:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/portfolio/interest-history

        权重:50

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        size              	LONG    	NO      	Default:10 Max:100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_portfolio_interest_history, **to_local(locals()))


    # 统一账户资金归集(TRADE)
    def set_auto_collection(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /papi/v1/auto-collection

        权重:750

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	赋值不能超过 60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.set_auto_collection, **to_local(locals()))


    # 特定资产资金归集(TRADE)
    def set_asset_collection(self,asset:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /papi/v1/asset-collection

        权重(IP):

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.set_asset_collection, **to_local(locals()))


    # BNB划转(TRADE)
    def set_bnb_transfer(self,amount:Union[int,float] = '',transferSide:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /papi/v1/bnb-transfer

        权重:750

        请求参数:
        Parameter         	Type    	Required	Description

        amount            	DECIMAL 	YES     	
        transferSide      	STRING  	YES     	"TO_UM","FROM_UM"
        recvWindow        	LONG    	NO      	赋值不能超过 60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.set_bnb_transfer, **to_local(locals()))


    # 获取UM损益资金流水 (USER_DATA)
    def get_um_income(self,symbol:str = '',incomeType:str = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/um/income

        权重:30

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        incomeType        	STRING  	NO      	TRANSFER, WELCOME_BONUS, REALIZED_PNL, FUNDING_FEE, COMMISSION, INSURANCE_CLEAR, REFERRAL_KICKBACK, COMMISSION_REBATE, API_REBATE, CONTEST_REWARD, CROSS_COLLATERAL_TRANSFER, OPTIONS_PREMIUM_FEE, OPTIONS_SETTLE_PROFIT, INTERNAL_TRANSFER, AUTO_EXCHANGE, DELIVERED_SETTELMENT, COIN_SWAP_DEPOSIT, COIN_SWAP_WITHDRAW, POSITION_LIMIT_INCREASE_FEE
        startTime         	LONG    	NO      	起始时间
        endTime           	LONG    	NO      	结束时间
        limit             	INT     	NO      	默认 100; 最大 1000
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_um_income, **to_local(locals()))


    # 获取CM损益资金流水(USER_DATA)
    def get_cm_income(self,symbol:str = '',incomeType:str = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/cm/income

        权重:30

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        incomeType        	STRING  	NO      	"TRANSFER","WELCOME_BONUS", "FUNDING_FEE", "REALIZED_PNL", "COMMISSION", "INSURANCE_CLEAR", and "DELIVERED_SETTELMENT"
        startTime         	LONG    	NO      	起始时间
        endTime           	LONG    	NO      	结束时间
        limit             	INT     	NO      	默认 100; 最大 1000
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_cm_income, **to_local(locals()))


    # 获取UM账户信息 (USER_DATA)
    def get_um_account(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/um/account

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_um_account, **to_local(locals()))


    # 获取CM账户信息 (USER_DATA)
    def get_cm_account(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/cm/account

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_cm_account, **to_local(locals()))


    # 更改自动清还合约负余额模式(TRADE)
    def set_repay_futures_switch(self,autoRepay:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /papi/v1/repay-futures-switch

        权重(IP):

        请求参数:
        Parameter         	Type    	Required	Description

        autoRepay         	STRING  	YES     	默认为true;false代表关闭自动清还合约负余额
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.set_repay_futures_switch, **to_local(locals()))


    # 查询自动清还合约负余额模式(USER_DATA)
    def get_repay_futures_switch(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/repay-futures-switch

        权重(IP):

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_repay_futures_switch, **to_local(locals()))


    # 清还合约负余额(USER_DATA)
    def set_repay_futures_negative_balance(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /papi/v1/repay-futures-negative-balance

        权重(IP):

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.set_repay_futures_negative_balance, **to_local(locals()))


    # UM持仓ADL队列估算 (USER_DATA)
    def get_um_adlQuantile(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/um/adlQuantile

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_um_adlQuantile, **to_local(locals()))


    # CM持仓ADL队列估算 (USER_DATA)
    def get_cm_adlQuantile(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /papi/v1/cm/adlQuantile

        权重:5

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_PMAccountEndpoints.get_cm_adlQuantile, **to_local(locals()))