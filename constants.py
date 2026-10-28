from typing import Final

# Network identifiers
MAINNET_ID: Final[str] = "mainnet"
TESTNET_ID: Final[str] = "testnet"

# API request settings
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Crypto asset configuration
BASE_ASSETS: Final[list[str]] = ["BTC", "ETH", "SOL"]
SUPPORTED_EXCHANGES: Final[tuple[str, ...]] = ("binance", "coinbase", "kraken")

# Decimal precision standards
PRICE_PRECISION: Final[int] = 8
AMOUNT_PRECISION: Final[int] = 6

# Rate limiting defaults
RATE_LIMIT_PER_MINUTE: Final[int] = 1200
BURST_LIMIT: Final[int] = 50