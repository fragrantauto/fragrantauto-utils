import decimal
from typing import Union


def to_decimal(value: Union[int, float, str]) -> decimal.Decimal:
    return decimal.Decimal(str(value))


def format_currency(value: decimal.Decimal, precision: int = 8) -> str:
    return f"{value:.{precision}f}"


def calculate_fee(amount: decimal.Decimal, rate: decimal.Decimal) -> decimal.Decimal:
    return (amount * rate).quantize(decimal.Decimal('0.00000001'), rounding=decimal.ROUND_HALF_UP)


def validate_address(address: str, prefix: str = '0x') -> bool:
    return address.startswith(prefix) and len(address) == 42


def get_dust_threshold(symbol: str) -> decimal.Decimal:
    thresholds = {
        'BTC': decimal.Decimal('0.000005'),
        'ETH': decimal.Decimal('0.0001'),
        'USDT': decimal.Decimal('1.0')
    }
    return thresholds.get(symbol.upper(), decimal.Decimal('0.00001'))