import asyncio
import functools
import logging
import random
import time
from typing import Any, Callable, Type, Union

logger = logging.getLogger("fragrantauto.utils")


def retry_network_op(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: Union[Type[Exception], tuple[Type[Exception], ...]] = Exception,
) -> Callable:
    def decorator(func: Callable) -> Callable:
        if asyncio.iscoroutinefunction(func):

            @functools.wraps(func)
            async def async_wrapper(*args: Any, **kwargs: Any) -> Any:
                delay = initial_delay
                for attempt in range(1, max_retries + 1):
                    try:
                        return await func(*args, **kwargs)
                    except exceptions as err:
                        if attempt == max_retries:
                            raise err
                        jitter = random.uniform(0, 0.1 * delay)
                        await asyncio.sleep(delay + jitter)
                        delay *= backoff_factor

            return async_wrapper
        else:

            @functools.wraps(func)
            def sync_wrapper(*args: Any, **kwargs: Any) -> Any:
                delay = initial_delay
                for attempt in range(1, max_retries + 1):
                    try:
                        return func(*args, **kwargs)
                    except exceptions as err:
                        if attempt == max_retries:
                            raise err
                        jitter = random.uniform(0, 0.1 * delay)
                        time.sleep(delay + jitter)
                        delay *= backoff_factor

            return sync_wrapper

    return decorator
