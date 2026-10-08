import re
from typing import Dict, List, Any

class ValidationError(Exception):
    pass

def validate_tx_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    address_pattern = re.compile(r"^0x[a-fA-F0-9]{40}$")
    tx_id = payload.get("tx_id")
    if not isinstance(tx_id, str) or not tx_id.strip():
        raise ValidationError("Invalid or missing transaction ID")

    to_address = payload.get("to_address")
    if not isinstance(to_address, str) or not address_pattern.match(to_address):
        raise ValidationError("Invalid Ethereum address")

    amount = payload.get("amount")
    try:
        amount_val = float(amount)
        if amount_val <= 0:
            raise ValueError
    except (TypeError, ValueError):
        raise ValidationError("Amount must be a positive number")

    return {
        "tx_id": tx_id.strip(),
        "to_address": to_address.lower(),
        "amount": amount_val,
    }

def process_transaction_queue(payloads: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    processed = []
    for payload in payloads:
        try:
            validated = validate_tx_payload(payload)
            processed.append(validated)
        except ValidationError:
            pass
    return processed