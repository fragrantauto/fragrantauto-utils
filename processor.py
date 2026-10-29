import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_call(max_retries: int = 3, delay: float = 1.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"attempt {attempt + 1} failed: {e}")
                    time.sleep(delay * (2 ** attempt))
            raise last_exception
        return wrapper
    return decorator

@retry_network_call(max_retries=3, delay=2.0)
def fetch_price_data(ticker: str) -> dict:
    # implementation for fetching crypto prices
    return {"symbol": ticker, "price": 0.0}
