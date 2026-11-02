import logging
import sys
from pathlib import Path
from typing import Optional, Union


class CryptoFormatter(logging.Formatter):
    """Custom log formatter for formatting cryptocurrency transaction events."""

    def format(self, record: logging.LogRecord) -> str:
        symbol = getattr(record, "symbol", "N/A")
        record.msg = f"[{symbol}] {record.msg}"
        return super().format(record)


def setup_logger(
    name: str = "fragrantauto",
    log_file: Optional[Union[str, Path]] = None,
    level: int = logging.INFO,
) -> logging.Logger:
    """Configures and returns a structured logger for crypto operations.

    Args:
        name: The name of the logger instance.
        log_file: Optional file path to store output logs.
        level: Logging severity level.

    Returns:
        Configured Logger instance ready for operational logging.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False

    if logger.handlers:
        return logger

    formatter = CryptoFormatter(
        fmt="%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if log_file:
        file_path = Path(log_file)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(file_path, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
