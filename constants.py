from enum import Enum

class CryptoErrorCodes(Enum):
    INVALID_ASSET = 1001
    INSUFFICIENT_LIQUIDITY = 1002
    NETWORK_TIMEOUT = 1003
    RATE_LIMIT_EXCEEDED = 1004
    INVALID_SIGNATURE = 1005
    EXCHANGE_MAINTENANCE = 1006

ERROR_MESSAGES = {
    CryptoErrorCodes.INVALID_ASSET: "the specified asset is not supported",
    CryptoErrorCodes.INSUFFICIENT_LIQUIDITY: "insufficient liquidity for trade execution",
    CryptoErrorCodes.NETWORK_TIMEOUT: "network request timed out",
    CryptoErrorCodes.RATE_LIMIT_EXCEEDED: "rate limit quota exceeded",
    CryptoErrorCodes.INVALID_SIGNATURE: "provided cryptographic signature is invalid",
    CryptoErrorCodes.EXCHANGE_MAINTENANCE: "exchange is currently under maintenance"
}

MAX_RETRIES = 3
TIMEOUT_SECONDS = 30
SUPPORTED_NETWORKS = {"ethereum", "bsc", "polygon", "solana"}