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

def normalize_amount(amount: float, precision: int = 8) -> str:
    return f"{Decimal(str(amount)):.{precision}f}"

def get_timestamp() -> int:
    return int(time.time() * 1000)

def format_order_params(params: Dict[str, Any]) -> str:
    keys = sorted(params.keys())
    return '&'.join([f"{k}={params[k]}" for k in keys])

def validate_ticker(ticker: str) -> bool:
    if not isinstance(ticker, str) or len(ticker) < 2:
        return False
    return ticker.isalnum()