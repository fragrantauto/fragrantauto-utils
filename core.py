import re
from decimal import Decimal, InvalidOperation
from typing import Any, Dict, List

ETH_ADDRESS_REGEX = re.compile(r"^0x[a-fA-F0-9]{40}$")
SUPPORTED_SYMBOLS = {"BTC", "ETH", "USDT", "SOL"}


class TransactionValidationError(Exception):
    pass


def validate_payload(raw_tx: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(raw_tx, dict):
        raise TransactionValidationError("Payload must be a dictionary")

    address = raw_tx.get("recipient")
    if not isinstance(address, str) or not ETH_ADDRESS_REGEX.match(address):
        raise TransactionValidationError(f"Invalid address format: {address}")

    symbol = raw_tx.get("symbol")
    if symbol not in SUPPORTED_SYMBOLS:
        raise TransactionValidationError(f"Unsupported token symbol: {symbol}")

    try:
        amount = Decimal(str(raw_tx.get("amount", 0)))
        if amount <= Decimal("0"):
            raise TransactionValidationError("Amount must be strictly positive")
    except (InvalidOperation, TypeError):
        raise TransactionValidationError("Malformed numeric amount field")

    return {
        "recipient": address,
        "symbol": symbol,
        "amount": amount,
        "nonce": int(raw_tx.get("nonce", 0)),
    }


def run_processing_loop(queue: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    results = []
    for item in queue:
        try:
            tx = validate_payload(item)
            tx["status"] = "QUEUED"
            results.append(tx)
        except TransactionValidationError:
            continue
    return results
