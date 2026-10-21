from typing import Final

# Network constants
MAINNET_CHAIN_ID: Final[int] = 1
SEPOLIA_CHAIN_ID: Final[int] = 11155111

# Default decimals for ERC20 tokens
DEFAULT_DECIMALS: Final[int] = 18

# Gas estimation multipliers
GAS_BUFFER_MULTIPLIER: Final[float] = 1.2
MIN_GAS_LIMIT: Final[int] = 21000

# Common time constants
BLOCK_TIME_SECONDS: Final[int] = 12
RETRY_DELAY_SECONDS: Final[float] = 2.5

# HTTP configurations
REQUEST_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Precision settings
PRECISION_SCALE: Final[int] = 8

# Standard transaction status
STATUS_SUCCESS: Final[int] = 1
STATUS_FAILURE: Final[int] = 0