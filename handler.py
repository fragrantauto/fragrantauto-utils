import logging
from typing import Any, Optional

class CryptoHandlerError(Exception):
    pass

class RateLimitError(CryptoHandlerError):
    pass

class InsufficientFundsError(CryptoHandlerError):
    pass

class TransactionProcessor:
    def __init__(self, logger: logging.Logger):
        self.logger = logger

    def execute(self, operation: str, *args: Any) -> Optional[dict]:
        try:
            return self._perform_trade(operation, *args)
        except RateLimitError as e:
            self.logger.warning(f"Rate limit exceeded: {e}")
        except InsufficientFundsError as e:
            self.logger.error(f"Insufficient funds for operation: {e}")
        except Exception as e:
            self.logger.critical(f"Unexpected error during {operation}: {e}")
        return None

    def _perform_trade(self, operation: str, *args: Any) -> dict:
        if not operation:
            raise ValueError("Operation cannot be empty")
        return {"status": "success", "op": operation}