from typing import Final, Dict, List

EXCHANGE_TIMEOUT: Final[float] = 30.0
MAX_RETRIES: Final[int] = 3

SUPPORTED_ASSETS: Final[List[str]] = ["BTC", "ETH", "SOL", "USDT"]

RATE_LIMITS: Final[Dict[str, int]] = {
    "public": 10,
    "private": 5
}

ENDPOINT_BASE: Final[str] = "https://api.fragrantauto.io/v1"

DECIMAL_PRECISION: Final[int] = 8

class ChainID:
    MAINNET: Final[int] = 1
    TESTNET: Final[int] = 5

def get_chain_label(chain_id: int) -> str:
    """Return string representation for given chain identifier."""
    mapping: Dict[int, str] = {
        ChainID.MAINNET: "mainnet",
        ChainID.TESTNET: "testnet"
    }
    return mapping.get(chain_id, "unknown")