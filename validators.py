import time
import functools
import logging
from typing import Callable, Any, Type

logger = logging.getLogger(__name__)

def retry_on_failure(exceptions: tuple[Type[Exception], ...], max_retries: int = 3, delay: float = 1.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"attempt {attempt + 1} failed: {e}. retrying...")
                    time.sleep(delay * (2 ** attempt))
            raise last_exception
        return wrapper
    return decorator

def validate_network_response(response: dict) -> bool:
    if not response or "status" not in response:
        return False
    return response.get("status") == "success"