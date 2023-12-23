from typing import Literal, Union
import traceback
from threading import Thread
from paux.digit import origin_float, origin_int
from binance_interface.app import code
from binance_interface.app import exception
from binance_interface.app.trade.trade_cm.order import TradeOrder
from binance_interface.app.trade.trade_cm.quantity_and_price import TradeQuantityAndPrice



class TradeClose(TradeOrder, TradeQuantityAndPrice):
    # 限价单卖出 Weight > 1
    def close_limit(
            self,
            symbol: str,
            marginType: Literal['ISOLATED', 'CROSSED'],
            positionSide: Literal['LONG', 'SHORT'],
            closePrice: Union[int, float, str, origin_float, origin_int, None] = None,
            tpRate: Union[int, float, None] = None,
            quantity: Union[int, float, str, origin_float, origin_int] = 'all',
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
        :param symbol: 产品
        :param marginType: 保证金模式
            ISOLATED:   逐仓
            CROSSED:    全仓
        :param positionSide: 持仓方向
            LONG:   多单
            SHORT:  空单
        :param closePrice: 平仓价格
        :param tpRate: 挂单止盈率
            closePrice和tpRate不能同时为空
            优先级 closePrice >> tpRate
            closePrice为空，tpRate不为空，会计算出挂单价格
                平多  closePrice = askPrice * (1 + abs(tpRate))
                平空  closePrice = bidPrice * (1 - abs(tpRate))
        :param quantity: 下单数量，支持类型：字符串、普通数值、origin类型
            1. 字符串:
                - 'all'       获取产品全部可卖出数量
                - 数值型字符串  不会进行quantity的圆整
            2. 普通数值:   圆整后转换为字符串
            3. origin:   使用quantity.origin()
        :param meta: 回调函数传递参数
        :param block: 是否堵塞
        :param timeout: 订单超时时间 （秒)
        :param delay: 检测订单状态的间隔 (秒)
        :param cancel: 未完全成交是否取消订单
        :param newClientOrderId: 客户自定义订单ID
        :param newThread: 是否开启新线程执行
        :param callback: 非执行异常的回调函数
        :param errorback: 执行异常的回调函数
        '''
        # 常量参数
        TYPE = 'LIMIT'
        TIMEINFORCE = 'GTC'
        positionSide = positionSide.upper()
        marginType = marginType.upper()
        # 记录信息
        information = {
            'symbol': symbol,
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
            closePrice=closePrice,
            tpRate=tpRate,
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
                closePrice=closePrice,
                tpRate=tpRate,
                quantity=quantity,
                newClientOrderId=newClientOrderId,
                block=block,
                timeout=timeout,
                delay=delay,
                cancel=cancel,
        ):
            # 根据positionSide调整方向
            if positionSide == 'LONG':
                side = 'SELL'
            elif positionSide == 'SHORT':
                side = 'BUY'
            else:
                raise exception.ParamPositionSideException(positionSide)
            # SellLine
            if closePrice in [None, ''] and tpRate in [None, '']:
                msg = 'closePrice and tpRate can not be empty together'
                raise exception.ParamException(msg)
            # 【卖出价格】 closePrice closePrice_f
            # 字符串
            if isinstance(closePrice, str):
                closePrice_f = closePrice
                closePrice = float(closePrice)
            # origin
            elif isinstance(closePrice, origin_float) or isinstance(closePrice, origin_int):
                closePrice_f = closePrice.origin()
                closePrice = closePrice
            # 数字对象和None
            else:
                # 如果没有closePrice，根据tpRate计算closePrice
                if not closePrice:
                    get_bookTicker_result = self._market.get_bookTicker(symbol)
                    # [ERROR RETURN]
                    if get_bookTicker_result['code'] != 200:
                        return get_bookTicker_result
                    # 多单选择最佳卖出价格作为开仓价
                    if positionSide == 'LONG':
                        askPrice = get_bookTicker_result['data']['askPrice']
                        askPrice = float(askPrice)
                        closePrice = askPrice * (1 + abs(tpRate))
                    # 空单选择最佳买入价格作为开仓价
                    else:
                        bidPrice = get_bookTicker_result['data']['bidPrice']
                        bidPrice = float(bidPrice)
                        closePrice = bidPrice * (1 - abs(tpRate))
                # 圆整 -> closePrice
                round_price_result = self.round_price(
                    price=closePrice,
                    symbol=symbol,
                    type='CEIL' if positionSide == 'LONG' else 'FLOOR'
                )
                # [ERROR RETURN]
                if round_price_result['code'] != 200:
                    return round_price_result
                closePrice = round_price_result['data']
                # 转化为字符串 closePrice_f
                closePrice_f_result = self.price_to_f(
                    price=closePrice,
                    symbol=symbol,
                )
                # [ERROR RETURN]
                if closePrice_f_result['code'] != 200:
                    return closePrice_f_result
                closePrice_f = closePrice_f_result['data']
            # 【平仓数量】 quantity quantity_f
            # 全部
            if quantity == 'all':
                get_position_result = self._account.get_position(symbol=symbol)
                if get_position_result['code'] != 200:
                    return get_position_result
                # 持仓数量 发送的平仓数量可以超过现有的可平仓数量
                # 例如持有100BTC，正在平仓20BTC，查询到的positionAmt = 100，再发送平仓100BTC，只会平仓80BTC
                positionAmt = get_position_result['data'][marginType][positionSide]['positionAmt']
                round_quantity_result = self.round_quantity(
                    quantity=float(positionAmt),
                    symbol=symbol,
                )
                # [ERROR RETURN]
                if round_quantity_result['code'] != 200:
                    return round_quantity_result
                quantity = round_quantity_result['data']
                quantity_to_f_result = self.quantity_to_f(
                    quantity=quantity,
                    symbol=symbol,
                )
                # [ERROR RETURN]
                if quantity_to_f_result['code'] != 200:
                    return quantity_to_f_result
                quantity_f = quantity_to_f_result['data']
            # 数值字符串
            elif isinstance(quantity, str):
                quantity_f = quantity
                quantity = float(quantity)
            # origin
            elif isinstance(quantity, origin_float) or isinstance(quantity, origin_int):
                quantity_f = quantity.origin()
            # 数字对象 圆整 转化为字符串
            else:
                round_quantity_result = self.round_quantity(quantity=quantity, symbol=symbol)
                # [ERROR RETURN]
                if round_quantity_result['code'] != 200:
                    return round_quantity_result
                quantity = round_quantity_result['data']
                quantity_to_f_result = self.quantity_to_f(quantity=quantity, symbol=symbol)
                # [ERROR RETURN]
                if quantity_to_f_result['code'] != 200:
                    return quantity_to_f_result
                quantity_f = quantity_to_f_result['data']
            # 设置全仓|逐仓模式
            set_margin_type_result = self._account.set_marginType(symbol=symbol, marginType=marginType)
            # [ERROR RETURN]
            if set_margin_type_result['code'] != 200:
                return set_margin_type_result
            request_param = dict(
                symbol=symbol,
                side=side,
                positionSide=positionSide,
                type=TYPE,
                quantity=quantity_f,
                price=closePrice_f,
                newClientOrderId=newClientOrderId,
                timeInForce=TIMEINFORCE,
            )
            information['request_param'] = request_param
            set_order_result = self.set_order(**request_param)
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
            closePrice=closePrice,
            tpRate=tpRate,
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

    # 市价单卖出 Weight > 1
    def close_market(
            self,
            symbol: str,
            marginType: Literal['ISOLATED', 'CROSSED'],
            positionSide: Literal['LONG', 'SHORT'],
            quantity: Union[int, float, str, origin_float, origin_int] = 'all',
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
            例如symbol='BTCUSDT' 其中的基础货币base_asset为'USDT'
            仅在quantity = 'all' 的时候需要填写
        :param quantity: 下单数量，支持类型：字符串、普通数值、origin类型
            1. 字符串:
                - 'all'       获取产品全部可卖出数量
                - 数值型字符串  不会进行quantity的圆整
            2. 普通数值:   圆整后转换为字符串
            3. origin:   使用quantity.origin()
        :param meta: 回调函数传递参数
        :param timeout: 订单超时时间 （秒)
        :param delay: 检测订单状态的间隔 (秒)
        :param cancel: 未完全成交是否取消订单
        :param newClientOrderId: 客户自定义订单ID
        :param newThread: 是否开启新线程执行
        :param callback: 非执行异常的回调函数
        :param errorback: 执行异常的回调函数
        '''
        # 常量参数
        TYPE = 'MARKET'
        positionSide = positionSide.upper()
        marginType = marginType.upper()

        # 记录信息
        information = {
            'symbol': symbol,
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
                quantity=quantity,
                newClientOrderId=newClientOrderId,
                timeout=timeout,
                delay=delay,
                cancel=cancel,
        ):
            # 根据positionSide调整方向
            if positionSide == 'LONG':
                side = 'SELL'
            elif positionSide == 'SHORT':
                side = 'BUY'
            else:
                raise exception.ParamPositionSideException(positionSide)
            # 【平仓数量】 quantity quantity_f
            # 全部
            if quantity == 'all':
                get_position_result = self._account.get_position(symbol=symbol)
                # [ERROR RETURN]
                if get_position_result['code'] != 200:
                    return get_position_result
                # 持仓数量
                positionAmt = get_position_result['data'][marginType][positionSide]['positionAmt']
                round_quantity_result = self.round_quantity(
                    quantity=float(positionAmt),
                    symbol=symbol,
                )
                # [ERROR RETURN]
                if round_quantity_result['code'] != 200:
                    return round_quantity_result
                quantity = round_quantity_result['data']
                quantity_to_f_result = self.quantity_to_f(
                    quantity=quantity,
                    symbol=symbol,
                )
                # [ERROR RETURN]
                if quantity_to_f_result['code'] != 200:
                    return quantity_to_f_result
                quantity_f = quantity_to_f_result['data']
            # 数值字符串
            elif isinstance(quantity, str):
                quantity_f = quantity
                quantity = float(quantity)
            # 数值
            else:
                # 圆整 -> quantity
                round_quantity_result = self.round_quantity(quantity=quantity, symbol=symbol)
                # [ERROR RETURN]
                if round_quantity_result['code'] != 200:
                    return round_quantity_result
                quantity = round_quantity_result['data']
                # 转化为字符串 -> quantity_f
                quantity_f_result = self.quantity_to_f(
                    quantity=quantity,
                    symbol=symbol,
                )
                # [ERROR RETURN]
                if quantity_f_result['code'] != 200:
                    return quantity_f_result
                quantity_f = quantity_f_result['data']
            # 设置全仓|逐仓模式
            set_margin_type_result = self._account.set_marginType(symbol=symbol, marginType=marginType)
            if set_margin_type_result['code'] != 200:
                return set_margin_type_result

            request_param = dict(
                symbol=symbol,
                side=side,
                positionSide=positionSide,
                type=TYPE,
                quantity=quantity_f,
                newClientOrderId=newClientOrderId,
            )
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
