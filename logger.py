import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "fragrantauto.log"


def setup_logger(name: str = "fragrantauto") -> logging.Logger:
    LOG_DIR.mkdir(exist_ok=True)
    
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    
    handler = RotatingFileHandler(
        LOG_FILE, 
        maxBytes=5_000_000, 
        backupCount=5
    )
    handler.setFormatter(formatter)
    
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    logger.addHandler(console)
    
    return logger

logger = setup_logger()