from typing import Final, Dict, List

RPC_ENDPOINTS: Final[List[str]] = [
    "https://api.mainnet.chain.com",
    "https://rpc.cluster.internal"
]

DEFAULT_TIMEOUT: Final[float] = 30.0
MAX_RETRIES: Final[int] = 3

CURRENCY_PRECISION: Final[Dict[str, int]] = {
    "BTC": 8,
    "ETH": 18,
    "USDT": 6
}

FEE_RESERVATION: Final[float] = 0.0002


def get_precision(symbol: str) -> int:
    """Return decimal precision for a given crypto asset."""
    return CURRENCY_PRECISION.get(symbol, 8)


def format_wei(amount: int, symbol: str) -> float:
    """Convert integer base units to float representation."""
    return amount / (10 ** get_precision(symbol))