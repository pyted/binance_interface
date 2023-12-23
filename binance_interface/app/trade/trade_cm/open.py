from typing import Literal, Union
import traceback
from threading import Thread
from paux.digit import origin_float, origin_int
from binance_interface.app import code
from binance_interface.app import exception
from binance_interface.app.trade.trade_cm.order import TradeOrder
from binance_interface.app.trade.trade_cm.quantity_and_price import TradeQuantityAndPrice




class TradeOpen(TradeOrder, TradeQuantityAndPrice):

    # 限价单购买 Weight > 1
    def open_limit(
            self,
            symbol: str,
            openPrice: Union[int, float, str, origin_float, origin_int],
            marginType: Literal['ISOLATED', 'CROSSED'],
            positionSide: Literal['LONG', 'SHORT'],
            leverage: int = 1,
            openMoney: Union[int, float, None] = None,
            quantity: Union[int, float, str, origin_float, origin_int, None] = None,
            meta: dict = {},
            block: bool = True,
            timeout: Union[int, float] = 60,
            delay: Union[int, float] = 0.2,
            cancel: bool = True,
            newClientOrderId: str = '',
            newThread: bool = False,
            callback: object = None,
            errorback: object = None,
    ) -> dict:
        '''
        :param symbol: 合约产品
        :param openPrice: 开仓价格
        :param marginType: 保证金模式
            ISOLATED:   逐仓
            CROSSED:    全仓
        :param positionSide: 持仓方向
            LONG:   多单
            SHORT:  空单
        :param leverage: 杠杆倍数
        :param openMoney: 开仓金额
        :param quantity: 下单数量
        :param meta: 回调函数传递参数
        :param block: 是否堵塞
        :param timeout: 订单超时时间 （秒)
        :param delay: 检测订单状态的间隔 (秒)
        :param cancel: 未完全成交是否取消订单
        :param newClientOrderId: 客户自定义订单ID
        :param newThread: 是否开启新线程执行
        :param callback: 非执行异常的回调函数
        :param errorback: 执行异常的回调函数

        openPrice与quantity
            如果是字符串类型，会跳过圆整函数
            如果是origin_float或origin_int类型，会使用origin()的字符串作为下单参数数值
            如果是其他的数字类型，包括int、float、np.float均会先进行圆整，后转化为字符串作为下单参数

        quantity如果为None，会按照开仓价格openPrice、开仓金额openMoney与杠杆倍数leverage计算可以下单的quantity数量
        quantity与openMoney不能同时为None
        '''
        # 常量参数
        TYPE = 'LIMIT'
        TIMEINFORCE = 'GTC'
        positionSide = positionSide.upper()
        marginType = marginType.upper()

        # 记录信息
        information = {
            'symbol':symbol,
            'status': None,
            'meta': None,
            'request_param': None,
            'func_param': None,
            'get_order_result': None,
            'set_order_result': None,
            'error_result': None,
            'cancel_result': None,
        }
        # 函数的参数
        information['func_param'] = dict(
            symbol=symbol,
            openPrice=openPrice,
            positionSide=positionSide,
            marginType=marginType,
            leverage=leverage,
            openMoney=openMoney,
            quantity=quantity,
            meta=meta,
            block=block,
            timeout=timeout,
            delay=delay,
            cancel=cancel,
            newClientOrderId=newClientOrderId,
            newThread=newThread,
            callback=callback,
            errorback=errorback,
        )
        # meta
        information['meta'] = meta

        def main_func(
                symbol=symbol,
                positionSide=positionSide,
                marginType=marginType,
                leverage=leverage,
                openPrice=openPrice,
                openMoney=openMoney,
                quantity=quantity,
                newClientOrderId=newClientOrderId,
                block=block,
                timeout=timeout,
                delay=delay,
                cancel=cancel,
        ):
            # 根据positionSide调整方向
            if positionSide == 'LONG':
                side = 'BUY'
            elif positionSide == 'SHORT':
                side = 'SELL'
            else:
                raise exception.ParamPositionSideException(positionSide)
            # 【开仓数量】 -> openPrice openPrice_f
            # 字符串
            if isinstance(openPrice, str):
                openPrice_f = openPrice
                openPrice = float(openPrice)
            # origin
            elif isinstance(openPrice, origin_float) or isinstance(openPrice, origin_int):
                openPrice_f = openPrice.origin()
                openPrice = openPrice
            # 数字对象
            else:
                # 圆整 -> openPrice
                round_price_result = self.round_price(
                    price=openPrice,
                    symbol=symbol,
                    type='FLOOR' if positionSide == 'LONG' else 'CEIL',
                )
                # [ERROR RETURN]
                if round_price_result['code'] != 200:
                    return round_price_result
                # 转化为字符串 -> openPrice_f
                openPrice = round_price_result['data']
                openPrice_f_result = self.price_to_f(price=openPrice, symbol=symbol)
                # [ERROR RETURN]
                if openPrice_f_result['code'] != 200:
                    return openPrice_f_result
                openPrice_f = openPrice_f_result['data']
            # 【购买数量】 quantity quantity_f
            # 字符串
            if isinstance(quantity, str):
                quantity_f = quantity
                quantity = float(quantity)
            # origin
            elif isinstance(quantity, origin_float) or isinstance(quantity, origin_int):
                quantity_f = quantity.origin()
            # 数字对象和None
            else:
                # None 通过openMoney获取quantity
                if quantity == None:
                    get_quantity_result = self.get_quantity(
                        openPrice=openPrice, openMoney=openMoney,
                        leverage=leverage, symbol=symbol
                    )
                    # [ERROR RETURN]
                    if get_quantity_result['code'] != 200:
                        return get_quantity_result
                    quantity = get_quantity_result['data']
                # 数字对象 圆整quantity
                else:
                    round_quantity_result = self.round_quantity(
                        quantity=quantity, symbol=symbol
                    )
                    # [ERROR RETURN]
                    if round_quantity_result['code'] != 200:
                        return round_quantity_result
                    quantity = round_quantity_result['data']
                # 转化为字符串 -> quantity_f
                quantity_f_result = self.quantity_to_f(quantity=quantity, symbol=symbol)
                # [ERROR RETURN]
                if quantity_f_result['code'] != 200:
                    return quantity_f_result
                quantity_f = quantity_f_result['data']

            # 设置全仓|逐仓模式
            set_margin_type_result = self._account.set_marginType(symbol=symbol, marginType=marginType)
            # [ERROR RETURN]
            if set_margin_type_result['code'] != 200:
                return set_margin_type_result
            # 设置杠杆
            set_leverage_result = self._account.set_leverage(symbol=symbol, leverage=leverage)
            # [ERROR RETURN]
            if set_leverage_result['code'] != 200:
                return set_leverage_result
            request_param = dict(
                symbol=symbol,
                side=side,
                positionSide=positionSide,
                type=TYPE,
                quantity=quantity_f,
                price=openPrice_f,
                newClientOrderId=newClientOrderId,
                timeInForce=TIMEINFORCE,
            )
            information['request_param'] = request_param
            set_order_result = self.set_order(**request_param)  # 下单
            information['set_order_result'] = set_order_result
            # [ERROR RETURN]
            if set_order_result['code'] != 200:
                return set_order_result
            # 是否时堵塞模式
            if not block:
                return None

            orderId = set_order_result['data']['orderId']
            order_result = self.wait_order_FILLED(
                symbol=symbol,
                orderId=orderId,
                timeout=timeout,
                delay=delay,
            )
            information['get_order_result'] = order_result
            information['status'] = order_result['data']['status']

            if order_result['data']['status'] == self.ORDER_STATUS.FILLED:
                # [SUC RETURN]
                return None
            if cancel:
                # 订单取消失败
                cancel_order_result = self.cancel_order(symbol=symbol, orderId=orderId)
                information['cancel_result'] = cancel_order_result
                if cancel_order_result['code'] != 200:
                    return cancel_order_result
                # 查看订单结果
                get_order_result = self.get_order(
                    symbol=symbol, orderId=orderId
                )
                if get_order_result['code'] != 200:
                    return get_order_result
                information['get_order_result'] = get_order_result
                information['status'] = get_order_result['data']['status']
            return None

        main_data = dict(
            symbol=symbol,
            openPrice=openPrice,
            positionSide=positionSide,
            marginType=marginType,
            leverage=leverage,
            openMoney=openMoney,
            quantity=quantity,
            newClientOrderId=newClientOrderId,
            block=block,
            timeout=timeout,
            delay=delay,
            cancel=cancel,
        )

        def inner_func():
            try:
                error_result = main_func(**main_data)
                information['error_result'] = error_result
            except:
                error_msg = str(traceback.format_exc())
                error_result = {
                    'code': code.FUNC_EXCEPTION[0],
                    'data': {},
                    'msg': error_msg,
                }
                information['error_result'] = error_result

            if information['error_result']:
                if errorback:
                    errorback(information)
            else:
                if callback:
                    callback(information)
            return information

        if newThread == False:
            return inner_func()
        else:
            t = Thread(target=inner_func)
            t.start()
            return t

    # 市价单购买 Weight > 1
    def open_market(
            self,
            symbol: str,
            marginType: Literal['ISOLATED', 'CROSSED'],
            positionSide: Literal['LONG', 'SHORT'],
            openMoney: Union[int, float, None] = None,
            leverage: int = 1,
            quantity: Union[int, float, str, origin_float, origin_int] = None,
            meta: dict = {},
            timeout: Union[int, float] = 60,
            delay: Union[int, float] = 0.2,
            cancel: bool = True,
            newClientOrderId: str = '',
            newThread: bool = False,
            callback: object = None,
            errorback: object = None,
    ) -> dict:
        '''
        :param symbol: 产品
        :param marginType: 保证金模式
            ISOLATED:   逐仓
            CROSSED:    全仓
        :param positionSide: 持仓方向
            LONG:   多单
            SHORT:  空单
        :param openMoney: 购买金额
        :param leverage: 杠杆倍数
        :param quantity: 下单数量
        :param meta: 回调函数传递参数
        :param timeout: 订单超时时间 （秒)
        :param delay: 检测订单状态的间隔 (秒)
        :param cancel: 未完全成交是否取消订单
        :param newClientOrderId: 客户自定义订单ID
        :param newThread: 是否开启新线程执行
        :param callback: 非执行异常的回调函数
        :param errorback: 执行异常的回调函数

        quantity
            如果是字符串类型，会跳过圆整函数
            如果是origin_float或origin_int类型，会使用origin()的字符串作为下单参数数值
            如果是其他的数字类型，包括int、float、np.float均会先进行圆整，后转化为字符串作为下单参数
            如果为None，会选择当前最优的购买价格openPrice、再通过购买金额openMoney计算可以下单的quantity数量
        quantity与openMoney不能同时为None
        '''
        # 常量参数
        TYPE = 'MARKET'
        positionSide = positionSide.upper()
        marginType = marginType.upper()
        # 记录信息
        information = {
            'symbol':symbol,
            'status': None,
            'meta': None,
            'request_param': None,
            'func_param': None,
            'get_order_result': None,
            'set_order_result': None,
            'error_result': None,
            'cancel_result': None,
        }
        # 函数的参数
        information['func_param'] = dict(
            symbol=symbol,
            positionSide=positionSide,
            marginType=marginType,
            openMoney=openMoney,
            leverage=leverage,
            quantity=quantity,
            meta=meta,
            timeout=timeout,
            delay=delay,
            cancel=cancel,
            newClientOrderId=newClientOrderId,
            newThread=newThread,
            callback=callback,
            errorback=errorback,
        )
        # meta
        information['meta'] = meta

        def main_func(
                symbol=symbol,
                positionSide=positionSide,
                marginType=marginType,
                openMoney=openMoney,
                leverage=leverage,
                quantity=quantity,
                newClientOrderId=newClientOrderId,
                timeout=timeout,
                delay=delay,
                cancel=cancel,
        ):
            # 根据positionSide调整方向
            if positionSide == 'LONG':
                side = 'BUY'
            elif positionSide == 'SHORT':
                side = 'SELL'
            else:
                raise exception.ParamPositionSideException(positionSide)
            # 【购买数量】 quantity quantity_f
            # 字符串
            if isinstance(quantity, str):
                quantity_f = quantity
                quantity = float(quantity)
            # origin
            elif isinstance(quantity, origin_float) or isinstance(quantity, origin_int):
                quantity_f = quantity.origin()
                quantity = quantity
            # 数字对象和None
            else:
                # None 按照最优购买价格 计算下单数量
                if quantity == None:
                    get_bookTicker_result = self._market.get_bookTicker(symbol=symbol)
                    # [ERROR RETURN]
                    if get_bookTicker_result['code'] != 200:
                        return get_bookTicker_result
                    # 多单选择最佳卖出价格作为开仓价
                    if positionSide == 'LONG':
                        openPrice = origin_float(get_bookTicker_result['data']['askPrice'])
                    # 空单选择最佳买入价格作为开仓价
                    else:
                        openPrice = origin_float(get_bookTicker_result['data']['bidPrice'])
                    get_quantity_result = self.get_quantity(
                        openPrice=openPrice, openMoney=openMoney,
                        leverage=leverage, symbol=symbol
                    )
                    # [ERROR RETURN]
                    if get_quantity_result['code'] != 200:
                        return get_quantity_result
                    quantity = get_quantity_result['data']
                # 数字对象 圆整下单数量
                else:
                    round_quantity_result = self.round_quantity(
                        quantity=quantity,
                        symbol=symbol
                    )
                    if round_quantity_result['code'] != 200:
                        # [ERROR RETURN]
                        return round_quantity_result
                    quantity = round_quantity_result['data']
                # 下单数量转化为字符串
                quantity_f_result = self.quantity_to_f(quantity=quantity, symbol=symbol)
                # [ERROR RETURN]
                if quantity_f_result['code'] != 200:
                    return quantity_f_result
                quantity_f = quantity_f_result['data']

            # 设置全仓|逐仓模式
            set_margin_type_result = self._account.set_marginType(symbol=symbol, marginType=marginType)
            if set_margin_type_result['code'] != 200:
                return set_margin_type_result
            # 设置杠杆
            set_leverage_result = self._account.set_leverage(symbol=symbol, leverage=leverage)
            if set_leverage_result['code'] != 200:
                return set_leverage_result

            request_param = dict(
                symbol=symbol,
                side=side,
                positionSide=positionSide,
                type=TYPE,
                quantity=quantity_f,
                newClientOrderId=newClientOrderId,
            )
            # 购买
            information['request_param'] = request_param
            set_order_result = self.set_order(**request_param)  # 下单
            information['set_order_result'] = set_order_result

            # [ERROR RETURN]
            if set_order_result['code'] != 200:
                return set_order_result

            orderId = set_order_result['data']['orderId']
            order_result = self.wait_order_FILLED(
                symbol=symbol,
                orderId=orderId,
                timeout=timeout,
                delay=delay,
            )

            information['get_order_result'] = order_result
            information['status'] = order_result['data']['status']

            # [SUC RETURN]
            if order_result['data']['status'] == self.ORDER_STATUS.FILLED:
                return None
            if cancel:
                # 订单取消失败
                cancel_order_result = self.cancel_order(symbol=symbol, orderId=orderId)
                information['cancel_result'] = cancel_order_result
                # [ERROR RETURN]
                if cancel_order_result['code'] != 200:
                    return cancel_order_result
                # 查看订单结果
                get_order_result = self.get_order(
                    symbol=symbol, orderId=orderId
                )
                if get_order_result['code'] != 200:
                    return get_order_result
                information['get_order_result'] = get_order_result
                information['status'] = get_order_result['data']['status']
            return None

        main_data = dict(
            symbol=symbol,
            positionSide=positionSide,
            marginType=marginType,
            openMoney=openMoney,
            leverage=leverage,
            quantity=quantity,
            newClientOrderId=newClientOrderId,
            timeout=timeout,
            delay=delay,
            cancel=cancel,
        )

        def inner_func():
            try:
                error_result = main_func(**main_data)
                information['error_result'] = error_result
            except:
                error_msg = str(traceback.format_exc())
                error_result = {
                    'code': code.FUNC_EXCEPTION[0],
                    'data': {},
                    'msg': error_msg,
                }
                information['error_result'] = error_result

            if information['error_result']:
                if errorback:
                    errorback(information)
            else:
                if callback:
                    callback(information)
            return information

        if newThread == False:
            return inner_func()
        else:
            t = Thread(target=inner_func)
            t.start()
            return t
