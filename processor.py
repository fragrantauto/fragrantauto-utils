from decimal import Decimal, ROUND_HALF_DOWN
from typing import Union, List

def format_crypto_amount(amount: Union[str, float, Decimal], decimals: int = 8) -> Decimal:
    return Decimal(str(amount)).quantize(Decimal(10)**-decimals, rounding=ROUND_HALF_DOWN)

def calculate_position_size(balance: Decimal, risk_percent: float, entry_price: Decimal, stop_loss: Decimal) -> Decimal:
    risk_amount = balance * Decimal(str(risk_percent))
    risk_per_unit = abs(entry_price - stop_loss)
    if risk_per_unit == 0:
        return Decimal('0')
    return risk_amount / risk_per_unit

def sanitize_order_params(params: dict) -> dict:
    return {k: v for k, v in params.items() if v is not None}

def aggregate_order_books(bids: List[List[str]], asks: List[List[str]]) -> dict:
    return {
        'bids': sorted([[Decimal(p), Decimal(a)] for p, a in bids], reverse=True),
        'asks': sorted([[Decimal(p), Decimal(a)] for p, a in asks])
    }

def validate_ticker(ticker: str) -> bool:
    return bool(ticker and ticker.replace('/', '').isalnum())