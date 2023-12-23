from binance_interface.app.exception._base import AbstractEXP


# 规则异常
class RuleException(AbstractEXP):
    def __init__(self, msg):
        self.error_msg = msg
