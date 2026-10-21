import re
from typing import Any, Dict, List


class ValidationError(Exception):
    pass


def validate_transaction(tx: Dict[str, Any]) -> None:
    if not isinstance(tx, dict):
        raise ValidationError("Transaction payload must be a dictionary")

    required_keys = {"tx_hash", "sender", "receiver", "amount"}
    if not required_keys.issubset(tx.keys()):
        missing = required_keys - tx.keys()
        raise ValidationError(f"Missing required fields: {', '.join(missing)}")

    if not isinstance(tx["amount"], (int, float)) or tx["amount"] <= 0:
        raise ValidationError("Amount must be a positive number")

    address_pattern = re.compile(r"^0x[a-fA-F0-9]{40}$")
    if not address_pattern.match(str(tx["sender"])):
        raise ValidationError("Invalid sender address format")
    if not address_pattern.match(str(tx["receiver"])):
        raise ValidationError("Invalid receiver address format")

    hash_pattern = re.compile(r"^0x[a-fA-F0-9]{64}$")
    if not hash_pattern.match(str(tx["tx_hash"])):
        raise ValidationError("Invalid transaction hash format")


def process_queue(queue: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    processed = []
    for item in queue:
        try:
            validate_transaction(item)
            item["status"] = "validated"
            processed.append(item)
        except ValidationError as err:
            tx_hash = item.get("tx_hash") if isinstance(item, dict) else None
            processed.append(
                {
                    "tx_hash": tx_hash,
                    "status": "failed",
                    "error": str(err),
                }
            )
    return processed
