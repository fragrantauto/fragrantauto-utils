from decimal import Decimal, InvalidOperation
import re

ETH_ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")


class CryptoValueError(ValueError):
    pass


def parse_wei_to_ether(wei_value: int | str) -> Decimal:
    try:
        val = Decimal(str(wei_value))
        if val < 0:
            raise CryptoValueError("wei amount cannot be negative")
        return val / Decimal("1000000000000000000")
    except (InvalidOperation, TypeError) as exc:
        raise CryptoValueError(f"invalid wei value: {wei_value}") from exc


def sanitize_hex_string(hex_str: str) -> str:
    if not isinstance(hex_str, str):
        raise TypeError("hex input must be a string")
    cleaned = hex_str.strip()
    if not cleaned:
        raise CryptoValueError("hex string cannot be empty")
    if cleaned.startswith(("0x", "0X")):
        cleaned = cleaned[2:]
    if len(cleaned) % 2 != 0:
        cleaned = f"0{cleaned}"
    try:
        int(cleaned, 16)
    except ValueError as exc:
        raise CryptoValueError(f"invalid hex payload: {hex_str}") from exc
    return f"0x{cleaned.lower()}"


def calculate_slippage(expected: Decimal, actual: Decimal) -> Decimal:
    if expected <= 0 or actual < 0:
        raise CryptoValueError("trade amounts must be positive")
    try:
        return ((expected - actual) / expected) * Decimal("100")
    except ZeroDivisionError as exc:
        raise CryptoValueError("expected amount cannot be zero") from exc
