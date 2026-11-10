import hashlib
from functools import lru_cache
from typing import List, Sequence


class CryptoBatchProcessor:
    __slots__ = ("_algorithm",)

    def __init__(self, algorithm: str = "sha256") -> None:
        self._algorithm = algorithm

    @lru_cache(maxsize=1024)
    def hash_payload(self, data: bytes) -> bytes:
        hasher = hashlib.new(self._algorithm)
        hasher.update(data)
        return hasher.digest()

    def compute_merkle_root(self, leaf_hashes: Sequence[bytes]) -> bytes:
        if not leaf_hashes:
            return b""

        current_level = list(leaf_hashes)
        while len(current_level) > 1:
            if len(current_level) % 2 != 0:
                current_level.append(current_level[-1])

            next_level = []
            for i in range(0, len(current_level), 2):
                combined = current_level[i] + current_level[i + 1]
                next_level.append(self.hash_payload(combined))
            current_level = next_level

        return current_level[0]

    def fast_batch_digest(self, payload_list: List[bytes]) -> List[bytes]:
        cache_get = self.hash_payload
        return [cache_get(item) for item in payload_list]
