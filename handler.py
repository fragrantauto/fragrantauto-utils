from typing import Dict, Any, List
from decimal import Decimal

class CryptoDataHandler:
    def __init__(self, precision: int = 8):
        self.precision = precision

    def format_balance(self, amount: str) -> Decimal:
        return Decimal(amount).quantize(Decimal(f'1.{"0" * self.precision}'))

    def normalize_ticker(self, symbol: str) -> str:
        return symbol.strip().upper().replace('/', '_')

    def sanitize_order_payload(self, data: Dict[str, Any]) -> Dict[str, Any]:
        required = {'symbol', 'side', 'quantity', 'price'}
        if not all(k in data for k in required):
            raise ValueError(f'missing keys: {required - data.keys()}')
        
        return {
            'symbol': self.normalize_ticker(data['symbol']),
            'side': data['side'].lower(),
            'quantity': float(self.format_balance(str(data['quantity']))),
            'price': float(self.format_balance(str(data['price'])))
        }

    def aggregate_market_data(self, inputs: List[Dict[str, Any]]) -> Dict[str, float]:
        results = {}
        for entry in inputs:
            symbol = self.normalize_ticker(entry['symbol'])
            results[symbol] = float(self.format_balance(str(entry['price'])))
        return results