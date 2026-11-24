import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

class CryptoHelper:
    @staticmethod
    def format_amount(amount: float, decimals: int = 8) -> str:
        return f"{amount:.{decimals}f}"

    @staticmethod
    def validate_address(address: str, chain: str) -> bool:
        if not address:
            return False
        if chain == "eth":
            return address.startswith("0x") and len(address) == 42
        if chain == "btc":
            return len(address) >= 26
        return True

    @classmethod
    def safe_dict_get(cls, data: Dict[str, Any], key: str, default: Any = None) -> Any:
        return data.get(key, default)

def sanitize_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in payload.items() if v is not None}

def retry_operation(func, retries: int = 3):
    def wrapper(*args, **kwargs):
        last_ex = None
        for _ in range(retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                last_ex = e
        raise last_ex
    return wrapper