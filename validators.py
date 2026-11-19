from typing import Any, Dict

class ValidationError(Exception):
    pass

def validate_crypto_payload(data: Any) -> Dict[str, Any]:
    if not isinstance(data, dict):
        raise ValidationError("payload must be a dictionary")
    
    required_keys = {"symbol", "amount", "price"}
    if not required_keys.issubset(data.keys()):
        raise ValidationError(f"missing keys: {required_keys - data.keys()}")
    
    if not isinstance(data["amount"], (int, float)) or data["amount"] <= 0:
        raise ValidationError("amount must be a positive number")
        
    if not isinstance(data["price"], (int, float)) or data["price"] <= 0:
        raise ValidationError("price must be a positive number")

    return data

def process_loop(data_stream: Any) -> None:
    for entry in data_stream:
        try:
            validated = validate_crypto_payload(entry)
            # logic processing here
            print(f"processing {validated['symbol']}")
        except ValidationError as e:
            print(f"validation failure: {e}")