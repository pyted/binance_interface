from paux.param import to_local
from binance_interface.api.spot import SPOT
from binance_interface.app import code
from binance_interface.app import utils
from binance_interface.app import exception


class AccountSPOT():

    def __init__(self, key: str, secret: str, proxies={}, proxy_host: str = None):
        self.spotAPI = SPOT(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)

    # 获取账户信息 Weight: 20
    def get_account(self, recvWindow: int = '') -> dict:
        return self.spotAPI.account.get_account(**to_local(locals()))

    # 获取全部现货余额 Weight: 20
    def get_balances(self, assets=[]):
        '''
        :param assets:获取的货币，空表示全部
        :return:
        '''
        api_account_result = self.get_account()
        if api_account_result['code'] != 200:
            return api_account_result

        balances_result = {'code': 200, 'data': [], 'msg': ''}

        for balance in api_account_result['data']['balances']:
            this_asset = balance['asset']
            if assets and this_asset not in assets:
                continue
            balances_result['data'].append(balance)
        return balances_result

    # 获取单个现货余额 Weight: 20
    def get_balance(self, asset: str = '', symbol: str = '', base_asset: str = ''):
        '''
        :param asset: 货币名称
        :param symbol: 产品名称
        :param base_asset: 产品的交易基础货币
        asset与symbol不能同时为空

        例如：对于产品：BTCUSDT，其中：
            asset = 'BTC'
            symbol = 'BTCUSDT'
            base_asset = 'USDT'
        '''
        if not asset and not symbol:
            raise exception.ParamException('asset and symbol can not be empty together')
        if not asset:
            asset = utils.get_asset(symbol=symbol, base_asset=base_asset)
        account_result = self.get_account()
        if account_result['code'] != 200:
            return account_result
        for balance in account_result['data']['balances']:
            if balance['asset'] == asset:
                result = {
                    'code': 200,
                    'data': balance,
                    'msg': ''
                }
                return result
        else:
            msg = f'Can not find asset = {asset}'
            result = {
                'code': code.ASSET_ERROR[0],
                'data': {},
                'msg': msg,
            }
            return result

    # 获取全部现货余额字典 Weight: 20
    def get_balancesMap(self, assets=[]):
        '''
        :param assets:获取的货币，空表示全部
        :return:
        '''
        balances_result = self.get_balances(assets=assets)
        if not balances_result['code'] == 200:
            return balances_result
        balancesMap = {}
        for balance in balances_result['data']:
            balance: dict
            asset = balance['asset']
            balancesMap[asset] = balance
        result = {'code': 200, 'data': balancesMap, 'msg': ''}
        return result
