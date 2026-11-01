import logging
import time
from typing import Any, Callable, Optional


class CryptoAPIError(Exception):
    pass


class RateLimitExceededError(CryptoAPIError):
    pass


class InsufficientFundsError(CryptoAPIError):
    pass


class InvalidOrderError(CryptoAPIError):
    pass


class ExecutionHandler:
    def __init__(self, max_retries: int = 3, backoff_factor: float = 1.5):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        self.logger = logging.getLogger(__name__)

    def execute_with_retry(
        self, func: Callable[..., Any], *args: Any, **kwargs: Any
    ) -> Optional[Any]:
        retries = 0
        delay = 1.0

        while retries <= self.max_retries:
            try:
                return func(*args, **kwargs)
            except RateLimitExceededError as err:
                retries += 1
                if retries > self.max_retries:
                    self.logger.error("Max retries exceeded for rate limit")
                    raise err
                self.logger.warning(
                    f"Rate limit hit. Retrying in {delay:.2f}s... (Attempt {retries}/{self.max_retries})"
                )
                time.sleep(delay)
                delay *= self.backoff_factor
            except InsufficientFundsError as err:
                self.logger.critical(f"Order aborted due to funds: {err}")
                raise err
            except InvalidOrderError as err:
                self.logger.error(f"Invalid order parameters: {err}")
                return None
            except Exception as err:
                self.logger.exception(f"Unexpected error during execution: {err}")
                raise CryptoAPIError(f"Unhandled execution failure: {err}") from err

        return None
