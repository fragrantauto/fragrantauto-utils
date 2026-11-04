import functools
from typing import Any, Callable, Dict

_CACHE: Dict[tuple, bool] = {}

def lru_memoize(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any) -> bool:
        if args not in _CACHE:
            _CACHE[args] = func(*args)
        return _CACHE[args]
    return wrapper

@lru_memoize
def validate_checksum(address: str) -> bool:
    if not isinstance(address, str) or len(address) != 42:
        return False
    return address.startswith('0x') and address.isalnum()

def batch_validate(addresses: list[str]) -> list[bool]:
    return [validate_checksum(addr) for addr in addresses]

def clear_validator_cache() -> None:
    _CACHE.clear()