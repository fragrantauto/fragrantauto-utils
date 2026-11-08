import logging
import sys
from functools import lru_cache

@lru_cache(maxsize=8)
def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger

class PerformanceLogger:
    def __init__(self, name: str):
        self.logger = get_logger(name)

    def log_execution_time(self, func):
        import time
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = time.perf_counter() - start
            self.logger.info(f'{func.__name__} took {duration:.6f}s')
            return result
        return wrapper