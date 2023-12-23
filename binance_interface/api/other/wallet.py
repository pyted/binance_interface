# 钱包接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _WalletEndpoints():


    get_system_status = ['https://api.binance.com', 'GET', '/sapi/v1/system/status', False] # 系统状态(System)
    get_capital_config_getall = ['https://api.binance.com', 'GET', '/sapi/v1/capital/config/getall', True] # 获取所有币信息 (USER_DATA) 
    get_accountSnapshot = ['https://api.binance.com', 'GET', '/sapi/v1/accountSnapshot', True] # 查询每日资产快照 (USER_DATA) 
    set_account_disableFastWithdrawSwitch = ['https://api.binance.com', 'POST', '/sapi/v1/account/disableFastWithdrawSwitch', True] # 关闭站内划转 (USER_DATA) 
    set_account_enableFastWithdrawSwitch = ['https://api.binance.com', 'POST', '/sapi/v1/account/enableFastWithdrawSwitch', True] # 开启站内划转 (USER_DATA) 
    set_capital_withdraw_apply = ['https://api.binance.com', 'POST', '/sapi/v1/capital/withdraw/apply', True] # 提币 (USER_DATA) 
    get_capital_deposit_hisrec = ['https://api.binance.com', 'GET', '/sapi/v1/capital/deposit/hisrec', True] # 获取充值历史(支持多网络) (USER_DATA) 
    get_capital_withdraw_history = ['https://api.binance.com', 'GET', '/sapi/v1/capital/withdraw/history', True] # 获取提币历史 (支持多网络)  (USER_DATA) 
    get_capital_deposit_address = ['https://api.binance.com', 'GET', '/sapi/v1/capital/deposit/address', True] # 获取充值地址 (支持多网络) (USER_DATA) 
    get_account_status = ['https://api.binance.com', 'GET', '/sapi/v1/account/status', True] # 账户状态 (USER_DATA) 
    get_account_apiTradingStatus = ['https://api.binance.com', 'GET', '/sapi/v1/account/apiTradingStatus', True] # 账户API交易状态(USER_DATA) 
    get_asset_dribblet = ['https://api.binance.com', 'GET', '/sapi/v1/asset/dribblet', True] # 小额资产转换BNB历史 (USER_DATA) 
    set_asset_dust_btc = ['https://api.binance.com', 'POST', '/sapi/v1/asset/dust-btc', True] # 获取可以转换成BNB的小额资产 (USER_DATA) 
    set_asset_dust = ['https://api.binance.com', 'POST', '/sapi/v1/asset/dust', True] # 小额资产转换 (USER_DATA) 
    get_asset_assetDividend = ['https://api.binance.com', 'GET', '/sapi/v1/asset/assetDividend', True] # 资产利息记录 (USER_DATA) 
    get_asset_assetDetail = ['https://api.binance.com', 'GET', '/sapi/v1/asset/assetDetail', True] # 上架资产详情 (USER_DATA) 
    get_asset_tradeFee = ['https://api.binance.com', 'GET', '/sapi/v1/asset/tradeFee', True] # 交易手续费率查询 (USER_DATA) 
    set_asset_transfer = ['https://api.binance.com', 'POST', '/sapi/v1/asset/transfer', True] # 用户万向划转 (USER_DATA) 
    get_asset_transfer = ['https://api.binance.com', 'GET', '/sapi/v1/asset/transfer', True] # 查询用户万向划转历史 (USER_DATA) 
    set_asset_get_funding_asset = ['https://api.binance.com', 'POST', '/sapi/v1/asset/get-funding-asset', True] # 资金账户 (USER_DATA) 
    set_asset_getUserAsset = ['https://api.binance.com', 'POST', '/sapi/v3/asset/getUserAsset', True] # 用户持仓 (USER_DATA) 
    set_asset_convert_transfer = ['https://api.binance.com', 'POST', '/sapi/v1/asset/convert-transfer', True] # 稳定币自动兑换划转 (TRADE) 
    get_asset_convert_transfer_queryByPage = ['https://api.binance.com', 'GET', '/sapi/v1/asset/convert-transfer/queryByPage', True] # 稳定币自动兑换划转查询 (USER_DATA) 
    get_asset_ledger_transfer_cloud_mining_queryByPage = ['https://api.binance.com', 'GET', '/sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage', True] # 云算力历史记录分页查询 (USER_DATA) 
    get_account_apiRestrictions = ['https://api.binance.com', 'GET', '/sapi/v1/account/apiRestrictions', True] # 查询用户API Key权限 (USER_DATA) 
    get_capital_contract_convertible_coins = ['https://api.binance.com', 'GET', '/sapi/v1/capital/contract/convertible-coins', True] # 查询用户稳定币与 BUSD 互相转换的设置 (USER_DATA)【TODO 没有找到Table】 
    set_capital_contract_convertible_coins = ['https://api.binance.com', 'POST', '/sapi/v1/capital/contract/convertible-coins', True] # 修改哪些稳定币可与 BUSD 互相转换(USER_DATA) 
    set_capital_deposit_credit_apply = ['https://api.binance.com', 'POST', '/sapi/v1/capital/deposit/credit-apply', True] # 一键上账 (充值到过期地址) (USER_DATA) 
    get_capital_deposit_address_list = ['https://api.binance.com', 'GET', '/sapi/v1/capital/deposit/address/list', True] # 查询充值地址列表(USER_DATA) 
    get_asset_wallet_balance = ['https://api.binance.com', 'GET', '/sapi/v1/asset/wallet/balance', True] # 查询用户钱包余额 (USER_DATA) 
    get_asset_custody_transfer_history = ['https://api.binance.com', 'GET', '/sapi/v1/asset/custody/transfer-history', True] # 查询用户委托资金历史(适用主账户)(USER_DATA)  


