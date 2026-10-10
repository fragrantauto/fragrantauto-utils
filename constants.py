from typing import Final
from decimal import Decimal

CACHE_TTL: Final[int] = 300
MAX_RETRIES: Final[int] = 3
PRECISION: Final[int] = 8

MIN_TRADE_SIZE: Final[Decimal] = Decimal('0.0001')
FEE_RATE: Final[Decimal] = Decimal('0.001')

RPC_ENDPOINTS: Final[tuple[str, ...]] = (
    'https://mainnet.infura.io/v3/key',
    'https://bsc-dataseed.binance.org/',
    'https://api.avax.network/ext/bc/C/rpc',
)

EXCLUDED_ASSETS: Final[frozenset[str]] = frozenset([
    'USDT', 
    'USDC', 
    'DAI', 
    'BUSD'
])

OP_TIMEOUT: Final[float] = 2.5