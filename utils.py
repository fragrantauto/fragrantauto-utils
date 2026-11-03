import hashlib
import hmac
import time
from typing import Dict, Any
from decimal import Decimal

def generate_signature(api_secret: str, payload: str) -> str:
    return hmac.new(
        api_secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def get_timestamp() -> int:
    return int(time.time() * 1000)

def format_amount(amount: float, precision: int = 8) -> Decimal:
    return Decimal(str(amount)).quantize(Decimal(f"1.{'0' * precision}"))

def sanitize_params(params: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in params.items() if v is not None}

def validate_pair(pair: str) -> bool:
    parts = pair.split('_')
    return len(parts) == 2 and all(len(p) >= 2 for p in parts)