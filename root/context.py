
from .stock_data import *

class Context:
    """
    """

    def __init__(self):
        self.codes = []
        self.code = ""
        self.data = None
        self.time = None
        self.stock_data = StockData()

    def get_codes(self):
        return self.codes

    def set_codes(self, codes):
        self.codes = codes

    def get_k_data(self, code):
        """
        Get K data by code
        """
        k_data = self.stock_data.get_k_data(code)
        if self.time:
            return k_data[k_data.date <= self.time]
        else:
            return k_data

    def get_profile_data(self, date=None):
        if not date:
            date = self.time
        profile_data = self.stock_data.get_profile_data(date)
        return profile_data

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time

    def get_stock_basics(self):
        today = formatted_date(self.get_time())
        return self.stock_data.get_stock_basics(today)