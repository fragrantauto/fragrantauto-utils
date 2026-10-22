import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry(max_retries: int = 3, delay: float = 1.0, backoff: int = 2):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            retries = 0
            current_delay = delay
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    retries += 1
                    if retries >= max_retries:
                        logger.error(f"failed after {max_retries} attempts: {e}")
                        raise
                    logger.warning(f"retry {retries}/{max_retries} due to {e}")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator