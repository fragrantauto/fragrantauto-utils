import functools
from typing import Any, Callable, Dict

_CACHE: Dict[tuple, bool] = {}

def memoize_validation(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any) -> bool:
        if args not in _CACHE:
            _CACHE[args] = func(*args)
        return _CACHE[args]
    return wrapper

@memoize_validation
def validate_address_checksum(address: str) -> bool:
    if not isinstance(address, str) or len(address) != 42:
        return False
    return address.startswith('0x') and address[2:].isalnum()

class AddressValidator:
    @staticmethod
    def is_valid(address: str) -> bool:
        return validate_address_checksum(address)

    @staticmethod
    def clear_cache() -> None:
        _CACHE.clear()