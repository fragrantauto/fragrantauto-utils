from typing import List, Dict, Optional
import logging

class DataProcessor:
    def __init__(self, target_chain: str = 'ethereum'):
        self.chain = target_chain
        self.logger = logging.getLogger(__name__)

    def sanitize_payload(self, data: Dict) -> Dict:
        return {k: v for k, v in data.items() if v is not None}

    def process_transaction(self, tx: Dict) -> Optional[Dict]:
        try:
            if not tx.get('hash') or not tx.get('value'):
                return None
            return {
                'tx_hash': tx['hash'],
                'amount': float(tx['value']),
                'chain': self.chain
            }
        except (ValueError, KeyError) as e:
            self.logger.error(f'invalid transaction data: {e}')
            return None

    def batch_process(self, transactions: List[Dict]) -> List[Dict]:
        return [p for tx in transactions if (p := self.process_transaction(tx))]

def run_pipeline(data: List[Dict]) -> List[Dict]:
    processor = DataProcessor()
    return processor.batch_process(data)