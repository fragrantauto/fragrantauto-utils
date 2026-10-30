import hashlib
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from typing import List, Tuple


@lru_cache(maxsize=4096)
def fast_hash_payload(payload: bytes) -> str:
    return hashlib.blake2b(payload, digest_size=32).hexdigest()


class BatchCoreProcessor:
    def __init__(self, max_workers: int = 8) -> None:
        self.max_workers = max_workers

    def compute_hashes(self, payloads: List[bytes]) -> List[str]:
        if len(payloads) < 64:
            return [fast_hash_payload(p) for p in payloads]

        chunk_size = max(1, len(payloads) // (self.max_workers * 4))
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            return list(
                executor.map(fast_hash_payload, payloads, chunksize=chunk_size)
            )

    def verify_and_hash_batch(
        self, items: List[Tuple[str, bytes]]
    ) -> List[Tuple[str, str, bool]]:
        payloads = [item[1] for item in items]
        hashes = self.compute_hashes(payloads)
        return [
            (tx_id, h, len(h) == 64) for (tx_id, _), h in zip(items, hashes)
        ]
