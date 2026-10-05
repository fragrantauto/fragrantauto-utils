import time
import random
import logging
from functools import wraps
from typing import Callable, Any, Tuple, Type

logger = logging.getLogger("fragrantauto.utils")


def retry(
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    tries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    jitter: bool = True,
) -> Callable:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            mdelay = delay
            for attempt in range(1, tries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == tries:
                        logger.error(
                            f"Failed '{func.__name__}' after {tries} attempts. Error: {e}"
                        )
                        raise

                    sleep_time = mdelay
                    if jitter:
                        sleep_time *= random.uniform(0.5, 1.5)

                    logger.warning(
                        f"Retrying '{func.__name__}' in {sleep_time:.2f}s "
                        f"(Attempt {attempt}/{tries}) due to: {e}"
                    )
                    time.sleep(sleep_time)
                    mdelay *= backoff

        return wrapper

    return decorator
