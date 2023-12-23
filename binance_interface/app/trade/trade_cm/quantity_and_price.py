from typing import Literal, Union
from paux import order as _order
from paux.digit import origin_float
from binance_interface.app.trade.trade_cm._base import TradeCMBase
from binance_interface.app import exception
from binance_interface.app import code


class TradeQuantityAndPrice(TradeCMBase):
    # 下单数量圆整
    # Weight 0 | 1
    def round_quantity(
            self,
            quantity: Union[int, float, str, origin_float],
            symbol: str,
            stepSize: str = None,
            minQty: str = None,
            maxQty: str = None,
            expire_seconds=60 * 5,
    ) -> dict:
        '''
        :param quantity: 下单数量
        :param symbol: 合约产品
        :param stepSize: 订单最小数量间隔
        :param minQty:  最小数量
        :param maxQty:  最大数量
        :param use_cache: 使用缓存获取交易规则和交易对信息
        :param expire_seconds: 缓存过期时间 (秒)

        stepSize minQty maxQty任意为空，通过market.exchangeInfo获取交易规则与交易对信息
        '''

        # 填充stepSize minQty maxQty
        if stepSize in [None, ''] or minQty in [None, ''] or maxQty in [None, '']:
            exchangeInfo = self._market.get_exchangeInfo(
                symbol=symbol,
                expire_seconds=expire_seconds
            )
            if exchangeInfo['code'] != 200:
                return exchangeInfo
            if stepSize in [None, '']:
                stepSize = exchangeInfo['data']['filter']['LOT_SIZE']['stepSize']
            if minQty in [None, '']:
                minQty = exchangeInfo['data']['filter']['LOT_SIZE']['minQty']
            if maxQty in [None, '']:
                maxQty = exchangeInfo['data']['filter']['LOT_SIZE']['maxQty']
        # code = 0 | -1 | -2
        round_quantity_result = _order.round_quantity(
            quantity=quantity,
            stepSize=stepSize,
            minQty=minQty,
            maxQty=maxQty
        )
        # code -> [200,code.ROUND_QUANTITY_ERROR[0]]
        if round_quantity_result['code'] == 0:
            round_quantity_result['code'] = 200
        else:
            round_quantity_result['code'] = code.ROUND_QUANTITY_ERROR[0]
            round_quantity_result['msg'] = f'symbol={symbol} ' + round_quantity_result['msg']
        return round_quantity_result

    # 价格圆整
    # Weight 0 | 1
    def round_price(
            self,
            price: Union[int, float],
            symbol: str,
            type: Literal['CEIL', 'FLOOR', 'ceil', 'floor'],
            tickSize: str = None,
            minPrice: str = None,
            maxPrice: str = None,
            expire_seconds=60 * 5,
    ) -> dict:
        '''
        :param price: 价格
        :param symbol: 合约产品
        :param type: 圆整方式
                CEIL:   向上圆整
                FLOOR:  向下圆整
        :param tickSize: 订单价格的最小间隔
        :param minPrice: 最小价格
        :param maxPrice: 最大价格
        :param use_cache: 使用缓存获取交易规则和交易对信息
        :param expire_seconds: 缓存过期时间 (秒)

        tickSize minPrice maxPrice任意为空，通过market.exchangeInfo获取交易规则与交易对信息
        '''
        # 验证type
        if type not in ['CEIL', 'FLOOR']:
            raise exception.ParamRoundPriceTypeException(type=type)
        # tickSize maxPrice minPrice
        if tickSize in [None, ''] or maxPrice in [None, ''] or minPrice in [None, '']:
            exchangeInfo = self._market.get_exchangeInfo(
                symbol=symbol,
                expire_seconds=expire_seconds
            )
            if exchangeInfo['code'] != 200:
                return exchangeInfo
            if tickSize in [None, '']:
                tickSize = exchangeInfo['data']['filter']['PRICE_FILTER']['tickSize']
            if minPrice in [None, '']:
                minPrice = exchangeInfo['data']['filter']['PRICE_FILTER']['minPrice']
            if maxPrice in [None, '']:
                maxPrice = exchangeInfo['data']['filter']['PRICE_FILTER']['maxPrice']
        # code = 0 | -1 | -2
        round_price_result = _order.round_price(
            price=price,
            type=type,
            tickSize=tickSize,
            minPrice=minPrice,
            maxPrice=maxPrice
        )
        # code -> [200,code.ROUND_PRICE_ERROR[0]]
        if round_price_result['code'] == 0:
            round_price_result['code'] = 200
        else:
            round_price_result['code'] = code.ROUND_PRICE_ERROR[0]
            round_price_result['msg'] = f'symbol={symbol} ' + round_price_result['msg']
        return round_price_result

    # 根据合约产品的开仓金额、杠杆倍数、开仓价格获取购买数量
    # Weight 0 | 1
    def get_quantity(
            self,
            openPrice: Union[int, float],
            openMoney: Union[int, float],
            symbol: str,
            stepSize: str = None,
            leverage: int = 1,
            minQty: str = None,
            maxQty: str = None,
            expire_seconds=60 * 5,
    ) -> dict:
        '''
        :param openPrice: 开仓价格
        :param openMoney: 开仓金额
        :param symbol: 合约产品
        :param stepSize: 订单最小数量间隔
        :param leverage: 杠杆数量
        :param minQty: 最小数量
        :param maxQty: 最大数量
        :param use_cache: 使用缓存获取交易规则和交易对信息
        :param expire_seconds: 缓存过期时间 (秒)

        stepSize minQty maxQty任意为空，通过market.exchangeInfo获取交易规则与交易对信息
        '''
        # stepSize minQty maxQty
        if stepSize in [None, ''] or minQty in [None, ''] or maxQty in [None, '']:
            exchangeInfo = self._market.get_exchangeInfo(
                symbol=symbol,
                expire_seconds=expire_seconds
            )
            if exchangeInfo['code'] != 200:
                return exchangeInfo
            if stepSize in [None, '']:
                stepSize = exchangeInfo['data']['filter']['LOT_SIZE']['stepSize']
            if minQty in [None, '']:
                minQty = exchangeInfo['data']['filter']['LOT_SIZE']['minQty']
            if maxQty in [None, '']:
                maxQty = exchangeInfo['data']['filter']['LOT_SIZE']['maxQty']
        # 未圆整的下单数量
        quantity = openMoney * leverage / openPrice
        # 返回圆整结果
        return self.round_quantity(
            quantity=quantity,
            symbol=symbol,
            stepSize=stepSize,
            minQty=minQty,
            maxQty=maxQty,
            expire_seconds=expire_seconds,
        )

    # 将下单数量转化为字符串
    # Weight 0 | 1
    def quantity_to_f(
            self,
            quantity: Union[int, float],
            symbol: str,
            stepSize: str = None,
            expire_seconds=60 * 5,

    ) -> dict:
        '''
        :param quantity: 下单数量
        :param symbol: 合约产品
        :param stepSize: 订单最小数量间隔
        :param use_cache: 使用缓存获取交易规则和交易对信息
        :param expire_seconds: 缓存过期时间 (秒)

        stepSize为空，通过market.exchangeInfo获取交易规则与交易对信息
        '''
        # stepSize
        if stepSize in [None, '']:
            exchangeInfo = self._market.get_exchangeInfo(
                symbol=symbol,
                expire_seconds=expire_seconds
            )
            if exchangeInfo['code'] != 200:
                return exchangeInfo
            stepSize = exchangeInfo['data']['filter']['LOT_SIZE']['stepSize']
        # code : 0 | -1
        quantity_to_f_result = _order.quantity_to_f(
            quantity=quantity,
            stepSize=stepSize,
        )
        # code -> [200,code.QUANTITY_TO_F_ERROR[0]]
        if quantity_to_f_result['code'] == 0:
            quantity_to_f_result['code'] = 200
        else:
            quantity_to_f_result['code'] = code.QUANTITY_TO_F_ERROR[0]
            quantity_to_f_result['msg'] = f'symbol={symbol} ' + quantity_to_f_result['msg']
        return quantity_to_f_result

    # 将价格转化为字符串
    # Weight 0 | 1
    def price_to_f(
            self,
            price: Union[int, float],
            symbol: str,
            tickSize: str = None,
            expire_seconds=60 * 5,
    ) -> dict:
        '''
        :param price: 价格
        :param symbol: 合约产品
        :param tickSize: 订单最小价格间隔
        :param use_cache: 使用缓存获取交易规则和交易对信息
        :param expire_seconds: 缓存过期时间 (秒)

        tickSize为空，通过market.exchangeInfo获取交易规则与交易对信息
        '''
        # tickSize
        if tickSize in [None, '']:
            exchangeInfo = self._market.get_exchangeInfo(
                symbol=symbol,
                expire_seconds=expire_seconds
            )
            if exchangeInfo['code'] != 200:
                return exchangeInfo
            tickSize = exchangeInfo['data']['filter']['PRICE_FILTER']['tickSize']
        # code : 0 | -1
        price_to_f_result = _order.price_to_f(
            price=price,
            tickSize=tickSize
        )
        # code->[200,code.PRICE_TO_F_ERROR[0]]
        if price_to_f_result['code'] == 0:
            price_to_f_result['code'] = 200
        else:
            price_to_f_result['code'] = code.PRICE_TO_F_ERROR[0]
            price_to_f_result['msg'] = f'symbol={symbol} ' + price_to_f_result['msg']
        return price_to_f_result
