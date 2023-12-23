from binance_interface.app.exception._base import AbstractEXP


# 请求状态码异常
class CodeException(AbstractEXP):
    def __init__(self, msg):
        self.error_msg = msg


# 请求异常
class RequestException(AbstractEXP):
    def __init__(self, msg):
        self.error_msg = msg
