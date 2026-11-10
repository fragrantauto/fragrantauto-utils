import hashlib
from decimal import Decimal, ROUND_DOWN
from typing import Union


def to_base_unit(amount: Union[int, float, str], decimals: int = 18) -> int:
    d_amount = Decimal(str(amount))
    multiplier = Decimal(10 ** decimals)
    return int(d_amount * multiplier)


def from_base_unit(amount: int, decimals: int = 18) -> Decimal:
    d_amount = Decimal(str(amount))
    divider = Decimal(10 ** decimals)
    return d_amount / divider


def calculate_slippage_bounds(
    price: Union[float, Decimal],
    slippage_percent: float
) -> tuple[Decimal, Decimal]:
    d_price = Decimal(str(price))
    d_slippage = Decimal(str(slippage_percent)) / Decimal("100")
    min_price = d_price * (Decimal("1") - d_slippage)
    max_price = d_price * (Decimal("1") + d_slippage)
    return min_price, max_price


def truncate_amount(amount: Decimal, max_decimals: int = 4) -> Decimal:
    fmt = "0." + "0" * max_decimals if max_decimals > 0 else "0"
    return amount.quantize(Decimal(fmt), rounding=ROUND_DOWN)


def generate_tx_hash(payload: bytes) -> str:
    return f"0x{hashlib.sha256(payload).hexdigest()}"
