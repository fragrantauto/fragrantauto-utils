from typing import Dict, Any, Optional

class ValidationError(Exception):
    pass

def validate_crypto_payload(data: Dict[str, Any]) -> bool:
    required_keys = {'symbol', 'amount', 'side'}
    if not all(key in data for key in required_keys):
        raise ValidationError('missing required keys in payload')
    
    if not isinstance(data['amount'], (int, float)) or data['amount'] <= 0:
        raise ValidationError('invalid amount value')
        
    if data['side'] not in {'buy', 'sell'}:
        raise ValidationError('invalid trade side')
        
    return True

def sanitize_input(data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        'symbol': str(data['symbol']).upper(),
        'amount': float(data['amount']),
        'side': str(data['side']).lower()
    }