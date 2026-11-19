from typing import Any, Dict

class ValidationError(Exception):
    pass

def validate_transaction(data: Dict[str, Any]) -> None:
    required = {'tx_hash', 'amount', 'currency'}
    if not all(k in data for k in required):
        raise ValidationError('missing required transaction fields')
    
    if not isinstance(data['amount'], (int, float)) or data['amount'] <= 0:
        raise ValidationError('invalid transaction amount')
    
    if not isinstance(data['tx_hash'], str) or len(data['tx_hash']) < 32:
        raise ValidationError('invalid transaction hash format')

def validate_config(config: Dict[str, Any]) -> None:
    if 'api_key' not in config or not config['api_key']:
        raise ValidationError('missing or empty api key')
    
    if 'node_url' not in config or not config['node_url'].startswith('http'):
        raise ValidationError('invalid node url configuration')

def validate_payload(payload: Any) -> None:
    if not isinstance(payload, dict):
        raise ValidationError('payload must be a dictionary')
    if not payload:
        raise ValidationError('payload cannot be empty')
