from typing import Any, Optional
import re


class CryptoValidator:
    @staticmethod
    def is_valid_address(address: str, chain_type: str = 'evm') -> bool:
        if chain_type == 'evm':
            return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))
        if chain_type == 'solana':
            return bool(re.match(r'^[1-9A-HJ-NP-Za-km-z]{32,44}$', address))
        return False

    @staticmethod
    def sanitize_amount(amount: Any) -> float:
        try:
            value = float(amount)
            return value if value >= 0 else 0.0
        except (ValueError, TypeError):
            return 0.0

    @staticmethod
    def validate_asset_pair(pair: str) -> bool:
        pattern = r'^[A-Z0-9]{2,10}/[A-Z0-9]{2,10}$'
        return bool(re.match(pattern, pair))


def validate_transaction_payload(data: dict) -> Optional[dict]:
    required_fields = {'address', 'amount', 'symbol'}
    if not all(field in data for field in required_fields):
        return None
    
    if not CryptoValidator.is_valid_address(data['address']):
        return None
        
    data['amount'] = CryptoValidator.sanitize_amount(data['amount'])
    if data['amount'] <= 0:
        return None
        
    return data