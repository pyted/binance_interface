# 子母账户接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _SubAccountEndpoints():


    set_sub_account_virtualSubAccount = ['https://api.binance.com', 'POST', '/sapi/v1/sub-account/virtualSubAccount', False] # 创建虚拟子账户（适用主账户）
    get_sub_account_list = ['https://api.binance.com', 'GET', '/sapi/v1/sub-account/list', False] # 查询子账户列表（适用主账户）
    get_sub_account_sub_transfer_history = ['https://api.binance.com', 'GET', '/sapi/v1/sub-account/sub/transfer/history', False] # 查询子账户现货资金划转历史 (适用主账户)
    get_sub_account_futures_internalTransfer = ['https://api.binance.com', 'GET', '/sapi/v1/sub-account/futures/internalTransfer', False] # 查询子账户合约资金划转历史 (适用主账户)
    set_sub_account_futures_internalTransfer = ['https://api.binance.com', 'POST', '/sapi/v1/sub-account/futures/internalTransfer', False] # 执行子账户合约资金划转 (适用主账户)
    get_sub_account_assets_v3 = ['https://api.binance.com', 'GET', '/sapi/v3/sub-account/assets', False] # 查询子账户资产 (适用主账户)
    get_sub_account_spotSummary = ['https://api.binance.com', 'GET', '/sapi/v1/sub-account/spotSummary', False] # 查询子账户现货资产汇总 (适用主账户)
    get_capital_deposit_subAddress = ['https://api.binance.com', 'GET', '/sapi/v1/capital/deposit/subAddress', False] # 获取子账户充值地址 (适用主账户)
    get_capital_deposit_subHisrec = ['https://api.binance.com', 'GET', '/sapi/v1/capital/deposit/subHisrec', False] # 获取子账户充值记录 (适用主账户)
    get_sub_account_status = ['https://api.binance.com', 'GET', '/sapi/v1/sub-account/status', False] # 查询子账户Margin/Futures状态 (适用主账户)
    set_sub_account_margin_enable = ['https://api.binance.com', 'POST', '/sapi/v1/sub-account/margin/enable', False] # 为子账户开通Margin (适用主账户)
    get_sub_account_margin_account = ['https://api.binance.com', 'GET', '/sapi/v1/sub-account/margin/account', False] # 查询子账户Margin账户详情 (适用主账户)
    get_sub_account_margin_accountSummary = ['https://api.binance.com', 'GET', '/sapi/v1/sub-account/margin/accountSummary', False] # 查询子账户Margin账户汇总 (适用主账户)
    set_sub_account_futures_enable = ['https://api.binance.com', 'POST', '/sapi/v1/sub-account/futures/enable', False] # 为子账户开通Futures (适用主账户)
    get_sub_account_futures_account_v1 = ['https://api.binance.com', 'GET', '/sapi/v1/sub-account/futures/account', False] # 查询子账户Futures账户详情 (适用主账户)
    get_sub_account_futures_accountSummary_v1 = ['https://api.binance.com', 'GET', '/sapi/v1/sub-account/futures/accountSummary', False] # 查询子账户Futures账户汇总 (适用主账户)
    get_sub_account_futures_positionRisk_v1 = ['https://api.binance.com', 'GET', '/sapi/v1/sub-account/futures/positionRisk', False] # 查询子账户合约持仓信息 (仅适用主账户)
    set_sub_account_futures_transfer = ['https://api.binance.com', 'POST', '/sapi/v1/sub-account/futures/transfer', False] # 子账户Futures划转 (仅适用主账户)
    set_sub_account_margin_transfer = ['https://api.binance.com', 'POST', '/sapi/v1/sub-account/margin/transfer', False] # 子账户Margin划转 (仅适用主账户)
    set_sub_account_transfer_subToSub = ['https://api.binance.com', 'POST', '/sapi/v1/sub-account/transfer/subToSub', False] # 向共同主账户下的子账户主动划转 (仅适用子账户)
    set_sub_account_transfer_subToMaster = ['https://api.binance.com', 'POST', '/sapi/v1/sub-account/transfer/subToMaster', False] # 向主账户主动划转 (仅适用子账户)
    get_sub_account_transfer_subUserHistory = ['https://api.binance.com', 'GET', '/sapi/v1/sub-account/transfer/subUserHistory', False] # 查询子账户划转历史 (仅适用子账户)
    set_sub_account_universalTransfer = ['https://api.binance.com', 'POST', '/sapi/v1/sub-account/universalTransfer', False] # 子母账户万能划转 (适用主账户)
    get_sub_account_universalTransfer = ['https://api.binance.com', 'GET', '/sapi/v1/sub-account/universalTransfer', False] # 查询子母账户万能划转历史 (适用主账户)
    get_sub_account_futures_account = ['https://api.binance.com', 'GET', '/sapi/v2/sub-account/futures/account', False] # 查询子账户Futures账户详情V2 (适用主账户)
    get_sub_account_futures_accountSummary = ['https://api.binance.com', 'GET', '/sapi/v2/sub-account/futures/accountSummary', False] # 查询子账户Futures账户汇总V2 (适用主账户)
    get_sub_account_futures_positionRisk = ['https://api.binance.com', 'GET', '/sapi/v2/sub-account/futures/positionRisk', False] # 查询子账户合约持仓信息V2 (仅适用主账户)
    set_sub_account_blvt_enable = ['https://api.binance.com', 'POST', '/sapi/v1/sub-account/blvt/enable', False] # 为子账户开通杠杆代币 (适用母账户)
    get_sub_account_subAccountApi_ipRestriction = ['https://api.binance.com', 'GET', '/sapi/v1/sub-account/subAccountApi/ipRestriction', False] # 查询子账户API Key IP白名单 (适用母账户)
    cancel_sub_account_subAccountApi_ipRestriction_ipList = ['https://api.binance.com', 'DELETE', '/sapi/v1/sub-account/subAccountApi/ipRestriction/ipList', False] # 删除子账户API Key IP白名单 (适用母账户)
    set_sub_account_subAccountApi_ipRestriction = ['https://api.binance.com', 'POST', '/sapi/v2/sub-account/subAccountApi/ipRestriction', False] # 为子账户API Key增加IP白名单 (适用母账户)
    set_managed_subaccount_deposit = ['https://api.binance.com', 'POST', '/sapi/v1/managed-subaccount/deposit', False] # 投资人账户为托管子账户充值资产 (适用投资人母账户)
    get_managed_subaccount_asset = ['https://api.binance.com', 'GET', '/sapi/v1/managed-subaccount/asset', False] # 投资人账户查询托管子账户资产 (适用投资人母账户)
    set_managed_subaccount_withdraw = ['https://api.binance.com', 'POST', '/sapi/v1/managed-subaccount/withdraw', False] # 投资人账户为托管子账户提币资产 (适用投资人母账户)
    get_managed_subaccount_accountSnapshot = ['https://api.binance.com', 'GET', '/sapi/v1/managed-subaccount/accountSnapshot', False] # 查询托管子账户资产快照 (适用投资人母账户)
    get_managed_subaccount_queryTransLogForInvestor = ['https://api.binance.com', 'GET', '/sapi/v1/managed-subaccount/queryTransLogForInvestor', True] # 查询托管子账户的划转记录(适用投资人母账户) (USER_DATA) 
    get_managed_subaccount_queryTransLogForTradeParent = ['https://api.binance.com', 'GET', '/sapi/v1/managed-subaccount/queryTransLogForTradeParent', True] # 查询托管子账户的划转记录(适用交易团队母账户)(USER_DATA) 
    get_managed_subaccount_fetch_future_asset = ['https://api.binance.com', 'GET', '/sapi/v1/managed-subaccount/fetch-future-asset', True] # 投资人账户查询托管子账户期货资产 (适用投资人母账户) (USER_DATA) 
    get_managed_subaccount_marginAsset = ['https://api.binance.com', 'GET', '/sapi/v1/managed-subaccount/marginAsset', True] # 投资人账户查询托管子账户杠杆资产 (适用投资人母账户) (USER_DATA) 
    get_sub_account_assets = ['https://api.binance.com', 'GET', '/sapi/v4/sub-account/assets', True] # 查询子账户资产(适用主账户)(USER_DATA) 
    get_managed_subaccount_info = ['https://api.binance.com', 'GET', '/sapi/v1/managed-subaccount/info', True] # 查询托管子账户列表 (适用投资人母账户)(USER_DATA) 
    get_sub_account_transaction_statistics = ['https://api.binance.com', 'GET', '/sapi/v1/sub-account/transaction-statistics', True] # 查询子账户交易量统计列表 (适用母账户)(USER_DATA) 
    get_managed_subaccount_deposit_address = ['https://api.binance.com', 'GET', '/sapi/v1/managed-subaccount/deposit/address', True] # 获取托管子账户充值地址 (适用投资人母账户)(USER_DATA) 
    set_sub_account_eoptions_enable = ['https://api.binance.com', 'POST', '/sapi/v1/sub-account/eoptions/enable', True] # 为子账户开通期权(适用主账户)(USER_DATA) 
    get_managed_subaccount_query_trans_log = ['https://api.binance.com', 'GET', '/sapi/v1/managed-subaccount/query-trans-log', True] # 查询托管子账户的划转记录(适用交易团队子账户)(USER_DATA)  


