class FragrantAutoError(Exception):
    """Base exception for fragrantauto-utils."""


class ConnectionTimeoutError(FragrantAutoError):
    """Raised when network requests exceed threshold."""


class RateLimitError(FragrantAutoError):
    """Raised when API rate limits are exceeded."""


class ValidationError(FragrantAutoError):
    """Raised when cryptographic inputs are invalid."""


class InsufficientFundsError(FragrantAutoError):
    """Raised when wallet balance is too low."""


def handle_crypto_error(err: Exception) -> None:
    if isinstance(err, (ConnectionTimeoutError, RateLimitError)):
        # Trigger exponential backoff logic
        pass
    elif isinstance(err, ValidationError):
        # Log malformed signature or key
        pass
    elif isinstance(err, InsufficientFundsError):
        # Abort transaction flow
        pass
    else:
        raise err