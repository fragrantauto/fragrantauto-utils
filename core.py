from hashlib import blake2b
from functools import lru_cache
from typing import List, Tuple, Dict


@lru_cache(maxsize=8192)
def _hash_pair(left: bytes, right: bytes) -> bytes:
    return blake2b(left + right, digest_size=32).digest()


class FastMerkleTree:
    def __init__(self, leaf_hashes: List[bytes]) -> None:
        self._leaves = leaf_hashes

    def compute_root(self) -> bytes:
        if not self._leaves:
            return b"\x00" * 32
        nodes = self._leaves
        while len(nodes) > 1:
            if len(nodes) % 2 == 1:
                nodes = list(nodes)
                nodes.append(nodes[-1])
            nodes = [
                _hash_pair(nodes[i], nodes[i + 1])
                for i in range(0, len(nodes), 2)
            ]
        return nodes[0]


class FastOrderBookAggregator:
    def __init__(self, precision: int = 2) -> None:
        self.precision = precision
        self.factor = 10**precision

    def aggregate(self, orders: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
        aggregated: Dict[int, float] = {}
        for price, volume in orders:
            bucket = int(price * self.factor)
            aggregated[bucket] = aggregated.get(bucket, 0.0) + volume

        return [
            (round(bucket / self.factor, self.precision), round(vol, 8))
            for bucket, vol in sorted(aggregated.items())
        ]
