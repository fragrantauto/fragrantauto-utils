import logging
from typing import Any, Optional

class CryptoOperationError(Exception):
    pass

def safe_execute(func: callable, *args: Any, **kwargs: Any) -> Optional[Any]:
    try:
        return func(*args, **kwargs)
    except (ConnectionError, TimeoutError) as e:
        logging.error(f"Network failure during execution: {e}")
        raise CryptoOperationError("Network connectivity issue") from e
    except ValueError as e:
        logging.error(f"Invalid input data: {e}")
        return None
    except Exception as e:
        logging.critical(f"Unexpected system failure: {e}")
        raise

def validate_transaction_payload(payload: dict) -> bool:
    required = {"amount", "address", "asset_id"}
    if not isinstance(payload, dict):
        return False
    return required.issubset(payload.keys()) and payload["amount"] > 0