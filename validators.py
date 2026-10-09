from typing import Any, Dict

class ValidationError(Exception):
    pass

def validate_order_payload(data: Any) -> Dict[str, Any]:
    if not isinstance(data, dict):
        raise ValidationError("payload must be a dictionary")
    
    required_fields = {"symbol": str, "side": str, "amount": (int, float), "price": (int, float)}
    
    for field, field_type in required_fields.items():
        if field not in data:
            raise ValidationError(f"missing required field: {field}")
        if not isinstance(data[field], field_type):
            raise ValidationError(f"invalid type for {field}")
            
    if data["side"] not in ("buy", "sell"):
        raise ValidationError("side must be buy or sell")
    if data["amount"] <= 0 or data["price"] <= 0:
        raise ValidationError("amount and price must be positive")
        
    return data

def validate_api_key(key: str) -> bool:
    if not isinstance(key, str) or len(key) != 32:
        return False
    return key.isalnum()
