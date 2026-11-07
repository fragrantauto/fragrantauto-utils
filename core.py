import functools
from typing import Callable, Any, Dict

class ExecutionEngine:
    def __init__(self):
        self._cache: Dict[tuple, Any] = {}

    @staticmethod
    def memoize_state(func: Callable) -> Callable:
        cache = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key not in cache:
                cache[key] = func(*args, **kwargs)
            return cache[key]
        return wrapper

    @staticmethod
    def batch_process(data: list, size: int = 100):
        for i in range(0, len(data), size):
            yield data[i:i + size]

    def compute_hash_sequence(self, transactions: list) -> list:
        return [hash(tx) for tx in transactions]

def optimize_compute(func):
    @functools.lru_cache(maxsize=128)
    def cached_func(*args, **kwargs):
        return func(*args, **kwargs)
    return cached_func