from binance_interface.app.market._base import MarketBase
from typing import Union

__all__ = ['Ticker']


class Ticker(MarketBase):

    # 获取全部产品的最优挂单
    # Weight: 现货 2 合约 5
    def get_bookTickers(self) -> dict:
        '''
        现货
            https://binance-docs.github.io/apidocs/spot/cn/#5393cd07b4
        U本位合约
            https://binance-docs.github.io/apidocs/futures/cn/#5393cd07b4
        币本位合约
            https://binance-docs.github.io/apidocs/delivery/cn/#5393cd07b4
        '''
        return self.marketAPI.get_ticker_bookTicker()

    # 获取全部产品的最优挂单 （字典格式）
    # Weight: 现货 2 合约 5
    def get_bookTickersMap(self) -> dict:
        get_bookTickers_result = self.get_bookTickers()
        # [ERROR RETURN] 数据异常
        if get_bookTickers_result['code'] != 200:
            return get_bookTickers_result
        data_map = {}
        for ticker in get_bookTickers_result['data']:
            symbol = ticker['symbol']
            data_map[symbol] = ticker

        get_bookTickers_result['data'] = data_map
        return get_bookTickers_result

    # 获取一个产品的最优挂单
    # Weight: 现货 1 合约 2
    def get_bookTicker(self, symbol: str) -> dict:
        '''
        现货
            https://binance-docs.github.io/apidocs/spot/cn/#5393cd07b4
        U本位合约
            https://binance-docs.github.io/apidocs/futures/cn/#5393cd07b4
        币本位合约
            https://binance-docs.github.io/apidocs/delivery/cn/#5393cd07b4
        :param symbol: 产品
        '''
        return self.marketAPI.get_ticker_bookTicker(symbol=symbol)

    # 获取全部产品的最新价格
    # Weight: 2
    def get_tickerPrices(self):
        '''
        现货
            https://binance-docs.github.io/apidocs/spot/cn/#8ff46b58de
        U本位合约
            https://binance-docs.github.io/apidocs/futures/cn/#8ff46b58de
        币本位合约
            https://binance-docs.github.io/apidocs/delivery/cn/#8ff46b58de
        '''
        return self.marketAPI.get_ticker_price(symbol='')

    # 获取全部产品的最新价格 (字典格式)
    # Weight: 2
    def get_tickerPricesMap(self):
        get_tickerPrices_result = self.get_tickerPrices()
        # [ERROR RETURN] 数据异常
        if get_tickerPrices_result['code'] != 200:
            return get_tickerPrices_result
        data_map = {}
        for ticker in get_tickerPrices_result['data']:
            symbol = ticker['symbol']
            data_map[symbol] = ticker

        get_tickerPrices_result['data'] = data_map
        return get_tickerPrices_result

    # 获取一个产品的最新价格
    # Weight: 1
    def get_tickerPrice(self, symbol: str):
        '''
        现货
            https://binance-docs.github.io/apidocs/spot/cn/#8ff46b58de
        U本位合约
            https://binance-docs.github.io/apidocs/futures/cn/#8ff46b58de
        币本位合约
            https://binance-docs.github.io/apidocs/delivery/cn/#8ff46b58de
        :param symbol: 产品
        '''
        return self.marketAPI.get_ticker_price(symbol=symbol)

    def get_depth(self, symbol: str, limit: Union[int, str] = ''):
        '''
        现货
            https://binance-docs.github.io/apidocs/spot/cn/#38a975b802
        U本位合约
            https://binance-docs.github.io/apidocs/futures/cn/#38a975b802
        币本位合约
            https://binance-docs.github.io/apidocs/delivery/cn/#38a975b802
        :param symbol: 产品
        :param limit: 数量
        '''
        return self.marketAPI.get_depth(symbol=symbol, limit=limit)
