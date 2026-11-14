from decimal import Decimal, ROUND_HALF_UP
from typing import Union, List

def format_crypto_amount(amount: Union[str, float, Decimal], precision: int = 8) -> Decimal:
    return Decimal(str(amount)).quantize(Decimal(10) ** -precision, rounding=ROUND_HALF_UP)

def calculate_position_size(balance: Decimal, risk_pct: Decimal, entry: Decimal, stop: Decimal) -> Decimal:
    if entry <= stop:
        raise ValueError("Entry price must be greater than stop loss for long positions")
    risk_amount = balance * risk_pct
    price_diff = entry - stop
    return (risk_amount / price_diff).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)

def validate_ticker(ticker: str) -> bool:
    return bool(ticker and ticker.replace('/', '').isalnum())

def sanitize_order_book(data: List[dict]) -> List[dict]:
    return [item for item in data if item.get('price') > 0 and item.get('amount') > 0]

def calculate_slippage(expected: Decimal, actual: Decimal) -> Decimal:
    return abs((actual - expected) / expected) * 100