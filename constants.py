from typing import Final

# Network identifiers
MAINNET_CHAIN_ID: Final[int] = 1
BSC_CHAIN_ID: Final[int] = 56

# Token decimal standards
DEFAULT_DECIMALS: Final[int] = 18
USDC_DECIMALS: Final[int] = 6

# Transaction configurations
GAS_BUFFER_PERCENTAGE: Final[float] = 1.2
MAX_RETRIES: Final[int] = 3
TIMEOUT_SECONDS: Final[int] = 30

# Supported DEX protocols
UNISWAP_V3: Final[str] = 'uniswap_v3'
PANCAKESWAP_V3: Final[str] = 'pancakeswap_v3'

# API request constants
USER_AGENT: Final[str] = 'fragrantauto-utils/1.0.0'
CONTENT_TYPE_JSON: Final[str] = 'application/json'

# Error handling constants
RETRYABLE_RPC_ERRORS: Final[tuple] = (
    'Server error',
    'Gateway timeout',
    'Rate limit exceeded'
)

# Formatting defaults
PRECISION_LIMIT: Final[int] = 8