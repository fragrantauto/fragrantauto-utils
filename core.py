import functools
from typing import Callable, Any, Dict

class CacheManager:
    def __init__(self, ttl_seconds: int = 60):
        self.ttl = ttl_seconds
        self._cache: Dict[tuple, tuple] = {}

    def memoize_with_ttl(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            import time
            key = (func.__name__, args, frozenset(kwargs.items()))
            now = time.time()
            if key in self._cache:
                result, timestamp = self._cache[key]
                if now - timestamp < self.ttl:
                    return result
            result = func(*args, **kwargs)
            self._cache[key] = (result, now)
            return result
        return wrapper

    def clear(self) -> None:
        self._cache.clear()

class TradeProcessor:
    def __init__(self, cache: CacheManager):
        self.cache = cache

    @staticmethod
    def compute_order_book_spread(asks: list, bids: list) -> float:
        if not asks or not bids:
            return 0.0
        return float(min(asks) - max(bids))

    def get_market_delta(self, market_id: str, asks: list, bids: list) -> float:
        cached_func = self.cache.memoize_with_ttl(self.compute_order_book_spread)
        return cached_func(asks, bids)

cache_instance = CacheManager(ttl_seconds=30)
processor = TradeProcessor(cache_instance)