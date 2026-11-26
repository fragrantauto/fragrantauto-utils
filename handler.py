import json
from decimal import Decimal
from typing import Dict, Any, List, Optional

class CryptoDataHandler:
    @staticmethod
    def normalize_price(value: Any) -> Decimal:
        try:
            return Decimal(str(value)).quantize(Decimal('0.00000001'))
        except (ValueError, TypeError, AttributeError):
            return Decimal('0.00000000')

    @staticmethod
    def validate_payload(data: Dict[str, Any], required: List[str]) -> bool:
        return all(key in data for key in required)

    @classmethod
    def process_ticker_batch(cls, raw_data: str) -> List[Dict[str, Any]]:
        try:
            data = json.loads(raw_data)
            if not isinstance(data, list):
                return []
            
            results = []
            for item in data:
                if cls.validate_payload(item, ['symbol', 'price']):
                    results.append({
                        'symbol': str(item['symbol']).upper(),
                        'price': cls.normalize_price(item['price'])
                    })
            return results
        except json.JSONDecodeError:
            return []

    @staticmethod
    def format_balance(balance: Dict[str, Any]) -> str:
        asset = balance.get('asset', 'UNKNOWN')
        amount = CryptoDataHandler.normalize_price(balance.get('free', 0))
        return f"{asset}: {amount:.8f}"