import re
from typing import Any

ADDRESS_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')

def is_eth_address(address: Any) -> bool:
    if not isinstance(address, str):
        return False
    return bool(ADDRESS_PATTERN.match(address))

def validate_amount(amount: Any) -> float:
    try:
        value = float(amount)
        if value <= 0:
            raise ValueError('Amount must be positive')
        return value
    except (TypeError, ValueError):
        raise ValueError(f'Invalid amount: {amount}')

def is_valid_chain_id(chain_id: Any) -> bool:
    try:
        return isinstance(chain_id, int) and chain_id > 0
    except Exception:
        return False

def validate_gas_price(gas_price: Any) -> int:
    try:
        value = int(gas_price)
        if value < 0:
            raise ValueError('Gas price cannot be negative')
        return value
    except (TypeError, ValueError):
        raise ValueError(f'Invalid gas price: {gas_price}')