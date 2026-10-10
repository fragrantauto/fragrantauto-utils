import logging
import sys
from typing import Optional

class CryptoLogger:
    """Standardized logging for crypto trading utilities."""

    def __init__(self, name: str, level: int = logging.INFO) -> None:
        self.logger: logging.Logger = logging.getLogger(name)
        self.logger.setLevel(level)
        handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
        formatter: logging.Formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        """Log informational messages."""
        self.logger.info(message)

    def error(self, message: str, exc_info: Optional[Exception] = None) -> None:
        """Log error messages with optional exception details."""
        self.logger.error(message, exc_info=exc_info)

    def warning(self, message: str) -> None:
        """Log warning level messages."""
        self.logger.warning(message)

def get_logger(name: str) -> "CryptoLogger":
    """Factory function for creating logger instances."""
    return CryptoLogger(name)