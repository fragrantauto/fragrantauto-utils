import re
from typing import Any


def is_valid_evm_address(address: Any) -> bool:
    if not isinstance(address, str):
        return False
    return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))


def is_valid_amount(value: Any) -> bool:
    try:
        amount = float(value)
        return amount >= 0
    except (ValueError, TypeError):
        return False


def sanitize_symbol(symbol: str) -> str:
    return re.sub(r'[^A-Z0-9]', '', symbol.upper())


def validate_transaction_payload(data: dict) -> bool:
    required_fields = {'from', 'to', 'value'}
    if not isinstance(data, dict):
        return False
    
    if not required_fields.issubset(data.keys()):
        return False
    
    return (
        is_valid_evm_address(data['from']) and
        is_valid_evm_address(data['to']) and
        is_valid_amount(data['value'])
    )