from src.crypto_bot.utils import _retrieve_headers


def test_headers():
    header1 = _retrieve_headers()
    header2 = _retrieve_headers()

    assert type(header1) is str
    assert type(header2) is str
    assert len(header1) > 0
    assert len(header2) > 0
    assert header1 != header2
