import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "fragrantauto.log"

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    LOG_DIR.mkdir(exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    
    file_handler = RotatingFileHandler(
        LOG_FILE, 
        maxBytes=5 * 1024 * 1024, 
        backupCount=5
    )
    file_handler.setFormatter(formatter)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger