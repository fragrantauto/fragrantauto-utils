import time
import functools
from typing import Callable, Any, Type, Tuple

def retry(exceptions: Tuple[Type[Exception], ...], max_retries: int = 3, delay: float = 1.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_retries - 1:
                        time.sleep(delay * (2 ** attempt))
            raise last_exception
        return wrapper
    return decorator