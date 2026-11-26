import functools
from typing import Callable, Any, Dict
import time

class CacheManager:
    def __init__(self, ttl: int = 60):
        self.ttl = ttl
        self.cache: Dict[str, tuple[float, Any]] = {}

    def memoize(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            key = f"{func.__name__}:{args}:{frozenset(kwargs.items())}"
            now = time.time()
            if key in self.cache:
                timestamp, result = self.cache[key]
                if now - timestamp < self.ttl:
                    return result
            result = func(*args, **kwargs)
            self.cache[key] = (now, result)
            return result
        return wrapper

cache_instance = CacheManager()

@cache_instance.memoize
def get_market_price(symbol: str) -> float:
    # Simulate expensive network latency for crypto pricing
    time.sleep(0.1)
    return 50000.0

def batch_process(data: list) -> list:
    return [get_market_price(item) for item in data]
