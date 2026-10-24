import re
from typing import Any, Optional

def validate_address(address: str, chain_type: str = 'evm') -> bool:
    if not isinstance(address, str):
        return False
    if chain_type == 'evm':
        return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))
    if chain_type == 'solana':
        return bool(re.match(r'^[1-9A-HJ-NP-Za-km-z]{32,44}$', address))
    return False

def validate_amount(amount: Any) -> bool:
    try:
        value = float(amount)
        return value > 0
    except (ValueError, TypeError):
        return False

def sanitize_symbol(symbol: str) -> Optional[str]:
    if not isinstance(symbol, str):
        return None
    clean = re.sub(r'[^A-Z0-9]', '', symbol.upper())
    return clean if 1 <= len(clean) <= 10 else None