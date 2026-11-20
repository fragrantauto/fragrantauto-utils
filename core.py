import functools
from typing import Callable, Any, Dict
import time

CACHE_EXPIRY = 60
_cache: Dict[str, tuple[float, Any]] = {}

def memoize_crypto_data(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = f"{func.__name__}:{args}:{kwargs}"
        now = time.time()
        if key in _cache:
            expiry, result = _cache[key]
            if now - expiry < CACHE_EXPIRY:
                return result
        
        result = func(*args, **kwargs)
        _cache[key] = (now, result)
        return result
    return wrapper

@memoize_crypto_data
def calculate_market_volatility(prices: list[float]) -> float:
    if not prices:
        return 0.0
    mean = sum(prices) / len(prices)
    variance = sum((p - mean) ** 2 for p in prices) / len(prices)
    return variance ** 0.5

def process_batch_updates(data: list[dict]) -> list[float]:
    return [calculate_market_volatility(d['prices']) for d in data]