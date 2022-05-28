import os

import robin_stocks.robinhood as r
from dotenv import load_dotenv

load_dotenv()


class RobinhoodClient:
    """Robinhood client"""

    def __init__(self):
        """Init"""
        username = os.environ.get("ROBINHOOD_USERNAME")
        password = os.environ.get("ROBINHOOD_PASSWORD")
        r.login(username, password)

    def get_stock_data(self):
        """Get stock data"""
        return r.build_holdings()
