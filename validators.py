from typing import Any, Dict

class ValidationError(Exception):
    pass

def validate_trade_params(data: Dict[str, Any]) -> None:
    required_keys = {'symbol', 'amount', 'price'}
    if not all(key in data for key in required_keys):
        raise ValidationError(f"Missing required keys: {required_keys - data.keys()}")
    
    if data['amount'] <= 0 or data['price'] <= 0:
        raise ValidationError("Amount and price must be positive")

def validate_config(config: Dict[str, Any]) -> None:
    if not isinstance(config.get('api_key'), str) or len(config.get('api_key', '')) < 32:
        raise ValidationError("Invalid or missing API key")
    if not isinstance(config.get('leverage'), (int, float)) or not (1 <= config['leverage'] <= 100):
        raise ValidationError("Leverage must be between 1 and 100")