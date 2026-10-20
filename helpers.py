import time
import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

def format_crypto_amount(amount: float, precision: int = 8) -> str:
    return f"{amount:.{precision}f}".rstrip('0').rstrip('.')

def retry_on_failure(retries: int = 3, delay: float = 1.0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_ex = None
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_ex = e
                    time.sleep(delay * (2 ** i))
            raise last_ex
        return wrapper
    return decorator

def validate_payload(data: Dict[str, Any], required_keys: list) -> bool:
    return all(key in data for key in required_keys)

def sanitize_symbol(symbol: str) -> str:
    return symbol.upper().replace('/', '_').strip()