import re
from typing import Any

EVM_ADDRESS_REGEX = re.compile(r"^0x[a-fA-F0-9]{40}$")
HEX_32_BYTE_REGEX = re.compile(r"^0x[a-fA-F0-9]{64}$")
BASE58_REGEX = re.compile(r"^[1-9A-HJ-NP-Za-km-z]{32,44}$")


def is_valid_evm_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    return bool(EVM_ADDRESS_REGEX.match(address))


def is_valid_tx_hash(tx_hash: str) -> bool:
    if not isinstance(tx_hash, str):
        return False
    return bool(HEX_32_BYTE_REGEX.match(tx_hash))


def is_valid_solana_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    return bool(BASE58_REGEX.match(address))


def is_positive_amount(amount: Any) -> bool:
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False


def validate_gas_limit(gas_limit: int, min_gas: int = 21000, max_gas: int = 15000000) -> bool:
    if not isinstance(gas_limit, int):
        return False
    return min_gas <= gas_limit <= max_gas
