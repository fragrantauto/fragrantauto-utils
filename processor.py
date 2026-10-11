import logging
from typing import Any, Dict
from decimal import Decimal, InvalidOperation

logger = logging.getLogger(__name__)

def validate_trade_data(data: Dict[str, Any]) -> bool:
    required_keys = {'symbol', 'amount', 'price'}
    if not all(key in data for key in required_keys):
        return False
    try:
        amount = Decimal(str(data['amount']))
        price = Decimal(str(data['price']))
        return amount > 0 and price > 0
    except (InvalidOperation, ValueError, TypeError):
        return False

def process_trade_stream(stream: Any) -> None:
    for trade in stream:
        if not validate_trade_data(trade):
            logger.warning(f"invalid trade packet discarded: {trade}")
            continue
        
        try:
            execute_trade(trade)
        except Exception as e:
            logger.error(f"execution failure: {e}")

def execute_trade(trade: Dict[str, Any]) -> None:
    # internal execution logic
    pass