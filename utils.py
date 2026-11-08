import hashlib
import hmac
import time
from typing import Dict, Any
from urllib.parse import urlencode

def generate_signature(api_secret: str, query_string: str) -> str:
    return hmac.new(
        api_secret.encode('utf-8'),
        query_string.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def format_params(params: Dict[str, Any]) -> str:
    params['timestamp'] = int(time.time() * 1000)
    return urlencode(sorted(params.items()))

def validate_order_params(params: Dict[str, Any]) -> bool:
    required = {'symbol', 'side', 'type', 'quantity'}
    return all(key in params for key in required)

def sanitize_float(value: Any, precision: int = 8) -> float:
    return round(float(value), precision)

def get_headers(api_key: str) -> Dict[str, str]:
    return {
        'X-MBX-APIKEY': api_key,
        'Content-Type': 'application/json'
    }