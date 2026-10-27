import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional


def setup_logger(
    name: str = "fragrantauto",
    log_dir: str = "logs",
    log_filename: str = "crypto_bot.log",
    level: int = logging.INFO,
    max_bytes: int = 5 * 1024 * 1024,
    backup_count: int = 5,
) -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(level)
    logger.propagate = False

    log_path = Path(log_dir)
    log_path.mkdir(parents=True, exist_ok=True)
    file_path = log_path / log_filename

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = RotatingFileHandler(
        file_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)
    logger.addHandler(console_handler)

    return logger
