import re
from typing import Union

DEFAULT_DECIMALS = 18


def to_wei(amount: Union[int, float], decimals: int = DEFAULT_DECIMALS) -> int:
    return int(amount * (10 ** decimals))


def from_wei(amount: int, decimals: int = DEFAULT_DECIMALS) -> float:
    return amount / (10 ** decimals)


def truncate_address(address: str, prefix_len: int = 6, suffix_len: int = 4) -> str:
    if not address or len(address) <= prefix_len + suffix_len:
        return address
    return f"{address[:prefix_len]}...{address[-suffix_len:]}"


def calculate_slippage_price(
    price: float, slippage_percent: float, is_buy: bool = True
) -> float:
    adjustment = (slippage_percent / 100.0)
    factor = 1.0 + adjustment if is_buy else 1.0 - adjustment
    return round(price * factor, 8)


def is_valid_hex(hex_str: str) -> bool:
    clean_hex = hex_str[2:] if hex_str.startswith("0x") else hex_str
    if not clean_hex:
        return False
    return bool(re.fullmatch(r"[0-9a-fA-F]+", clean_hex)) and len(clean_hex) % 2 == 0
