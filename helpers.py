import re
from typing import Any, Dict, List


class ValidationError(Exception):
    pass


def validate_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))


def validate_trade_payload(payload: Dict[str, Any]) -> None:
    required_keys = {"address", "symbol", "amount", "side"}
    if not required_keys.issubset(payload.keys()):
        missing = required_keys - payload.keys()
        raise ValidationError(f"Missing required fields: {', '.join(missing)}")

    if not validate_address(payload["address"]):
        raise ValidationError(f"Invalid Ethereum address: {payload['address']}")

    if not isinstance(payload["amount"], (int, float)) or payload["amount"] <= 0:
        raise ValidationError(f"Amount must be a positive number: {payload['amount']}")

    if payload["side"] not in {"BUY", "SELL"}:
        raise ValidationError(f"Invalid trade side: {payload['side']}")


def process_trade_batch(payloads: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    processed = []
    for index, payload in enumerate(payloads):
        try:
            validate_trade_payload(payload)
            processed.append({
                "index": index,
                "status": "valid",
                "payload": payload
            })
        except ValidationError as err:
            processed.append({
                "index": index,
                "status": "invalid",
                "error": str(err)
            })
    return processed