from decimal import Decimal
from typing import Dict, List, Optional, Tuple, Any


class CryptoOrderProcessor:
    """Process and normalize cryptocurrency trade data across exchanges."""

    def __init__(self, base_currency: str = "USDT") -> None:
        self.base_currency: str = base_currency.upper()

    def calculate_fee(self, amount: Decimal, fee_rate: Decimal) -> Decimal:
        """Calculate trading fee for a given transaction amount."""
        return (amount * fee_rate).quantize(Decimal("0.00000001"))

    def normalize_order_book(
        self, raw_bids: List[List[Any]], raw_asks: List[List[Any]]
    ) -> Dict[str, List[Tuple[Decimal, Decimal]]]:
        """Parse and convert raw exchange order book entries to structured Decimals."""
        bids = [(Decimal(str(p)), Decimal(str(q))) for p, q in raw_bids]
        asks = [(Decimal(str(p)), Decimal(str(q))) for p, q in raw_asks]
        bids.sort(key=lambda x: x[0], reverse=True)
        asks.sort(key=lambda x: x[0])
        return {"bids": bids, "asks": asks}

    def compute_vwap(self, trades: List[Dict[str, Decimal]]) -> Optional[Decimal]:
        """Compute Volume Weighted Average Price from trade executions."""
        if not trades:
            return None

        total_volume = Decimal("0")
        total_value = Decimal("0")

        for trade in trades:
            price = trade.get("price", Decimal("0"))
            volume = trade.get("volume", Decimal("0"))
            total_value += price * volume
            total_volume += volume

        if total_volume == Decimal("0"):
            return None

        return (total_value / total_volume).quantize(Decimal("0.00000001"))
