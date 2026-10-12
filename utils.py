import asyncio
import functools
import logging
import random
from typing import Any, Callable, Tuple, Type, Union

logger = logging.getLogger(__name__)


def retry_async(
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    jitter: bool = True,
    exceptions: Union[Type[Exception], Tuple[Type[Exception], ...]] = (Exception,),
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return await func(*args, **kwargs)
                except exceptions as err:
                    if attempt == retries:
                        logger.error(
                            f"Call to {func.__name__} failed after {retries} attempts: {err}"
                        )
                        raise

                    sleep_time = current_delay
                    if jitter:
                        sleep_time += random.uniform(0, 0.1 * current_delay)

                    logger.warning(
                        f"Attempt {attempt}/{retries} for {func.__name__} failed: {err}. "
                        f"Retrying in {sleep_time:.2f}s..."
                    )
                    await asyncio.sleep(sleep_time)
                    current_delay *= backoff

        return wrapper

    return decorator
