import logging
from logging.handlers import RotatingFileHandler
import os

def get_logger(name: str, log_file: str = "fragrantauto.log") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        
        file_handler = RotatingFileHandler(
            log_file, 
            maxBytes=10 * 1024 * 1024, 
            backupCount=5
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    
    return logger