from typing import Literal, Union
from paux.param import to_local
from binance_interface.api.um import UM
from binance_interface.app import code
from binance_interface.app import utils
from binance_interface.app import exception


class AccountUM():

    def __init__(self, key: str, secret: str, proxies={}, proxy_host: str = None):
        self.umAPI = UM(key=key, secret=secret, proxies=proxies, proxy_host=proxy_host)

    # 获取账户信息 Weight: 5
    def get_account(self, recvWindow: int = '') -> dict:
        return self.umAPI.accountTrade.get_account(**to_local(locals()))

    # 获取全部产品余额 Weight: 5
    def get_balances(self, recvWindow: int = ''):
        return self.umAPI.accountTrade.get_balance(**to_local(locals()))

    # 获取单个产品余额 Weight: 5
    def get_balance(self, asset: str = ''):
        '''
        :param asset: 货币名称
        '''
        balances_result = self.get_balances()
        if balances_result['code'] != 200:
            return balances_result
        for balance in balances_result['data']:
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

    # 调整开仓杠杆 Weight : 1
    def set_leverage(
            self,
            symbol: str,
            leverage: int = '',
            recvWindow: int = ''
    ) -> dict:
        '''
        Name      	Type	Mandatory	Description
        symbol    	str 	YES      	交易对
        leverage  	int 	YES      	目标杠杆倍数
        '''
        return self.umAPI.accountTrade.set_leverage(**to_local(locals()))

    # 更改持仓模式 Weight : 1
    def set_marginType(
            self,
            symbol: str,
            marginType: Literal['ISOLATED', 'CROSSED'],
            recvWindow: int = ''
    ) -> dict:
        '''
        https://binance-docs.github.io/apidocs/delivery/cn/#trade-12

        Name      	Type	Mandatory	Description
        symbol    	str 	YES      	交易对
        marginType	str 	YES      	保证金模式 ISOLATED(逐仓), CROSSED(全仓)
        '''
        result = self.umAPI.accountTrade.set_marginType(**to_local(locals()))
        # 4046 NO_NEED_TO_CHANGE_MARGIN_TYPE 不需要切换仓位模式。
        if result['code'] in [-4046, 200]:
            result['code'] = 200
        return result

    # 获取全部产品的持仓信息 Weight: 5
    def get_positions(self):
        result = self.get_account()
        if result['code'] != 200:
            return result
        else:
            positions = {
                'CROSSED': {
                    'LONG': [],
                    'SHORT': [],
                },
                'ISOLATED': {
                    'LONG': [],
                    'SHORT': [],
                }
            }
            for v in result['data']['positions']:
                if 'positionAmt' in v.keys() and float(v['positionAmt']) > 0:
                    if v['isolated'] == True:
                        mode = 'ISOLATED'
                    else:
                        mode = 'CROSSED'
                    posSide = v['positionSide'].upper()
                    positions[mode][posSide].append(v)
            result['data'] = positions
            return result

    # 获取单个产品的持仓信息 Weight: 5
    def get_position(self, symbol: str) -> dict:
        result = self.get_positions()
        if result['code'] != 200:
            return result
        positions = {
            'CROSSED': {
                'LONG': {},
                'SHORT': {},
            },
            'ISOLATED': {
                'LONG': {},
                'SHORT': {},
            }
        }
        for mode, mode_data in result['data'].items():
            for posSide, posSide_datas in mode_data.items():
                for posSide_data in posSide_datas:
                    if posSide_data['symbol'] == symbol:
                        positions[mode][posSide] = posSide_data
        result['data'] = positions
        return result
