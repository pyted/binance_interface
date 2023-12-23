# 定投接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _AutoInvestEndpoints():


    get_lending_auto_invest_target_asset_list = ['https://api.binance.com', 'GET', '/sapi/v1/lending/auto-invest/target-asset/list', True] # 查询允许申购币种列表 (USER_DATA) 
    get_lending_auto_invest_target_asset_roi_list = ['https://api.binance.com', 'GET', '/sapi/v1/lending/auto-invest/target-asset/roi/list', True] # 查询申购币种投资回报率(USER_DATA) 
    get_lending_auto_invest_all_asset = ['https://api.binance.com', 'GET', '/sapi/v1/lending/auto-invest/all/asset', True] # 查询申购币种和投资币种列表(USER_DATA) 
    get_lending_auto_invest_source_asset_list = ['https://api.binance.com', 'GET', '/sapi/v1/lending/auto-invest/source-asset/list', True] # 查询投资币种列表(USER_DATA) 
    set_lending_auto_invest_plan_add = ['https://api.binance.com', 'POST', '/sapi/v1/lending/auto-invest/plan/add', True] # 创建定投计划 (TRADE) 
    set_lending_auto_invest_plan_edit = ['https://api.binance.com', 'POST', '/sapi/v1/lending/auto-invest/plan/edit', True] # 编辑定投计划 (TRADE) 
    set_lending_auto_invest_plan_edit_status = ['https://api.binance.com', 'POST', '/sapi/v1/lending/auto-invest/plan/edit-status', True] # 定投计划状态管理 (TRADE) 
    get_lending_auto_invest_plan_list = ['https://api.binance.com', 'GET', '/sapi/v1/lending/auto-invest/plan/list', True] # 查询定投计划列表 (USER_DATA) 
    get_lending_auto_invest_plan_id = ['https://api.binance.com', 'GET', '/sapi/v1/lending/auto-invest/plan/id', True] # 查询定投计划详情 (USER_DATA) 
    get_lending_auto_invest_history_list = ['https://api.binance.com', 'GET', '/sapi/v1/lending/auto-invest/history/list', True] # 查询申购历史 (USER_DATA) 
    get_lending_auto_invest_index_info = ['https://api.binance.com', 'GET', '/sapi/v1/lending/auto-invest/index/info', True] # 查询指数信息(USER_DATA) 
    get_lending_auto_invest_index_user_summary = ['https://api.binance.com', 'GET', '/sapi/v1/lending/auto-invest/index/user-summary', True] # 查询指数关连计划详情（USER_DATA） 
    set_lending_auto_invest_one_off = ['https://api.binance.com', 'POST', '/sapi/v1/lending/auto-invest/one-off', True] # 单次申购(TRADE) 
    get_lending_auto_invest_one_off_status = ['https://api.binance.com', 'GET', '/sapi/v1/lending/auto-invest/one-off/status', True] # 单次申购交易结果查询(USER_DATA) 
    set_lending_auto_invest_redeem = ['https://api.binance.com', 'POST', '/sapi/v1/lending/auto-invest/redeem', True] # 指数关连计划赎回交易(TRADE) 
    get_lending_auto_invest_redeem_history = ['https://api.binance.com', 'GET', '/sapi/v1/lending/auto-invest/redeem/history', True] # 指数关连计划赎回交易历史查询(USER_DATA) 
    get_lending_auto_invest_rebalance_history = ['https://api.binance.com', 'GET', '/sapi/v1/lending/auto-invest/rebalance/history', True] # 指数关连计划调仓历史记录(USER_DATA)  


