from typing import Union, Dict, Any
from decimal import Decimal, ROUND_DOWN


def format_amount(amount: Union[float, str, Decimal], precision: int = 8) -> Decimal:
    factor = Decimal(10) ** -precision
    return Decimal(str(amount)).quantize(factor, rounding=ROUND_DOWN)


def validate_order(order: Dict[str, Any], required_keys: list) -> bool:
    return all(key in order for key in required_keys)


def calculate_fee(amount: Decimal, fee_rate: Decimal) -> Decimal:
    return (amount * fee_rate).quantize(Decimal('0.00000001'))


def parse_symbol(symbol: str) -> tuple[str, str]:
    base, quote = symbol.split('/')
    return base.upper(), quote.upper()


def sanitize_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in payload.items() if v is not None}