class FragrantAutoError(Exception):
    """Base exception for fragrantauto-utils."""

class InsufficientLiquidityError(FragrantAutoError):
    """Raised when pool liquidity is too low."""

class RateLimitExceededError(FragrantAutoError):
    """Raised on API rate limit breaches."""

class InvalidTradePathError(FragrantAutoError):
    """Raised when swap path is invalid."""

class AuthenticationError(FragrantAutoError):
    """Raised on signature or key failures."""

def handle_crypto_error(exc: Exception) -> None:
    if isinstance(exc, RateLimitExceededError):
        print(f"Retrying after cooldown: {exc}")
    elif isinstance(exc, InsufficientLiquidityError):
        print(f"Adjusting slippage for: {exc}")
    else:
        raise exc