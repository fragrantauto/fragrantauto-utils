import logging
import sys
from typing import Optional

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Initialize and return a configured logger instance."""
    logger: logging.Logger = logging.getLogger(name)
    logger.setLevel(level)
    
    formatter: logging.Formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    
    console_handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(console_handler)
        
    return logger

class CryptoLogger:
    """Wrapper for consistent crypto utility logging."""
    def __init__(self, name: str, level: Optional[int] = None) -> None:
        self.logger: logging.Logger = get_logger(name, level or logging.INFO)

    def info(self, msg: str) -> None:
        """Log informational messages."""
        self.logger.info(msg)

    def error(self, msg: str) -> None:
        """Log error messages."""
        self.logger.error(msg)