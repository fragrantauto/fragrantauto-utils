from decimal import Decimal, ROUND_HALF_UP
from typing import Union

def format_amount(value: Union[str, float, Decimal], precision: int = 8) -> str:
    return str(Decimal(str(value)).quantize(Decimal(f'1.{"0" * precision}'), rounding=ROUND_HALF_UP))

def calculate_fee(amount: Decimal, rate: Decimal) -> Decimal:
    return (amount * rate).quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP)

def validate_pair(pair: str) -> bool:
    parts = pair.split('/')
    return len(parts) == 2 and all(len(p) >= 2 for p in parts)

def sanitize_order_id(order_id: str) -> str:
    return ''.join(c for c in order_id if c.isalnum())

def compute_price_impact(price: Decimal, target: Decimal) -> Decimal:
    return abs((target - price) / price) * 100