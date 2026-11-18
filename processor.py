from typing import Dict, List, Optional, Union
from decimal import Decimal

class CryptoProcessor:
    """Handles cryptographic transaction processing and fee calculation."""

    def __init__(self, fee_rate: float = 0.003) -> None:
        self.fee_rate = Decimal(str(fee_rate))

    def calculate_net_amount(self, gross: Union[int, float, str]) -> Decimal:
        """Calculates net amount after applying processor fee."""
        value = Decimal(str(gross))
        return value * (Decimal('1.0') - self.fee_rate)

    def aggregate_transactions(self, tx_list: List[Dict[str, Union[str, float]]]) -> Dict[str, Decimal]:
        """Aggregates total volume per currency asset."""
        totals: Dict[str, Decimal] = {}
        for tx in tx_list:
            asset = str(tx.get("asset", "unknown"))
            amount = Decimal(str(tx.get("amount", 0)))
            totals[asset] = totals.get(asset, Decimal('0')) + amount
        return totals

    def validate_threshold(self, amount: Decimal, limit: Optional[Decimal] = None) -> bool:
        """Checks if amount exceeds defined safety threshold."""
        if limit is None:
            limit = Decimal('10000.0')
        return amount <= limit