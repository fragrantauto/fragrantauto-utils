import functools
from typing import Callable, Any, Dict

class TransactionHandler:
    def __init__(self, cache_size: int = 1024):
        self._cache_size = cache_size
        self._buffer: Dict[str, Any] = {}

    @functools.lru_cache(maxsize=1024)
    def _compute_hash(self, tx_data: str) -> int:
        return hash(tx_data)

    def process_transaction(self, data: str) -> Dict[str, Any]:
        tx_id = self._compute_hash(data)
        if tx_id in self._buffer:
            return self._buffer[tx_id]
        
        result = {'id': tx_id, 'status': 'processed', 'payload': data}
        self._buffer[tx_id] = result
        
        if len(self._buffer) > self._cache_size:
            self._buffer.pop(next(iter(self._buffer)))
            
        return result

def batch_process(items: list, handler: TransactionHandler) -> list:
    return [handler.process_transaction(item) for item in items]

if __name__ == '__main__':
    h = TransactionHandler()
    print(batch_process(['tx1', 'tx2', 'tx1'], h))