class SubAccount(Client):

    # 创建虚拟子账户（适用主账户）
    def set_sub_account_virtualSubAccount(self,subAccountString:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/sub-account/virtualSubAccount

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        subAccountString  	STRING  	YES     	请输入字符串，我们将为您创建一个虚拟邮箱进行注册
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.set_sub_account_virtualSubAccount, **to_local(locals()))


    # 查询子账户列表（适用主账户）
    def get_sub_account_list(self,email:str = '',isFreeze:str = '',page:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/sub-account/list

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	NO      	Sub-account email
        isFreeze          	STRING  	NO      	true or false
        page              	INT     	NO      	默认: 1
        limit             	INT     	NO      	默认: 1, 最大: 200
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.get_sub_account_list, **to_local(locals()))


    # 查询子账户现货资金划转历史 (适用主账户)
    def get_sub_account_sub_transfer_history(self,fromEmail:str = '',toEmail:str = '',startTime:int = '',endTime:int = '',page:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/sub-account/sub/transfer/history

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        fromEmail         	STRING  	NO      	
        toEmail           	STRING  	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        page              	INT     	NO      	默认: 1
        limit             	INT     	NO      	默认: 500
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.get_sub_account_sub_transfer_history, **to_local(locals()))


    # 查询子账户合约资金划转历史 (适用主账户)
    def get_sub_account_futures_internalTransfer(self,email:str = '',futuresType:int = '',startTime:int = '',endTime:int = '',page:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/sub-account/futures/internalTransfer

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	子账户邮箱备注
        futuresType       	LONG    	YES     	1:USDT合约，2: 币本位合约
        startTime         	LONG    	NO      	默认返回100天内历史记录
        endTime           	LONG    	NO      	默认返回100天内历史记录
        page              	INT     	NO      	默认值: 1
        limit             	INT     	NO      	默认值: 50, 最大值：500
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.get_sub_account_futures_internalTransfer, **to_local(locals()))


    # 执行子账户合约资金划转 (适用主账户)
    def set_sub_account_futures_internalTransfer(self,fromEmail:str = '',toEmail:str = '',futuresType:int = '',asset:str = '',amount:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/sub-account/futures/internalTransfer

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        fromEmail         	STRING  	YES     	发送者邮箱备注
        toEmail           	STRING  	YES     	接收者邮箱备注
        futuresType       	LONG    	YES     	1:USDT合约， 2: 币本位合约
        asset             	STRING  	YES     	
        amount            	DECIMAL 	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.set_sub_account_futures_internalTransfer, **to_local(locals()))


    # 查询子账户资产 (适用主账户)
    def get_sub_account_assets_v3(self,email:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v3/sub-account/assets

        权重(UID):60

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	子账户邮箱备注
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.get_sub_account_assets_v3, **to_local(locals()))


    # 查询子账户现货资产汇总 (适用主账户)
    def get_sub_account_spotSummary(self,email:str = '',page:int = '',size:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/sub-account/spotSummary

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	NO      	子账户邮箱
        page              	LONG    	NO      	分页，默认 1
        size              	LONG    	NO      	单页条目数, 默认 10, 最大 20
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.get_sub_account_spotSummary, **to_local(locals()))


    # 获取子账户充值地址 (适用主账户)
    def get_capital_deposit_subAddress(self,email:str = '',coin:str = '',network:str = '',amount:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/capital/deposit/subAddress

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	子账户邮箱备注
        coin              	STRING  	YES     	
        network           	STRING  	NO      	
        amount            	DECIMAL 	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.get_capital_deposit_subAddress, **to_local(locals()))


    # 获取子账户充值记录 (适用主账户)
    def get_capital_deposit_subHisrec(self,email:str = '',coin:str = '',status:int = '',startTime:int = '',endTime:int = '',limit:int = '',offset:int = '',recvWindow:int = '',timestamp:int = '',txId:str = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/capital/deposit/subHisrec

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	子账户邮箱备注
        coin              	STRING  	NO      	
        status            	INT     	NO      	0(0:pending,6: credited but cannot withdraw,7:Wrong Deposit,8:Waiting User confirm,1:success)
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	
        offset            	INT     	NO      	default:0
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES     	
        txId              	STRING  	NO
        '''
        return self.send_request(*_SubAccountEndpoints.get_capital_deposit_subHisrec, **to_local(locals()))


    # 查询子账户Margin/Futures状态 (适用主账户)
    def get_sub_account_status(self,email:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/sub-account/status

        权重(IP):10

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	NO      	子账户邮箱备注
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.get_sub_account_status, **to_local(locals()))


    # 为子账户开通Margin (适用主账户)
    def set_sub_account_margin_enable(self,email:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/sub-account/margin/enable

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	子账户邮箱备注
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.set_sub_account_margin_enable, **to_local(locals()))


    # 查询子账户Margin账户详情 (适用主账户)
    def get_sub_account_margin_account(self,email:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/sub-account/margin/account

        权重(IP):10

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	子账户邮箱备注
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.get_sub_account_margin_account, **to_local(locals()))


    # 查询子账户Margin账户汇总 (适用主账户)
    def get_sub_account_margin_accountSummary(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/sub-account/margin/accountSummary

        权重(IP):10

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.get_sub_account_margin_accountSummary, **to_local(locals()))


    # 为子账户开通Futures (适用主账户)
    def set_sub_account_futures_enable(self,email:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/sub-account/futures/enable

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	子账户邮箱备注
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.set_sub_account_futures_enable, **to_local(locals()))


    # 查询子账户Futures账户详情 (适用主账户)
    def get_sub_account_futures_account_v1(self,email:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/sub-account/futures/account

        权重(IP):10

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	子账户邮箱备注
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.get_sub_account_futures_account_v1, **to_local(locals()))


    # 查询子账户Futures账户汇总 (适用主账户)
    def get_sub_account_futures_accountSummary_v1(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/sub-account/futures/accountSummary

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.get_sub_account_futures_accountSummary_v1, **to_local(locals()))


    # 查询子账户合约持仓信息 (仅适用主账户)
    def get_sub_account_futures_positionRisk_v1(self,email:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/sub-account/futures/positionRisk

        权重(IP):10

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	子账户邮箱备注
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.get_sub_account_futures_positionRisk_v1, **to_local(locals()))


    # 子账户Futures划转 (仅适用主账户)
    def set_sub_account_futures_transfer(self,email:str = '',asset:str = '',amount:Union[int,float] = '',type:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/sub-account/futures/transfer

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	子账户邮箱备注
        asset             	STRING  	YES     	划转资产, e.g., USDT
        amount            	DECIMAL 	YES     	划转数量
        type              	INT     	YES     	1: 由子账户的现货账户划转至其USDT本位合约账户; 2: 由子账户的USDT本位合约账户划转至其现货账户； 3:由子账户现货账户划转至其COIN本位合约账户；4: 由子账户COIN本位合约账户划转至其现货账户
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.set_sub_account_futures_transfer, **to_local(locals()))


    # 子账户Margin划转 (仅适用主账户)
    def set_sub_account_margin_transfer(self,email:str = '',asset:str = '',amount:Union[int,float] = '',type:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/sub-account/margin/transfer

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	子账户邮箱备注
        asset             	STRING  	YES     	划转资产, e.g., USDT
        amount            	DECIMAL 	YES     	划转数量
        type              	INT     	YES     	1: 由子账户的现货账户划转至其杠杆账户; 2: 由子账户的杠杆账户划转至其现货账户
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.set_sub_account_margin_transfer, **to_local(locals()))


    # 向共同主账户下的子账户主动划转 (仅适用子账户)
    def set_sub_account_transfer_subToSub(self,toEmail:str = '',asset:str = '',amount:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/sub-account/transfer/subToSub

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        toEmail           	STRING  	YES     	接收者子邮箱地址备注
        asset             	STRING  	YES     	
        amount            	DECIMAL 	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.set_sub_account_transfer_subToSub, **to_local(locals()))


    # 向主账户主动划转 (仅适用子账户)
    def set_sub_account_transfer_subToMaster(self,asset:str = '',amount:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/sub-account/transfer/subToMaster

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	YES     	
        amount            	DECIMAL 	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.set_sub_account_transfer_subToMaster, **to_local(locals()))


    # 查询子账户划转历史 (仅适用子账户)
    def get_sub_account_transfer_subUserHistory(self,asset:str = '',type:int = '',startTime:int = '',endTime:int = '',limit:int = '',returnFailHistory:bool = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/sub-account/transfer/subUserHistory

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	NO      	如不提供，返回所有asset 划转记录
        type              	INT     	NO      	1: transfer in, 2: transfer out; 如不提供，返回transfer out方向划转记录
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	默认值: 500
        returnFailHistory 	BOOLEAN 	NO      	默认False，返回PROCESS和SUCCESS状态的数据；如果传True返回PROCESS、SUCCESS、FAILURE状态的数据
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.get_sub_account_transfer_subUserHistory, **to_local(locals()))


    # 子母账户万能划转 (适用主账户)
    def set_sub_account_universalTransfer(self,fromEmail:str = '',toEmail:str = '',fromAccountType:str = '',toAccountType:str = '',clientTranId:str = '',symbol:str = '',asset:str = '',amount:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/sub-account/universalTransfer

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        fromEmail         	STRING  	NO      	
        toEmail           	STRING  	NO      	
        fromAccountType   	STRING  	YES     	"SPOT","USDT_FUTURE","COIN_FUTURE","MARGIN"(Cross),"ISOLATED_MARGIN"
        toAccountType     	STRING  	YES     	"SPOT","USDT_FUTURE","COIN_FUTURE","MARGIN"(Cross),"ISOLATED_MARGIN"
        clientTranId      	STRING  	NO      	不可重复
        symbol            	STRING  	NO      	仅在ISOLATED_MARGIN类型下使用
        asset             	STRING  	YES     	
        amount            	DECIMAL 	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.set_sub_account_universalTransfer, **to_local(locals()))


    # 查询子母账户万能划转历史 (适用主账户)
    def get_sub_account_universalTransfer(self,fromEmail:str = '',toEmail:str = '',clientTranId:str = '',startTime:int = '',endTime:int = '',page:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/sub-account/universalTransfer

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        fromEmail         	STRING  	NO      	
        toEmail           	STRING  	NO      	
        clientTranId      	STRING  	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        page              	INT     	NO      	默认 1
        limit             	INT     	NO      	默认 500, 最大 500
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.get_sub_account_universalTransfer, **to_local(locals()))


    # 查询子账户Futures账户详情V2 (适用主账户)
    def get_sub_account_futures_account(self,email:str = '',futuresType:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v2/sub-account/futures/account

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	子账户邮箱备注
        futuresType       	INT     	YES     	1:USDT Margined Futures, 2:COIN Margined Futures
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.get_sub_account_futures_account, **to_local(locals()))


    # 查询子账户Futures账户汇总V2 (适用主账户)
    def get_sub_account_futures_accountSummary(self,futuresType:int = '',page:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v2/sub-account/futures/accountSummary

        权重(IP):10

        请求参数:
        Parameter         	Type    	Required	Description

        futuresType       	INT     	YES     	1:USDT Margined Futures, 2:COIN Margined Futures
        page              	INT     	NO      	default:1
        limit             	INT     	NO      	default:10, max:20
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.get_sub_account_futures_accountSummary, **to_local(locals()))


    # 查询子账户合约持仓信息V2 (仅适用主账户)
    def get_sub_account_futures_positionRisk(self,email:str = '',futuresType:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v2/sub-account/futures/positionRisk

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	子账户邮箱备注
        futuresType       	INT     	YES     	1:USDT Margined Futures, 2:COIN Margined Futures
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.get_sub_account_futures_positionRisk, **to_local(locals()))


    # 为子账户开通杠杆代币 (适用母账户)
    def set_sub_account_blvt_enable(self,email:str = '',enableBlvt:bool = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/sub-account/blvt/enable

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	Sub-account email
        enableBlvt        	BOOLEAN 	YES     	Only true for now
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.set_sub_account_blvt_enable, **to_local(locals()))


    # 查询子账户API Key IP白名单 (适用母账户)
    def get_sub_account_subAccountApi_ipRestriction(self,email:str = '',subAccountApiKey:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/sub-account/subAccountApi/ipRestriction

        权重(UID):3000

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	Sub-account email
        subAccountApiKey  	STRING  	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.get_sub_account_subAccountApi_ipRestriction, **to_local(locals()))


    # 删除子账户API Key IP白名单 (适用母账户)
    def cancel_sub_account_subAccountApi_ipRestriction_ipList(self,email:str = '',subAccountApiKey:str = '',ipAddress:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        DELETE /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList

        权重(UID):3000

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	Sub-account email
        subAccountApiKey  	STRING  	YES     	
        ipAddress         	STRING  	NO      	可批量删除，用逗号分隔
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.cancel_sub_account_subAccountApi_ipRestriction_ipList, **to_local(locals()))


    # 为子账户API Key增加IP白名单 (适用母账户)
    def set_sub_account_subAccountApi_ipRestriction(self,email:str = '',subAccountApiKey:str = '',status:str = '',ipAddress:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v2/sub-account/subAccountApi/ipRestriction

        权重(UID):3000

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	Sub-account email
        subAccountApiKey  	STRING  	YES     	
        status            	STRING  	YES     	IP限制状态。1或不填入(null) = IP未受限。2 = 仅限受信任IP访问。
        ipAddress         	STRING  	NO      	可批量填入IP，以逗号区隔
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.set_sub_account_subAccountApi_ipRestriction, **to_local(locals()))


    # 投资人账户为托管子账户充值资产 (适用投资人母账户)
    def set_managed_subaccount_deposit(self,toEmail:str = '',asset:str = '',amount:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/managed-subaccount/deposit

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        toEmail           	STRING  	YES     	
        asset             	STRING  	YES     	
        amount            	DECIMAL 	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.set_managed_subaccount_deposit, **to_local(locals()))


    # 投资人账户查询托管子账户资产 (适用投资人母账户)
    def get_managed_subaccount_asset(self,email:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/managed-subaccount/asset

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.get_managed_subaccount_asset, **to_local(locals()))


    # 投资人账户为托管子账户提币资产 (适用投资人母账户)
    def set_managed_subaccount_withdraw(self,fromEmail:str = '',asset:str = '',amount:Union[int,float] = '',transferDate:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/managed-subaccount/withdraw

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        fromEmail         	STRING  	YES     	
        asset             	STRING  	YES     	
        amount            	DECIMAL 	YES     	
        transferDate      	LONG    	NO      	提币会自动发生在选择的日期(UTC0)，如果没有选择日期，提币会立即生效
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.set_managed_subaccount_withdraw, **to_local(locals()))


    # 查询托管子账户资产快照 (适用投资人母账户)
    def get_managed_subaccount_accountSnapshot(self,email:str = '',type:str = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/managed-subaccount/accountSnapshot

        权重(IP):2400

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	
        type              	STRING  	YES     	"SPOT"（现货）, "MARGIN"（全仓）, "FUTURES"（U本位合约）
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	min 7, max 30, default 7
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.get_managed_subaccount_accountSnapshot, **to_local(locals()))


    # 查询托管子账户的划转记录(适用投资人母账户) (USER_DATA)
    def get_managed_subaccount_queryTransLogForInvestor(self,email:str = '',startTime:int = '',endTime:int = '',page:int = '',limit:int = '',transfers:str = '',transferFunctionAccountType:str = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/managed-subaccount/queryTransLogForInvestor

        权重(UID):60

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	托管子账户邮箱
        startTime         	LONG    	YES     	开始时间
        endTime           	LONG    	YES     	结束时间(开始时间结束时间间隔不能超过半年)
        page              	INT     	YES     	页数
        limit             	INT     	YES     	每页数量 (最大值: 500)
        transfers         	STRING  	NO      	划转方向 (from/to)
        transferFunctionAccountType	STRING  	NO      	划转账户类型 (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE)
        '''
        return self.send_request(*_SubAccountEndpoints.get_managed_subaccount_queryTransLogForInvestor, **to_local(locals()))


    # 查询托管子账户的划转记录(适用交易团队母账户)(USER_DATA)
    def get_managed_subaccount_queryTransLogForTradeParent(self,email:str = '',startTime:int = '',endTime:int = '',page:int = '',limit:int = '',transfers:str = '',transferFunctionAccountType:str = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/managed-subaccount/queryTransLogForTradeParent

        权重(UID):60

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	托管子账户邮箱
        startTime         	LONG    	YES     	开始时间
        endTime           	LONG    	YES     	结束时间(开始时间结束时间间隔不能超过半年)
        page              	INT     	YES     	页数
        limit             	INT     	YES     	每页数量 (最大值: 500)
        transfers         	STRING  	NO      	划转方向 (FROM/TO)
        transferFunctionAccountType	STRING  	NO      	划转账户类型 (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE)
        '''
        return self.send_request(*_SubAccountEndpoints.get_managed_subaccount_queryTransLogForTradeParent, **to_local(locals()))


    # 投资人账户查询托管子账户期货资产 (适用投资人母账户) (USER_DATA)
    def get_managed_subaccount_fetch_future_asset(self,email:str = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/managed-subaccount/fetch-future-asset

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	托管子账户邮箱
        '''
        return self.send_request(*_SubAccountEndpoints.get_managed_subaccount_fetch_future_asset, **to_local(locals()))


    # 投资人账户查询托管子账户杠杆资产 (适用投资人母账户) (USER_DATA)
    def get_managed_subaccount_marginAsset(self,email:str = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/managed-subaccount/marginAsset

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	托管子账户邮箱
        '''
        return self.send_request(*_SubAccountEndpoints.get_managed_subaccount_marginAsset, **to_local(locals()))


    # 查询子账户资产(适用主账户)(USER_DATA)
    def get_sub_account_assets(self,email:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v4/sub-account/assets

        权重(UID):60

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	托管子账户邮箱
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.get_sub_account_assets, **to_local(locals()))


    # 查询托管子账户列表 (适用投资人母账户)(USER_DATA)
    def get_managed_subaccount_info(self,email:str = '',page:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/managed-subaccount/info

        权重(UID):60

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	NO      	托管子账户邮箱
        page              	INT     	NO      	默认值: 1
        limit             	INT     	NO      	默认值: 20, 最大值: 20
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.get_managed_subaccount_info, **to_local(locals()))


    # 查询子账户交易量统计列表 (适用母账户)(USER_DATA)
    def get_sub_account_transaction_statistics(self,email:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/sub-account/transaction-statistics

        权重(UID):60

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	Yes     	子账户邮箱
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.get_sub_account_transaction_statistics, **to_local(locals()))


    # 获取托管子账户充值地址 (适用投资人母账户)(USER_DATA)
    def get_managed_subaccount_deposit_address(self,email:str = '',coin:str = '',network:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/managed-subaccount/deposit/address

        权重(UID):1

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	托管子账户邮箱
        coin              	STRING  	YES     	
        network           	STRING  	NO      	网络可以在GET /sapi/v1/capital/deposit/address获取
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.get_managed_subaccount_deposit_address, **to_local(locals()))


    # 为子账户开通期权(适用主账户)(USER_DATA)
    def set_sub_account_eoptions_enable(self,email:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/sub-account/eoptions/enable

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	托管子账户邮箱
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.set_sub_account_eoptions_enable, **to_local(locals()))


    # 查询托管子账户的划转记录(适用交易团队子账户)(USER_DATA)
    def get_managed_subaccount_query_trans_log(self,startTime:int = '',endTime:int = '',page:int = '',limit:int = '',transfers:str = '',transferFunctionAccountType:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/managed-subaccount/query-trans-log

        权重(UID):60

        请求参数:
        Parameter         	Type    	Required	Description

        startTime         	LONG    	YES     	开始时间
        endTime           	LONG    	YES     	结束时间(开始时间结束时间间隔不能超过半年)
        page              	INT     	YES     	页数
        limit             	INT     	YES     	每页数量 (最大值: 500)
        transfers         	STRING  	NO      	划转方向 (FROM/TO)
        transferFunctionAccountType	STRING  	NO      	划转账户类型 (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE)
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_SubAccountEndpoints.get_managed_subaccount_query_trans_log, **to_local(locals()))