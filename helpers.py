from decimal import Decimal, InvalidOperation
import re


class CryptoValueError(ValueError):
    pass


class InvalidAddressError(CryptoValueError):
    pass


class InvalidAmountError(CryptoValueError):
    pass


def validate_checksum_address(address: str) -> str:
    if not isinstance(address, str):
        raise InvalidAddressError("Address must be a string")
    address = address.strip()
    if not re.match(r"^0x[a-fA-F0-9]{40}$", address):
        raise InvalidAddressError(f"Invalid address format: {address}")
    return address


def to_wei(amount: float | str | Decimal, decimals: int = 18) -> int:
    if not isinstance(decimals, int) or decimals < 0 or decimals > 36:
        raise ValueError("Decimals must be an integer between 0 and 36")
    try:
        dec_amount = Decimal(str(amount))
    except (InvalidOperation, TypeError):
        raise InvalidAmountError(f"Cannot parse amount: {amount}")

    if dec_amount < 0:
        raise InvalidAmountError("Amount cannot be negative")

    wei_val = dec_amount * (Decimal(10) ** decimals)
    if wei_val != wei_val.to_integral_value():
        raise InvalidAmountError("Amount precision exceeds specified decimals")

    return int(wei_val)


def from_wei(wei_amount: int, decimals: int = 18) -> Decimal:
    if not isinstance(wei_amount, int):
        raise InvalidAmountError("Wei amount must be an integer")
    if wei_amount < 0:
        raise InvalidAmountError("Wei amount cannot be negative")
    if not isinstance(decimals, int) or decimals < 0 or decimals > 36:
        raise ValueError("Decimals must be an integer between 0 and 36")

    factor = Decimal(10) ** decimals
    return Decimal(wei_amount) / factor