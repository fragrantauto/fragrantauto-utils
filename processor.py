import logging
from typing import Dict, Any, List

class DataProcessor:
    def __init__(self, logger: logging.Logger) -> None:
        self.logger = logger

    def sanitize_trade_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        required_fields = ['asset', 'price', 'quantity']
        return {k: v for k, v in data.items() if k in required_fields}

    def process_batch(self, batch: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        self.logger.info(f'Processing batch of {len(batch)} items')
        return [self.sanitize_trade_data(item) for item in batch if item]

    def validate_price(self, price: float) -> bool:
        return isinstance(price, (int, float)) and price > 0

def get_processor(name: str = 'fragrantauto') -> DataProcessor:
    logger = logging.getLogger(name)
    return DataProcessor(logger)