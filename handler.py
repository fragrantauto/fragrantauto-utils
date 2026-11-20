import json
from typing import Dict, Any, Optional
from decimal import Decimal, InvalidOperation

class CryptoDataHandler:
    def __init__(self, precision: int = 8):
        self.precision = precision

    def format_price(self, value: Any) -> Decimal:
        try:
            return Decimal(str(value)).quantize(Decimal(f"1.{'0' * self.precision}"))
        except (InvalidOperation, ValueError):
            return Decimal('0.00000000')

    def normalize_payload(self, data: Dict[str, Any]) -> Dict[str, Any]:
        normalized = {}
        for key, val in data.items():
            if key in ['price', 'amount', 'volume']:
                normalized[key] = float(self.format_price(val))
            else:
                normalized[key] = val
        return normalized

    @staticmethod
    def validate_ticker(ticker: str) -> bool:
        if not isinstance(ticker, str) or len(ticker) < 2:
            return False
        return ticker.isupper() and ticker.isalnum()

    def serialize_batch(self, data: list[dict]) -> str:
        return json.dumps([self.normalize_payload(item) for item in data])