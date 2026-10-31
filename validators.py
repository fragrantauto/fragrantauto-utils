import re
from typing import Any, Dict, Optional

ETH_ADDR_RE = re.compile(r"^0x[a-fA-F0-9]{40}$")
TX_HASH_RE = re.compile(r"^0x[a-fA-F0-9]{64}$")
BASE58_RE = re.compile(r"^[1-9A-HJ-NP-Za-km-z]+$")


def is_ethereum_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    return bool(ETH_ADDR_RE.match(address))


def is_transaction_hash(tx_hash: str) -> bool:
    if not isinstance(tx_hash, str):
        return False
    return bool(TX_HASH_RE.match(tx_hash))


def is_base58_string(data: str) -> bool:
    if not isinstance(data, str) or not data:
        return False
    return bool(BASE58_RE.match(data))


def validate_order_payload(payload: Dict[str, Any]) -> bool:
    required_fields = {"symbol", "side", "amount", "price"}
    if not isinstance(payload, dict) or not required_fields.issubset(payload.keys()):
        return False

    if payload["side"] not in ("buy", "sell"):
        return False

    try:
        amount = float(payload["amount"])
        price = float(payload["price"])
        return amount > 0 and price > 0
    except (ValueError, TypeError):
        return False


def normalize_hex(hex_str: str, byte_length: Optional[int] = None) -> str:
    if not isinstance(hex_str, str):
        raise TypeError("Input must be a string")
    clean = hex_str.strip()
    if clean.startswith(("0x", "0X")):
        clean = clean[2:]
    if len(clean) % 2 != 0:
        clean = f"0{clean}"
    if byte_length and len(clean) != byte_length * 2:
        raise ValueError(f"Expected {byte_length} bytes, got {len(clean) // 2}")
    return f"0x{clean.lower()}"
