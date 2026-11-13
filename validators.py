import re
from typing import Any

class ValidationError(Exception):
    pass

def validate_crypto_address(address: str) -> bool:
    if not isinstance(address, str) or not (26 <= len(address) <= 35):
        return False
    return bool(re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address))

def validate_transaction_amount(amount: Any) -> float:
    try:
        val = float(amount)
        if val <= 0:
            raise ValidationError('Amount must be positive')
        return val
    except (TypeError, ValueError) as e:
        raise ValidationError(f'Invalid amount format: {e}')

def validate_input(data: dict) -> None:
    required = ['address', 'amount', 'symbol']
    for field in required:
        if field not in data:
            raise ValidationError(f'Missing field: {field}')
    
    if not validate_crypto_address(data['address']):
        raise ValidationError('Invalid wallet address format')
    
    data['amount'] = validate_transaction_amount(data['amount'])

def process_main_loop(queue: list) -> None:
    for entry in queue:
        try:
            validate_input(entry)
            # execution logic here
        except ValidationError as e:
            print(f'Skipping invalid entry: {e}')