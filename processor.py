from decimal import Decimal, ROUND_HALF_UP
from typing import Union, List

def format_amount(amount: Union[str, float, Decimal], precision: int = 8) -> Decimal:
    return Decimal(str(amount)).quantize(Decimal('1e-{}'.format(precision)), rounding=ROUND_HALF_UP)

def calculate_fee(amount: Union[str, float, Decimal], rate: float) -> Decimal:
    val = Decimal(str(amount)) * Decimal(str(rate))
    return val.quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP)

def validate_order_size(amount: float, min_size: float) -> bool:
    return amount >= min_size

def calculate_position_size(balance: float, risk_per_trade: float, stop_loss_pct: float) -> Decimal:
    risk_amount = Decimal(str(balance)) * Decimal(str(risk_per_trade))
    position_size = risk_amount / Decimal(str(stop_loss_pct))
    return position_size.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)

def sanitize_symbol(symbol: str) -> str:
    return symbol.strip().upper().replace('/', '').replace('_', '')

def chunk_list(items: List, size: int) -> List[List]:
    return [items[i:i + size] for i in range(0, len(items), size)]