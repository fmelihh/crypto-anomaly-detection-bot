import pytest
import requests.exceptions

from src.crypto_bot.utils import retrieve_session


def test_status_code_200():
    session = retrieve_session()
    response = session.get("https://postman-echo.com/status/200")
    assert response.status_code == 200


def test_timeout():
    session = retrieve_session()
    with pytest.raises(requests.exceptions.Timeout):
        response = session.get("https://postman-echo.com/delay/10", timeout=5)


def test_retry(caplog):
    session = retrieve_session(retry_count=3)
    with pytest.raises(requests.exceptions.ConnectionError):
        session.get("http://this-url-does-not-exist.bar")

    assert "Retry(total=0, " in caplog.records[2].message
    assert "Retry(total=1, " in caplog.records[1].message
    assert "Retry(total=2, " in caplog.records[0].message
