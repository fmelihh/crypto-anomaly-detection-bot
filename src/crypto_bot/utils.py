import requests
from fake_useragent import UserAgent
from requests.adapters import HTTPAdapter, Retry

user_agent_generator = UserAgent()


def retrieve_session(retry_count: int = 5) -> requests.Session:
    retry_strategy = Retry(
        total=retry_count,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    s = requests.Session()
    s.headers["User-Agent"] = _retrieve_headers()
    s.mount('http://', HTTPAdapter(max_retries=retry_strategy))
    return s


def _retrieve_headers() -> str:
    return user_agent_generator.random


__all__ = ["retrieve_session"]
