import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry(retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            local_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == retries - 1:
                        logger.error(f"Final attempt failed: {e}")
                        raise
                    logger.warning(f"Attempt {attempt + 1} failed, retrying in {local_delay}s")
                    time.sleep(local_delay)
                    local_delay *= backoff
        return wrapper
    return decorator

@retry(retries=3, delay=0.5)
def execute_network_request(task: Callable, *args, **kwargs):
    return task(*args, **kwargs)