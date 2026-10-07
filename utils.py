from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, List, Optional

def format_price(amount: float, precision: int = 8) -> str:
    return format(Decimal(str(amount)).quantize(Decimal(f'1.{("0" * precision)}'), rounding=ROUND_HALF_UP), 'f')

def calculate_order_value(price: float, quantity: float) -> Decimal:
    return Decimal(str(price)) * Decimal(str(quantity))

def sanitize_orderbook(data: Dict[str, List[List[str]]]) -> Dict[str, List[List[float]]]:
    return {
        side: [[float(p), float(q)] for p, q in orders]
        for side, orders in data.items()
    }

def validate_pair(pair: str) -> bool:
    if not isinstance(pair, str) or '_' not in pair:
        return False
    base, quote = pair.split('_')
    return base.isalnum() and quote.isalnum()