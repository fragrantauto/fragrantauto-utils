from typing import List, Dict, Any
from functools import lru_cache
import hashlib

class AddressValidator:
    def __init__(self, checksum_enabled: bool = True):
        self.checksum_enabled = checksum_enabled

    @lru_cache(maxsize=1024)
    def validate_address(self, address: str) -> bool:
        if not isinstance(address, str) or len(address) != 42:
            return False
        if not address.startswith('0x'):
            return False
        return all(c in '0123456789abcdefABCDEF' for c in address[2:])

    def batch_validate(self, addresses: List[str]) -> Dict[str, bool]:
        return {addr: self.validate_address(addr) for addr in addresses}

def validate_transaction_batch(tx_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [tx for tx in tx_list if tx.get('value', 0) > 0]

class HashCache:
    def __init__(self):
        self._cache = {}

    def get_hash(self, data: str) -> str:
        if data not in self._cache:
            self._cache[data] = hashlib.sha256(data.encode()).hexdigest()
        return self._cache[data]