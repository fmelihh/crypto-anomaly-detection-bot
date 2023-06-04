from src.crypto_bot.binance_api import request_to_binance_api


def test_request_binance_api():
    resp = request_to_binance_api()
    assert type(resp) is dict
