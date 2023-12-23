# 矿池接口
from paux.param import to_local
from binance_interface.api.client import Client
from typing import Union

class _MiningEndpoints():


    get_mining_pub_algoList = ['https://api.binance.com', 'GET', '/sapi/v1/mining/pub/algoList', False] # 获取算法(MARKET_DATA)
    get_mining_pub_coinList = ['https://api.binance.com', 'GET', '/sapi/v1/mining/pub/coinList', False] # 获取币种(MARKET_DATA)
    get_mining_worker_detail = ['https://api.binance.com', 'GET', '/sapi/v1/mining/worker/detail', True] # 请求矿工列表明细 (USER_DATA) 
    get_mining_worker_list = ['https://api.binance.com', 'GET', '/sapi/v1/mining/worker/list', True] # 请求矿工列表 (USER_DATA) 
    get_mining_payment_list = ['https://api.binance.com', 'GET', '/sapi/v1/mining/payment/list', True] # 收益列表 (USER_DATA) 
    get_mining_payment_other = ['https://api.binance.com', 'GET', '/sapi/v1/mining/payment/other', True] # 其他收益列表 (USER_DATA) 
    get_mining_hash_transfer_config_details = ['https://api.binance.com', 'GET', '/sapi/v1/mining/hash-transfer/config/details', True] # 算力转让详情列表 (USER_DATA) 
    get_mining_hash_transfer_config_details_list = ['https://api.binance.com', 'GET', '/sapi/v1/mining/hash-transfer/config/details/list', True] # 算力转让列表 (USER_DATA) 
    get_mining_hash_transfer_profit_details = ['https://api.binance.com', 'GET', '/sapi/v1/mining/hash-transfer/profit/details', True] # 算力转让详情 (USER_DATA) 
    set_mining_hash_transfer_config = ['https://api.binance.com', 'POST', '/sapi/v1/mining/hash-transfer/config', True] # 算力转让请求 (USER_DATA) 
    set_mining_hash_transfer_config_cancel = ['https://api.binance.com', 'POST', '/sapi/v1/mining/hash-transfer/config/cancel', True] # 取消算力转让设置 (USER_DATA) 
    get_mining_statistics_user_status = ['https://api.binance.com', 'GET', '/sapi/v1/mining/statistics/user/status', True] # 统计列表 (USER_DATA) 
    get_mining_statistics_user_list = ['https://api.binance.com', 'GET', '/sapi/v1/mining/statistics/user/list', True] # 账号列表 (USER_DATA) 
    get_mining_payment_uid = ['https://api.binance.com', 'GET', '/sapi/v1/mining/payment/uid', True] # 矿池账户收益列表 (USER_DATA)  


