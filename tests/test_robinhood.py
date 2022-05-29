"""Test robinhood"""
from src.robinhood_client import RobinhoodClient


def test_robinhood_client():
    """Test robinhood client"""
    robinhood_client = RobinhoodClient()
    data = robinhood_client.get_stock_data()
    assert len(data.items()) > 0
