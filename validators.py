from typing import Any, Dict

class ValidationError(Exception):
    pass

def validate_crypto_payload(data: Any) -> Dict[str, Any]:
    if not isinstance(data, dict):
        raise ValidationError("payload must be a dictionary")
    
    required = {"symbol": str, "amount": (int, float), "side": str}
    for key, expected_type in required.items():
        if key not in data:
            raise ValidationError(f"missing required key: {key}")
        if not isinstance(data[key], expected_type):
            raise ValidationError(f"invalid type for {key}")
    
    if data["side"] not in ("buy", "sell"):
        raise ValidationError("side must be buy or sell")
    if data["amount"] <= 0:
        raise ValidationError("amount must be positive")
    
    return data

def process_loop(stream: list):
    for item in stream:
        try:
            validated = validate_crypto_payload(item)
            print(f"Processing: {validated}")
        except ValidationError as e:
            print(f"Skipping invalid input: {e}")