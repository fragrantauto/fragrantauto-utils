from decimal import Decimal
from typing import Any, Dict, List


class TransactionProcessor:
    """Processor for validating and executing crypto transaction payloads."""

    def __init__(self, base_fee: Decimal = Decimal("0.001")) -> None:
        self.base_fee = base_fee
        self._processed_hashes: set[str] = set()

    def calculate_total_amount(
        self, amount: Decimal, fee_multiplier: float = 1.0
    ) -> Decimal:
        """Calculate total transaction amount including dynamic network fees."""
        fee = self.base_fee * Decimal(str(fee_multiplier))
        return amount + fee

    def validate_payload(self, payload: Dict[str, Any]) -> bool:
        """Validate transaction payload structure and double-spend hashes."""
        required_keys = {"tx_hash", "sender", "recipient", "amount"}
        if not required_keys.issubset(payload.keys()):
            return False

        tx_hash = payload["tx_hash"]
        if not isinstance(tx_hash, str) or tx_hash in self._processed_hashes:
            return False

        return True

    def process_batch(
        self, transactions: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Process a list of raw transaction payloads and return execution results."""
        results = []
        for tx in transactions:
            if not self.validate_payload(tx):
                continue

            amount = Decimal(str(tx["amount"]))
            total = self.calculate_total_amount(amount)
            self._processed_hashes.add(tx["tx_hash"])
            results.append(
                {
                    "tx_hash": tx["tx_hash"],
                    "total_amount": str(total),
                    "status": "confirmed",
                }
            )
        return results