class Mining(Client):

    # 获取算法(MARKET_DATA)
    def get_mining_pub_algoList(self,proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/mining/pub/algoList

        权重(IP):1
        '''
        return self.send_request(*_MiningEndpoints.get_mining_pub_algoList, **to_local(locals()))


    # 获取币种(MARKET_DATA)
    def get_mining_pub_coinList(self,proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/mining/pub/coinList

        权重(IP):1
        '''
        return self.send_request(*_MiningEndpoints.get_mining_pub_coinList, **to_local(locals()))


    # 请求矿工列表明细 (USER_DATA)
    def get_mining_worker_detail(self,algo:str = '',userName:str = '',workerName:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/mining/worker/detail

        权重(IP):5

        请求参数:
        Parameter         	Type    	Required	Description

        algo              	STRING  	YES     	算法名称(sha256)
        userName          	STRING  	YES     	挖矿用户名
        workerName        	STRING  	YES     	矿工用户名，必传
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MiningEndpoints.get_mining_worker_detail, **to_local(locals()))


    # 请求矿工列表 (USER_DATA)
    def get_mining_worker_list(self,algo:str = '',userName:str = '',pageIndex:int = '',sort:int = '',sortColumn:int = '',workerStatus:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/mining/worker/list

        权重(IP):5

        请求参数:
        Parameter         	Type    	Required	Description

        algo              	STRING  	YES     	算法名称(sha256)
        userName          	STRING  	YES     	挖矿用户名
        pageIndex         	INTEGER 	NO      	页码，为空默认第一页，从1开始
        sort              	INTEGER 	NO      	排序方向(为空默认为0): 0 正序，1 倒序
        sortColumn        	INTEGER 	NO      	排序字段(默认为1):1: 根据矿工名称排序，2: 根据实时算力排序，3: 根据日均算力排序，4: 根据实时拒绝率排序，5最后提交时间
        workerStatus      	INTEGER 	NO      	矿机状态(默认为0)：0 全部，1 有效， 2 无效， 3 失效
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MiningEndpoints.get_mining_worker_list, **to_local(locals()))


    # 收益列表 (USER_DATA)
    def get_mining_payment_list(self,algo:str = '',userName:str = '',coin:str = '',startDate:int = '',endDate:int = '',pageIndex:int = '',pageSize:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/mining/payment/list

        权重(IP):5

        请求参数:
        Parameter         	Type    	Required	Description

        algo              	STRING  	YES     	算法名称(sha256)
        userName          	STRING  	YES     	挖矿用户名
        coin              	STRING  	NO      	币种名称
        startDate         	Long    	NO      	搜索日期 毫秒时间戳，同时为空查询所有
        endDate           	Long    	NO      	搜索日期 毫秒时间戳，同时为空查询所有
        pageIndex         	INTEGER 	NO      	页码，为空默认第一页，从1开始
        pageSize          	INTEGER 	NO      	分页数量,最小10,最大200
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MiningEndpoints.get_mining_payment_list, **to_local(locals()))


    # 其他收益列表 (USER_DATA)
    def get_mining_payment_other(self,algo:str = '',userName:str = '',coin:str = '',startDate:int = '',endDate:int = '',pageIndex:int = '',pageSize:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/mining/payment/other

        权重(IP):5

        请求参数:
        Parameter         	Type    	Required	Description

        algo              	STRING  	YES     	算法名称(sha256)
        userName          	STRING  	YES     	挖矿用户名
        coin              	STRING  	NO      	币种名称
        startDate         	Long    	NO      	搜索日期 毫秒时间戳，同时为空查询所有
        endDate           	Long    	NO      	搜索日期 毫秒时间戳，同时为空查询所有
        pageIndex         	INTEGER 	NO      	页码，为空默认第一页，从1开始
        pageSize          	INTEGER 	NO      	分页数量,最小10,最大200
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MiningEndpoints.get_mining_payment_other, **to_local(locals()))


    # 算力转让详情列表 (USER_DATA)
    def get_mining_hash_transfer_config_details(self,pageIndex:int = '',pageSize:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/mining/hash-transfer/config/details

        权重(IP):5

        请求参数:
        Parameter         	Type    	Required	Description

        pageIndex         	INTEGER 	NO      	页码，为空默认第一页，从1开始
        pageSize          	INTEGER 	NO      	分页数量,最小10,最大200
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MiningEndpoints.get_mining_hash_transfer_config_details, **to_local(locals()))


    # 算力转让列表 (USER_DATA)
    def get_mining_hash_transfer_config_details_list(self,pageIndex:int = '',pageSize:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/mining/hash-transfer/config/details/list

        权重(IP):5

        请求参数:
        Parameter         	Type    	Required	Description

        pageIndex         	INTEGER 	NO      	页码，为空默认第一页，从1开始
        pageSize          	INTEGER 	NO      	分页数量,最小10,最大200
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MiningEndpoints.get_mining_hash_transfer_config_details_list, **to_local(locals()))


    # 算力转让详情 (USER_DATA)
    def get_mining_hash_transfer_profit_details(self,configId:int = '',pageIndex:int = '',pageSize:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/mining/hash-transfer/profit/details

        权重(IP):5

        请求参数:
        Parameter         	Type    	Required	Description

        configId          	INTEGER 	YES     	配置的id
        pageIndex         	INTEGER 	NO      	页码，为空默认第一页，从1开始
        pageSize          	INTEGER 	NO      	分页数量,最小10,最大200
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MiningEndpoints.get_mining_hash_transfer_profit_details, **to_local(locals()))


    # 算力转让请求 (USER_DATA)
    def set_mining_hash_transfer_config(self,userName:str = '',algo:str = '',endDate:int = '',startDate:int = '',toPoolUser:str = '',hashRate:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/mining/hash-transfer/config

        权重(IP):5

        请求参数:
        Parameter         	Type    	Required	Description

        userName          	STRING  	YES     	挖矿用户名
        algo              	STRING  	YES     	算法名称(sha256)
        endDate           	Long    	YES     	转让结束时间(毫秒时间戳)
        startDate         	Long    	YES     	转让结束时间(毫秒时间戳)
        toPoolUser        	STRING  	YES     	挖矿用户名
        hashRate          	Long    	YES     	转让算力h/s必传(BTC 大于 500000000000 ETH大于 500000)
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MiningEndpoints.set_mining_hash_transfer_config, **to_local(locals()))


    # 取消算力转让设置 (USER_DATA)
    def set_mining_hash_transfer_config_cancel(self,configId:int = '',userName:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        POST /sapi/v1/mining/hash-transfer/config/cancel

        权重(IP):5

        请求参数:
        Parameter         	Type    	Required	Description

        configId          	INTEGER 	YES     	配置的id
        userName          	STRING  	YES     	挖矿用户名
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MiningEndpoints.set_mining_hash_transfer_config_cancel, **to_local(locals()))


    # 统计列表 (USER_DATA)
    def get_mining_statistics_user_status(self,algo:str = '',userName:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/mining/statistics/user/status

        权重(IP):5

        请求参数:
        Parameter         	Type    	Required	Description

        algo              	STRING  	YES     	算法名称(sha256)
        userName          	STRING  	YES     	挖矿用户名
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MiningEndpoints.get_mining_statistics_user_status, **to_local(locals()))


    # 账号列表 (USER_DATA)
    def get_mining_statistics_user_list(self,algo:str = '',userName:str = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/mining/statistics/user/list

        权重(IP):5

        请求参数:
        Parameter         	Type    	Required	Description

        algo              	STRING  	YES     	算法名称(sha256)
        userName          	STRING  	YES     	挖矿用户名
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MiningEndpoints.get_mining_statistics_user_list, **to_local(locals()))


    # 矿池账户收益列表 (USER_DATA)
    def get_mining_payment_uid(self,algo:str = '',startDate:int = '',endDate:int = '',pageIndex:int = '',pageSize:int = '',recvWindow:int = '',timestamp:int = '',proxies={},proxy_host:str=None):
        '''
        GET /sapi/v1/mining/payment/uid

        权重(IP):5

        请求参数:
        Parameter         	Type    	Required	Description

        algo              	STRING  	YES     	算法名称(sha256)
        startDate         	Long    	NO      	搜索日期 毫秒时间戳，同时为空查询所有
        endDate           	Long    	NO      	搜索日期 毫秒时间戳，同时为空查询所有
        pageIndex         	INTEGER 	NO      	页码，为空默认第一页，从1开始
        pageSize          	INTEGER 	NO      	分页数量,最小10,最大200
        recvWindow        	LONG    	NO      	
        timestamp         	LONG    	YES
        '''
        return self.send_request(*_MiningEndpoints.get_mining_payment_uid, **to_local(locals()))