class Wallet(Client):

    # 系统状态(System)
    def get_system_status(self,proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/system/status

        权重(IP):1
        '''
        return self.send_request(*_WalletEndpoints.get_system_status, **to_local(locals()))


    # 获取所有币信息 (USER_DATA)
    def get_capital_config_getall(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/capital/config/getall

        权重(IP):10

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_WalletEndpoints.get_capital_config_getall, **to_local(locals()))


    # 查询每日资产快照 (USER_DATA)
    def get_accountSnapshot(self,type:str = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/accountSnapshot

        权重(IP):2400

        请求参数:
        Parameter         	Type    	Required	Description

        type              	STRING  	YES     	"SPOT", "MARGIN", "FUTURES"
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	min 7, max 30, default 7
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_WalletEndpoints.get_accountSnapshot, **to_local(locals()))


    # 关闭站内划转 (USER_DATA)
    def set_account_disableFastWithdrawSwitch(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/account/disableFastWithdrawSwitch

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_WalletEndpoints.set_account_disableFastWithdrawSwitch, **to_local(locals()))


    # 开启站内划转 (USER_DATA)
    def set_account_enableFastWithdrawSwitch(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/account/enableFastWithdrawSwitch

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_WalletEndpoints.set_account_enableFastWithdrawSwitch, **to_local(locals()))


    # 提币 (USER_DATA)
    def set_capital_withdraw_apply(self,coin:str = '',withdrawOrderId:str = '',network:str = '',address:str = '',addressTag:str = '',amount:Union[int,float] = '',transactionFeeFlag:bool = '',name:str = '',walletType:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/capital/withdraw/apply

        权重(UID):600

        请求参数:
        Parameter         	Type    	Required	Description

        coin              	STRING  	YES     	
        withdrawOrderId   	STRING  	NO      	自定义提币ID
        network           	STRING  	NO      	提币网络
        address           	STRING  	YES     	提币地址
        addressTag        	STRING  	NO      	某些币种例如 XRP,XMR 允许填写次级地址标签
        amount            	DECIMAL 	YES     	数量
        transactionFeeFlag	BOOLEAN 	NO      	当站内转账时免手续费,true: 手续费归资金转入方;false: 手续费归资金转出方; . 默认false.
        name              	STRING  	NO      	地址的备注，填写该参数后会加入该币种的提现地址簿。地址簿上限为20，超出后会造成提现失败。地址中的空格需要encode成%20
        walletType        	INTEGER 	NO      	表示出金使用的钱包，0为现货钱包，1为资金钱包。默认walletType为"充币账户"是您设置在钱包->现货账户或资金账户->充值。
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_WalletEndpoints.set_capital_withdraw_apply, **to_local(locals()))


    # 获取充值历史(支持多网络) (USER_DATA)
    def get_capital_deposit_hisrec(self,includeSource:bool = '',coin:str = '',status:int = '',startTime:int = '',endTime:int = '',offset:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',txId:str = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/capital/deposit/hisrec

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        includeSource     	Boolean 	NO      	默认false，如果为true时会返回sourceAddress字段
        coin              	STRING  	NO      	
        status            	INT     	NO      	0(0:pending,6: credited but cannot withdraw,7=Wrong Deposit,8=Waiting User confirm,1:success)
        startTime         	LONG    	NO      	默认当前时间90天前的时间戳
        endTime           	LONG    	NO      	默认当前时间戳
        offset            	INT     	NO      	默认:0
        limit             	INT     	NO      	默认：1000，最大1000
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES     	
        txId              	STRING  	NO
        '''
        return self.send_request(*_WalletEndpoints.get_capital_deposit_hisrec, **to_local(locals()))


    # 获取提币历史 (支持多网络)  (USER_DATA)
    def get_capital_withdraw_history(self,coin:str = '',withdrawOrderId:str = '',status:int = '',offset:int = '',limit:int = '',startTime:int = '',endTime:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/capital/withdraw/history

        权重(UID):18000

        请求参数:
        Parameter         	Type    	Required	Description

        coin              	STRING  	NO      	
        withdrawOrderId   	STRING  	NO      	
        status            	INT     	NO      	0(0:已发送确认Email,1:已被用户取消 2:等待确认 3:被拒绝 4:处理中 5:提现交易失败 6 提现完成)
        offset            	INT     	NO      	
        limit             	INT     	NO      	默认：1000， 最大：1000
        startTime         	LONG    	NO      	默认当前时间90天前的时间戳
        endTime           	LONG    	NO      	默认当前时间戳
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_WalletEndpoints.get_capital_withdraw_history, **to_local(locals()))


    # 获取充值地址 (支持多网络) (USER_DATA)
    def get_capital_deposit_address(self,coin:str = '',network:str = '',amount:Union[int,float] = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/capital/deposit/address

        权重(IP):10

        请求参数:
        Parameter         	Type    	Required	Description

        coin              	STRING  	YES     	
        network           	STRING  	NO      	
        amount            	DECIMAL 	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_WalletEndpoints.get_capital_deposit_address, **to_local(locals()))


    # 账户状态 (USER_DATA)
    def get_account_status(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/account/status

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_WalletEndpoints.get_account_status, **to_local(locals()))


    # 账户API交易状态(USER_DATA)
    def get_account_apiTradingStatus(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/account/apiTradingStatus

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_WalletEndpoints.get_account_apiTradingStatus, **to_local(locals()))


    # 小额资产转换BNB历史 (USER_DATA)
    def get_asset_dribblet(self,startTime:int = '',endTime:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/asset/dribblet

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_WalletEndpoints.get_asset_dribblet, **to_local(locals()))


    # 获取可以转换成BNB的小额资产 (USER_DATA)
    def set_asset_dust_btc(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/asset/dust-btc

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_WalletEndpoints.set_asset_dust_btc, **to_local(locals()))


    # 小额资产转换 (USER_DATA)
    def set_asset_dust(self,asset:list = [],recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/asset/dust

        权重(UID):10

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	ARRAY   	YES     	正在转换的资产。 例如：asset=BTC,USDT
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_WalletEndpoints.set_asset_dust, **to_local(locals()))


    # 资产利息记录 (USER_DATA)
    def get_asset_assetDividend(self,asset:str = '',startTime:int = '',endTime:int = '',limit:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/asset/assetDividend

        权重(IP):10

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	NO      	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        limit             	INT     	NO      	Default 20, max 500
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_WalletEndpoints.get_asset_assetDividend, **to_local(locals()))


    # 上架资产详情 (USER_DATA)
    def get_asset_assetDetail(self,asset:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/asset/assetDetail

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_WalletEndpoints.get_asset_assetDetail, **to_local(locals()))


    # 交易手续费率查询 (USER_DATA)
    def get_asset_tradeFee(self,symbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/asset/tradeFee

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        symbol            	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_WalletEndpoints.get_asset_tradeFee, **to_local(locals()))


    # 用户万向划转 (USER_DATA)
    def set_asset_transfer(self,type:str = '',asset:str = '',amount:Union[int,float] = '',fromSymbol:str = '',toSymbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/asset/transfer

        权重(UID)):900

        请求参数:
        Parameter         	Type    	Required	Description

        type              	ENUM    	YES     	
        asset             	STRING  	YES     	
        amount            	DECIMAL 	YES     	
        fromSymbol        	STRING  	NO      	
        toSymbol          	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_WalletEndpoints.set_asset_transfer, **to_local(locals()))


    # 查询用户万向划转历史 (USER_DATA)
    def get_asset_transfer(self,type:str = '',startTime:int = '',endTime:int = '',current:int = '',size:int = '',fromSymbol:str = '',toSymbol:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/asset/transfer

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        type              	ENUM    	YES     	
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        current           	INT     	NO      	默认 1
        size              	INT     	NO      	默认 10, 最大 100
        fromSymbol        	STRING  	NO      	
        toSymbol          	STRING  	NO      	
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_WalletEndpoints.get_asset_transfer, **to_local(locals()))


    # 资金账户 (USER_DATA)
    def set_asset_get_funding_asset(self,asset:str = '',needBtcValuation:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/asset/get-funding-asset

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	NO      	
        needBtcValuation  	STRING  	NO      	true or false
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_WalletEndpoints.set_asset_get_funding_asset, **to_local(locals()))


    # 用户持仓 (USER_DATA)
    def set_asset_getUserAsset(self,asset:str = '',needBtcValuation:bool = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v3/asset/getUserAsset

        权重(IP):5

        请求参数:
        Parameter         	Type    	Required	Description

        asset             	STRING  	NO      	如果资产为空，则查询用户所有的正资产。
        needBtcValuation  	BOOLEAN 	NO      	是否需要返回兑换成BTC的估值
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_WalletEndpoints.set_asset_getUserAsset, **to_local(locals()))


    # 稳定币自动兑换划转 (TRADE)
    def set_asset_convert_transfer(self,clientTranId:str = '',asset:str = '',amount:Union[int,float] = '',targetAsset:str = '',accountType:str = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/asset/convert-transfer

        权重(UID):5

        请求参数:
        Parameter         	Type    	Required	Description

        clientTranId      	STRING  	YES     	用户自定义流水号，唯一标志，限制最短长度为20
        asset             	STRING  	YES     	当前资产
        amount            	BigDecimal	YES     	数量必须为正数
        targetAsset       	String  	YES     	目标资产
        accountType       	String  	NO      	仅支持MAIN和CARD，如果为空，默认查询主账户MAIN
        '''
        return self.send_request(*_WalletEndpoints.set_asset_convert_transfer, **to_local(locals()))


    # 稳定币自动兑换划转查询 (USER_DATA)
    def get_asset_convert_transfer_queryByPage(self,tranId:int = '',clientTranId:str = '',asset:str = '',startTime:int = '',endTime:int = '',accountType:str = '',current:int = '',size:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/asset/convert-transfer/queryByPage

        权重(UID):5

        请求参数:
        Parameter         	Type    	Required	Description

        tranId            	LONG    	NO      	流水号
        clientTranId      	STRING  	NO      	用户自定义流水号
        asset             	STRING  	NO      	不传或者空字符串查全部, 匹配扣除币种和目标币种
        startTime         	LONG    	YES     	开始时间（包含），单位：毫秒
        endTime           	LONG    	YES     	结束时间（不包含），单位：毫秒
        accountType       	STRING  	NO      	账户类型: MAIN-主账户。CARD-资金账户。如果传入则仅返回对应wallet的记录，不传或者传null则返回该用户spot和card钱包的记录。
        current           	INTEGER 	NO      	当前页面，默认1，最小值为1
        size              	INTEGER 	NO      	页面大小，默认10，最大值为100
        '''
        return self.send_request(*_WalletEndpoints.get_asset_convert_transfer_queryByPage, **to_local(locals()))


    # 云算力历史记录分页查询 (USER_DATA)
    def get_asset_ledger_transfer_cloud_mining_queryByPage(self,tranId:int = '',clientTranId:str = '',asset:str = '',startTime:int = '',endTime:int = '',current:int = '',size:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage

        权重(UID):600

        请求参数:
        Parameter         	Type    	Required	Description

        tranId            	LONG    	NO      	流水号
        clientTranId      	STRING  	NO      	外部唯一流水号
        asset             	STRING  	NO      	不传或者空字符串查全部
        startTime         	LONG    	YES     	开始时间（包含），单位：毫秒
        endTime           	LONG    	YES     	结束时间（不包含），单位：毫秒
        current           	INTEGER 	NO      	当前页面，默认1，最小值为1
        size              	INTEGER 	NO      	页面大小，默认10，最大值为100
        '''
        return self.send_request(*_WalletEndpoints.get_asset_ledger_transfer_cloud_mining_queryByPage, **to_local(locals()))


    # 查询用户API Key权限 (USER_DATA)
    def get_account_apiRestrictions(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/account/apiRestrictions

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_WalletEndpoints.get_account_apiRestrictions, **to_local(locals()))


    # 查询用户稳定币与 BUSD 互相转换的设置 (USER_DATA)【TODO 没有找到Table】
    def get_capital_contract_convertible_coins(self,proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/capital/contract/convertible-coins

        权重(UID):600

        
        '''
        return self.send_request(*_WalletEndpoints.get_capital_contract_convertible_coins, **to_local(locals()))


    # 修改哪些稳定币可与 BUSD 互相转换(USER_DATA)
    def set_capital_contract_convertible_coins(self,coin:str = '',enable:bool = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/capital/contract/convertible-coins

        权重(UID):600

        请求参数:
        Parameter         	Type    	Required	Description

        coin              	STRING  	YES     	USDC、USDP、TUSD 中的一个
        enable            	BOOLEAN 	YES     	true: 打开转换。false: 关闭转换
        '''
        return self.send_request(*_WalletEndpoints.set_capital_contract_convertible_coins, **to_local(locals()))


    # 一键上账 (充值到过期地址) (USER_DATA)
    def set_capital_deposit_credit_apply(self,depositId:int = '',txId:str = '',subAccountId:int = '',subUserId:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/capital/deposit/credit-apply

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        depositId         	LONG    	NO      	充值记录Id，优先使用
        txId              	STRING  	NO      	充值txId，当depositId没指定时使用
        subAccountId      	LONG    	NO      	Cloud的子账户ID
        subUserId         	LONG    	NO      	母账户的子账户userId
        '''
        return self.send_request(*_WalletEndpoints.set_capital_deposit_credit_apply, **to_local(locals()))


    # 查询充值地址列表(USER_DATA)
    def get_capital_deposit_address_list(self,coin:str = '',network:str = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/capital/deposit/address/list

        权重(IP):10

        请求参数:
        Parameter         	Type    	Required	Description

        coin              	STRING  	YES     	币种
        network           	STRING  	NO      	网络
        timestamp         	LONG    	YES     	时间戳
        '''
        return self.send_request(*_WalletEndpoints.get_capital_deposit_address_list, **to_local(locals()))


    # 查询用户钱包余额 (USER_DATA)
    def get_asset_wallet_balance(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/asset/wallet/balance

        权重(IP):60

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_WalletEndpoints.get_asset_wallet_balance, **to_local(locals()))


    # 查询用户委托资金历史(适用主账户)(USER_DATA)
    def get_asset_custody_transfer_history(self,email:str = '',startTime:int = '',endTime:int = '',type:str = '',asset:str = '',current:int = '',size:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/asset/custody/transfer-history

        权重(IP):60

        请求参数:
        Parameter         	Type    	Required	Description

        email             	STRING  	YES     	
        startTime         	LONG    	YES     	
        endTime           	LONG    	YES     	
        type              	ENUM    	NO      	Delegate/Undelegate
        asset             	STRING  	NO      	
        current           	INTEGER 	NO      	默认 1
        size              	INTEGER 	NO      	默认 10, 最大 100
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_WalletEndpoints.get_asset_custody_transfer_history, **to_local(locals()))