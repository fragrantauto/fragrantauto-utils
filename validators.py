import re
from typing import Union

ADDRESS_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')

def validate_eth_address(address: str) -> bool:
    """Validates Ethereum-style hex address format."""
    if not isinstance(address, str):
        return False
    return bool(ADDRESS_PATTERN.match(address))

def sanitize_amount(amount: Union[int, float, str]) -> float:
    """Converts crypto amount to validated float."""
    try:
        value = float(amount)
        if value < 0:
            raise ValueError("Amount cannot be negative")
        return value
    except (ValueError, TypeError):
        return 0.0

def validate_chain_id(chain_id: int) -> bool:
    """Verifies supported blockchain identifier range."""
    return isinstance(chain_id, int) and 0 < chain_id < 2**64

def format_wei_to_ether(wei: int) -> float:
    """Calculates decimal ether from wei unit."""
    if not isinstance(wei, int) or wei < 0:
        return 0.0
    return wei / 10**18