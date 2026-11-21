import hashlib
import hmac
import time
from typing import Dict, Any, Optional

def generate_signature(api_secret: str, message: str) -> str:
    return hmac.new(
        api_secret.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def format_order_payload(symbol: str, side: str, amount: float, price: float) -> Dict[str, Any]:
    return {
        "symbol": symbol.upper(),
        "side": side.lower(),
        "quantity": str(amount),
        "price": str(price),
        "timestamp": int(time.time() * 1000)
    }

def validate_crypto_pair(pair: str) -> bool:
    parts = pair.split('_')
    return len(parts) == 2 and all(len(p) >= 3 for p in parts)

def sanitize_price(price: float, precision: int = 8) -> float:
    return round(float(price), precision)