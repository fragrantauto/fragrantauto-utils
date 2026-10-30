import time
import functools
from typing import Callable, Any, Type

def with_retry(
    exceptions: tuple[Type[Exception], ...],
    max_retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            retries = 0
            current_delay = delay
            while True:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    retries += 1
                    if retries > max_retries:
                        raise e
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator