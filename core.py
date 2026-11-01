import functools
import logging
import random
import time
from typing import Any, Callable, Tuple, Type

logger = logging.getLogger("fragrantauto")


class NetworkRetryError(Exception):
    pass


def retry_on_network_failure(
    max_retries: int = 4,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    jitter: bool = True,
    retryable_exceptions: Tuple[Type[Exception], ...] = (Exception,),
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except retryable_exceptions as exc:
                    if attempt == max_retries:
                        logger.error("Max retries (%d) reached for %s", max_retries, func.__name__)
                        raise NetworkRetryError(f"Operation {func.__name__} failed: {exc}") from exc
                    sleep_time = delay + (random.uniform(0, 0.1 * delay) if jitter else 0)
                    logger.warning(
                        "Attempt %d/%d for %s failed (%s). Retrying in %.2fs...",
                        attempt, max_retries, func.__name__, exc, sleep_time
                    )
                    time.sleep(sleep_time)
                    delay *= backoff_factor

        return wrapper
    return decorator
