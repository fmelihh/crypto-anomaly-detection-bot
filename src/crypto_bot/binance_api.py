import json
from loguru import logger
from requests.exceptions import RetryError, Timeout, HTTPError

from .utils import retrieve_session

API_URL = "https://api.binance.com/api/v3/ticker/price"


def request_to_binance_api():
    try:
        session = retrieve_session()
        res = session.get(API_URL)
        return json.loads(res.text)
    except RetryError as err:
        logger.exception("retry err: ", str(err))
    except Timeout as err:
        logger.exception("timeout err: ", str(err))
    except HTTPError as err:
        logger.exception("http err: ", err.response.status_code, str(err))
    except Exception as err:
        logger.exception("unidentified err: ", str(err))
