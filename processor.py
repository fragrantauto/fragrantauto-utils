import logging
from typing import Dict, Any
from .validators import validate_transaction

logger = logging.getLogger(__name__)

def process_transactions(data: list) -> None:
    if not isinstance(data, list):
        logger.error("Invalid input format: expected list")
        return

    for tx in data:
        try:
            if not validate_transaction(tx):
                logger.warning(f"Validation failed for tx: {tx.get('id')}")
                continue
            
            execute_trade(tx)
        except Exception as e:
            logger.error(f"Unexpected error during processing: {e}")

def execute_trade(tx: Dict[str, Any]) -> None:
    symbol = tx.get("symbol")
    amount = tx.get("amount")
    logger.info(f"Executing {amount} of {symbol}")