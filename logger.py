import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_FILE = Path("logs/fragrantauto.log")
LOG_MAX_BYTES = 5 * 1024 * 1024
LOG_BACKUPS = 3

def setup_logger(name: str) -> logging.Logger:
    LOG_FILE.parent.mkdir(exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    
    handler = RotatingFileHandler(
        LOG_FILE, 
        maxBytes=LOG_MAX_BYTES, 
        backupCount=LOG_BACKUPS
    )
    handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(handler)
        logger.addHandler(logging.StreamHandler())
        
    return logger