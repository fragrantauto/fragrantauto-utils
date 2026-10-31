import re
from typing import Any, Dict, Optional


class ValidationError(Exception):
    """Raised when input validation fails in processing pipeline."""
    pass


def validate_eth_address(address: str) -> str:
    if not isinstance(address, str) or not re.match(r"^0x[a-fA-F0-9]{40}$", address):
        raise ValidationError(f"Invalid Ethereum address: {address}")
    return address.lower()


def validate_tx_hash(tx_hash: str) -> str:
    if not isinstance(tx_hash, str) or not re.match(r"^0x[a-fA-F0-9]{64}$", tx_hash):
        raise ValidationError(f"Invalid transaction hash: {tx_hash}")
    return tx_hash.lower()


def validate_amount(amount: Any, min_val: float = 0.0, max_val: Optional[float] = None) -> float:
    try:
        val = float(amount)
    except (ValueError, TypeError):
        raise ValidationError(f"Amount must be numeric, got {type(amount).__name__}")
    
    if val <= min_val:
        raise ValidationError(f"Amount must be greater than {min_val}, got {val}")
    if max_val is not None and val > max_val:
        raise ValidationError(f"Amount exceeds maximum threshold {max_val}, got {val}")
    return val


def validate_transaction_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(payload, dict):
        raise ValidationError("Payload must be a dictionary")
    
    required_fields = {"target_address", "amount", "tx_hash"}
    missing_fields = required_fields - set(payload.keys())
    if missing_fields:
        raise ValidationError(f"Missing payload fields: {sorted(missing_fields)}")
    
    return {
        "target_address": validate_eth_address(payload["target_address"]),
        "amount": validate_amount(payload["amount"]),
        "tx_hash": validate_tx_hash(payload["tx_hash"]),
    }
