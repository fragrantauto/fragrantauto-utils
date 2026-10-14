from typing import Final

# Network identifiers
MAINNET_ID: Final[str] = "mainnet"
TESTNET_ID: Final[str] = "testnet"

# Exchange rate precision
PRICE_PRECISION: Final[int] = 8
QUANTITY_PRECISION: Final[int] = 6

# API limits
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Environment keys
API_KEY_ENV: Final[str] = "FA_API_KEY"
API_SECRET_ENV: Final[str] = "FA_API_SECRET"

# Decimal representations
ZERO_DECIMAL: Final[str] = "0.00000000"

# Fee configurations
MAKER_FEE: Final[float] = 0.001
TAKER_FEE: Final[float] = 0.002

# Supported order types
ORDER_TYPES: Final[set] = {"market", "limit", "stop_loss"}

# Supported trading pairs
VALID_PAIRS: Final[list] = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]

# Logging configuration
LOG_FORMAT: Final[str] = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"