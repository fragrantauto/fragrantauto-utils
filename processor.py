import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_operation(max_attempts: int = 3, delay: float = 1.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"attempt {attempt + 1} failed: {e}")
                    time.sleep(delay * (2 ** attempt))
            raise last_exception
        return wrapper
    return decorator

class CryptoProcessor:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    @retry_network_operation(max_attempts=3, delay=2.0)
    def fetch_market_data(self, pair: str):
        logger.info(f"fetching {pair} from {self.endpoint}")
        # network call logic would reside here
        return {"pair": pair, "price": 0.0}