class AutoInvest(Client):

    # 查询允许申购币种列表 (USER_DATA)
    def get_lending_auto_invest_target_asset_list(self,targetAsset:str = '',size:int = '',current:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/lending/auto-invest/target-asset/list

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        targetAsset       	STRING  	NO      	
        size              	LONG    	NO      	默认: 8, 最多:100
        current           	LONG    	NO      	当前查询页。 从 1开始。 默认:1
        recvWindow        	LONG    	NO      	不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_AutoInvestEndpoints.get_lending_auto_invest_target_asset_list, **to_local(locals()))


    # 查询申购币种投资回报率(USER_DATA)
    def get_lending_auto_invest_target_asset_roi_list(self,targetAsset:str = '',hisRoiType:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/lending/auto-invest/target-asset/roi/list

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        targetAsset       	STRING  	YES     	e.g "BTC"
        hisRoiType        	ENUM    	YES     	FIVE_YEAR,THREE_YEAR,ONE_YEAR,SIX_MONTH,THREE_MONTH,SEVEN_DAY
        recvWindow        	LONG    	NO      	不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_AutoInvestEndpoints.get_lending_auto_invest_target_asset_roi_list, **to_local(locals()))


    # 查询申购币种和投资币种列表(USER_DATA)
    def get_lending_auto_invest_all_asset(self,recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/lending/auto-invest/all/asset

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        recvWindow        	LONG    	NO      	不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_AutoInvestEndpoints.get_lending_auto_invest_all_asset, **to_local(locals()))


    # 查询投资币种列表(USER_DATA)
    def get_lending_auto_invest_source_asset_list(self,targetAsset:list = [],indexId:int = '',usageType:str = '',flexibleAllowedToUse:bool = '',sourceType:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/lending/auto-invest/source-asset/list

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        targetAsset       	Array<STRING>	NO      	BTC、ETH、BNB
        indexId           	Long    	NO      	指数identifier,   value = 1
        usageType         	STRING  	YES     	"RECURRING", "ONE_TIME"
        flexibleAllowedToUse	BOOLEAN 	NO      	
        sourceType        	ENUM    	NO      	MAIN_SITEBinance用户,TRBinance Turkey用户
        recvWindow        	LONG    	NO      	不能大于60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_AutoInvestEndpoints.get_lending_auto_invest_source_asset_list, **to_local(locals()))


    # 创建定投计划 (TRADE)
    def set_lending_auto_invest_plan_add(self,sourceType:str = '',requestId:str = '',planType:str = '',IndexId:int = '',subscriptionAmount:Union[int,float] = '',subscriptionCycle:str = '',subscriptionStartDay:int = '',subscriptionStartWeekday:str = '',subscriptionStartTime:int = '',sourceAsset:str = '',flexibleAllowedToUse:bool = '',details:list = [],recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/lending/auto-invest/plan/add

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        sourceType        	ENUM    	YES     	"MAIN_SITE" 币安,“TR”为币安土耳其
        requestId         	STRING  	NO      	若不为空, 字段规则为 sourceType + unique string e.g: TR12354859
        planType          	ENUM    	YES     	“SINGLE”,”PORTFOLIO”,”INDEX”
        IndexId           	LONG    	NO      	只有当 planType = INDEX ,  value = 1
        subscriptionAmount	DECIMAL 	YES     	Fiat&stablecoin: 2dp, BNB/ETH/BTC: 4dp
        subscriptionCycle 	ENUM    	YES     	"H1", "H4", "H8","H12", "WEEKLY","DAILY","MONTHLY","BI_WEEKLY"
        subscriptionStartDay	INTEGER 	NO      	“1”,...”31”; 如果 “subscriptionCycleNumberUnit” = “MONTHLY”则必填,数值必须为 UTC+0
        subscriptionStartWeekday	ENUM    	NO      	“MON”,”TUE”,”WED”,”THU”,”FRI”,”SAT”,”SUN”; 如果 “subscriptionCycleNumberUnit” = “MONTHLY”则必填,数值必须为 UTC+0
        subscriptionStartTime	INTEGER 	YES     	“0,1,2,3,4,5,6,7,8,..23”;数值必须为 UTC+0
        sourceAsset       	STRING  	YES     	如 “USDT”
        flexibleAllowedToUse	BOOLEAN 	NO      	true/false；true:使用 flexible wallet
        details           	Array<PortfolioDetail>	YES     	sum(all node's percentage) == 100，若作为请求参数发送, 像以下格式details[0].targetAsset=BTC details[0].percentage=60 details[1].targetAsset=ETH details[1].percentage=40
        recvWindow        	LONG    	NO      	不超过60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_AutoInvestEndpoints.set_lending_auto_invest_plan_add, **to_local(locals()))


    # 编辑定投计划 (TRADE)
    def set_lending_auto_invest_plan_edit(self,planId:int = '',subscriptionAmount:Union[int,float] = '',subscriptionCycle:str = '',subscriptionStartDay:int = '',subscriptionStartWeekday:str = '',subscriptionStartTime:int = '',sourceAsset:str = '',flexibleAllowedToUse:bool = '',details:list = [],recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/lending/auto-invest/plan/edit

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        planId            	LONG    	YES     	计划编号
        subscriptionAmount	DECIMAL 	YES     	Fiat&Stablecoin: 2dp, BNB/ETH/BTC: 4dp
        subscriptionCycle 	ENUM    	YES     	"H1", "H4", "H8","H12", "WEEKLY","DAILY","MONTHLY","BI_WEEKLY"
        subscriptionStartDay	INTEGER 	NO      	“1”,...”31”; 如果 “subscriptionCycleNumberUnit” = “MONTHLY”则必填,数值必须为 UTC+0
        subscriptionStartWeekday	ENUM    	NO      	“MON”,”TUE”,”WED”,”THU”,”FRI”,”SAT”,”SUN”; 如果 “subscriptionCycleNumberUnit” = “MONTHLY”则必填,数值必须为 UTC+0
        subscriptionStartTime	INTEGER 	YES     	“0,1,2,3,4,5,6,7,8,..23”;Must be sent in form of UTC+0
        sourceAsset       	STRING  	YES     	如 “USDT”
        flexibleAllowedToUse	BOOLEAN 	NO      	true/false；true:使用 flexible wallet
        details           	Array<PortfolioDetail>	YES     	sum(all node's percentage) == 100，若作为请求参数发送, 像以下格式details[0].targetAsset=BTC
        recvWindow        	LONG    	NO      	no more than60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_AutoInvestEndpoints.set_lending_auto_invest_plan_edit, **to_local(locals()))


    # 定投计划状态管理 (TRADE)
    def set_lending_auto_invest_plan_edit_status(self,planId:int = '',status:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/lending/auto-invest/plan/edit-status

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        planId            	LONG    	YES     	计划编号
        status            	ENUM    	YES     	“ONGOING”,”PAUSED","REMOVED"
        recvWindow        	LONG    	NO      	no more than60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_AutoInvestEndpoints.set_lending_auto_invest_plan_edit_status, **to_local(locals()))


    # 查询定投计划列表 (USER_DATA)
    def get_lending_auto_invest_plan_list(self,planType:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/lending/auto-invest/plan/list

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        planType          	STRING  	YES     	“SINGLE”,”PORTFOLIO”,”INDEX”用以区分查询计划类型
        recvWindow        	LONG    	NO      	不超过60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_AutoInvestEndpoints.get_lending_auto_invest_plan_list, **to_local(locals()))


    # 查询定投计划详情 (USER_DATA)
    def get_lending_auto_invest_plan_id(self,planId:int = '',requestId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/lending/auto-invest/plan/id

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        planId            	LONG    	NO      	计划编号
        requestId         	STRING  	NO      	创建时requestId
        recvWindow        	LONG    	NO      	不超过60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_AutoInvestEndpoints.get_lending_auto_invest_plan_id, **to_local(locals()))


    # 查询申购历史 (USER_DATA)
    def get_lending_auto_invest_history_list(self,planId:int = '',requestId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/lending/auto-invest/history/list

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        planId            	LONG    	NO      	计划编号
        requestId         	STRING  	NO      	创建时requestId
        recvWindow        	LONG    	NO      	不超过60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_AutoInvestEndpoints.get_lending_auto_invest_history_list, **to_local(locals()))


    # 查询指数信息(USER_DATA)
    def get_lending_auto_invest_index_info(self,indexId:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/lending/auto-invest/index/info

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        indexId           	LONG    	YES     	
        recvWindow        	LONG    	NO      	不超过60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_AutoInvestEndpoints.get_lending_auto_invest_index_info, **to_local(locals()))


    # 查询指数关连计划详情（USER_DATA）
    def get_lending_auto_invest_index_user_summary(self,indexId:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/lending/auto-invest/index/user-summary

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        indexId           	LONG    	YES     	
        recvWindow        	LONG    	NO      	不超过60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_AutoInvestEndpoints.get_lending_auto_invest_index_user_summary, **to_local(locals()))


    # 单次申购(TRADE)
    def set_lending_auto_invest_one_off(self,sourceType:str = '',requestId:str = '',subscriptionAmount:Union[int,float] = '',sourceAsset:str = '',flexibleAllowedToUse:bool = '',planId:int = '',indexId:int = '',details:list = [],recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/lending/auto-invest/one-off

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        sourceType        	STRING  	YES     	"MAIN_SITE",“TR” 只有Binance Turkey使用TR入参
        requestId         	STRING  	NO      	if not null, must follow businessReference + unique string, e.g: TR12354859
        subscriptionAmount	DECIMAL 	YES     	
        sourceAsset       	STRING  	YES     	“USDT”,”BUSD”
        flexibleAllowedToUse	BOOLEAN 	NO      	true/false，True:使用flexible wallet，TR业务使用false
        planId            	LONG    	NO      	PORTFOLIO plan Id
        indexId           	LONG    	NO      	目前只有 1
        details           	Array<PortfolioDetail>	NO      	sum(all node's percentage) == 100，在请求参数，样例为 &details[0].targetAsset=BTC&details[0].percentage=60&details[1].targetAsset=ETH&details[1].percentage=40
        recvWindow        	LONG    	NO      	不超过60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_AutoInvestEndpoints.set_lending_auto_invest_one_off, **to_local(locals()))


    # 单次申购交易结果查询(USER_DATA)
    def get_lending_auto_invest_one_off_status(self,transactionId:int = '',requestId:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/lending/auto-invest/one-off/status

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        transactionId     	LONG    	YES     	PORTFOLIO plan Id
        requestId         	STRING  	NO      	TR1212123123, sourceType + unique, transactionId and requestId 不能同时为空
        recvWindow        	LONG    	NO      	不超过60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_AutoInvestEndpoints.get_lending_auto_invest_one_off_status, **to_local(locals()))


    # 指数关连计划赎回交易(TRADE)
    def set_lending_auto_invest_redeem(self,indexId:int = '',requestId:str = '',redemptionPercentage:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/lending/auto-invest/redeem

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        indexId           	LONG    	YES     	指数id
        requestId         	STRING  	NO      	TR1212123123, sourceType + unique, transactionId and requestId 不能同时为空
        redemptionPercentage	LONG    	YES     	赎回的占比, 10/20/100..
        recvWindow        	LONG    	NO      	不超过60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_AutoInvestEndpoints.set_lending_auto_invest_redeem, **to_local(locals()))


    # 指数关连计划赎回交易历史查询(USER_DATA)
    def get_lending_auto_invest_redeem_history(self,requestId:int = '',startTime:int = '',endTime:int = '',current:int = '',asset:str = '',size:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/lending/auto-invest/redeem/history

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        requestId         	LONG    	YES     	请求id
        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        current           	LONG    	NO      	当前查询页，从1开始，1位默认值
        asset             	STRING  	NO      	
        size              	LONG    	NO      	默认:10, 最大:100
        recvWindow        	LONG    	NO      	不超过60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_AutoInvestEndpoints.get_lending_auto_invest_redeem_history, **to_local(locals()))


    # 指数关连计划调仓历史记录(USER_DATA)
    def get_lending_auto_invest_rebalance_history(self,startTime:int = '',endTime:int = '',current:int = '',size:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/lending/auto-invest/rebalance/history

        权重(IP):1

        请求参数:
        Parameter         	Type    	Required	Description

        startTime         	LONG    	NO      	
        endTime           	LONG    	NO      	
        current           	LONG    	NO      	当前查询页，从1开始，1位默认值
        size              	LONG    	NO      	默认:10, 最大:100
        recvWindow        	LONG    	NO      	不超过60000
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_AutoInvestEndpoints.get_lending_auto_invest_rebalance_history, **to_local(locals()))