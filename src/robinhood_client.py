import os
import pyotp
import robin_stocks.robinhood as r
from dotenv import load_dotenv

load_dotenv()


class RobinhoodClient:
    """Robinhood client"""

    def __init__(self):
        """Init"""
        username = os.environ.get("ROBINHOOD_USERNAME")
        password = os.environ.get("ROBINHOOD_PASSWORD")
        mfa_totp_key = os.environ.get("MFA_TOTP_KEY")
        totp  = pyotp.TOTP(mfa_totp_key).now()
        r.login(username, password, mfa_code=totp)

    def get_stock_data(self):
        """Get stock data"""
        return r.build_holdings()

    def get_crypto_data(self):
        """Get crypto data"""
        return r.crypto.get_crypto_positions()
