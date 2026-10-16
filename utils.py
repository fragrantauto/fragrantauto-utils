import decimal
from typing import Union

def to_decimal(amount: Union[str, float, int]) -> decimal.Decimal:
    return decimal.Decimal(str(amount))

def format_crypto(amount: decimal.Decimal, precision: int = 8) -> str:
    return format(amount.normalize(), f'.{precision}f')

def calculate_fee(amount: decimal.Decimal, rate: float) -> decimal.Decimal:
    return (amount * decimal.Decimal(str(rate))).quantize(decimal.Decimal('0.00000001'))

def truncate_address(address: str, length: int = 6) -> str:
    if len(address) <= length * 2:
        return address
    return f"{address[:length]}...{address[-length:]}"

def is_valid_ticker(ticker: str) -> bool:
    return bool(ticker and ticker.isalnum() and 2 <= len(ticker) <= 8)