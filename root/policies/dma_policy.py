
from .base_policy import *
import talib


@Policy.register('DMA', PolicyLifetime_EachCode)
class DMAPolicy(Policy):
    """
    双均线策略
    """

    def handle(self, context):
        for code in context.get_codes():
            data = context.get_k_data(code)
            ma5 = talib.MA(data.close.values, timeperiod=5)
            ma60 = talib.MA(data.close.values, timeperiod=10)

            diff = ma5[-1] - ma60[-1]
            close = data.close.values[-1]
            # print(diff)
            return diff, close
