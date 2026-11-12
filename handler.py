import json
from decimal import Decimal
from typing import Dict, Any, Optional

def normalize_crypto_data(data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "symbol": str(data.get("s", "")).upper(),
        "price": Decimal(str(data.get("p", "0"))),
        "quantity": Decimal(str(data.get("q", "0"))),
        "timestamp": int(data.get("t", 0)),
    }

def validate_order_payload(payload: str) -> Optional[Dict[str, Any]]:
    try:
        parsed = json.loads(payload)
        required = {"s", "p", "q", "t"}
        if not all(k in parsed for k in required):
            return None
        return normalize_crypto_data(parsed)
    except (json.JSONDecodeError, ValueError, TypeError):
        return None

def calculate_position_value(price: Decimal, quantity: Decimal) -> Decimal:
    return price * quantity

def format_trade_log(data: Dict[str, Any]) -> str:
    return f"[{data['timestamp']}] {data['symbol']}: {data['quantity']} @ {data['price']}"