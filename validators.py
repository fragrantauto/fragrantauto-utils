import functools
from typing import Any, Callable, Dict

_CACHE: Dict[tuple, Any] = {}

class AddressValidator:
    @staticmethod
    @functools.lru_cache(maxsize=1024)
    def is_valid_address(address: str) -> bool:
        if not isinstance(address, str) or len(address) != 42:
            return False
        return address.startswith('0x') and all(c in '0123456789abcdefABCDEF' for c in address[2:])

    @staticmethod
    def validate_batch(addresses: list[str]) -> list[bool]:
        return [AddressValidator.is_valid_address(addr) for addr in addresses]

def memoize_validator(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

@memoize_validator
def check_checksum(address: str) -> bool:
    address = address.lower().replace('0x', '')
    return len(address) == 40