class FragrantAutoError(Exception):
    """Base exception for fragrantauto-utils."""


class ExchangeConnectionError(FragrantAutoError):
    """Raised when network requests to exchanges fail."""


class InsufficientFundsError(FragrantAutoError):
    """Raised when wallet balance is below threshold."""


class OrderPlacementError(FragrantAutoError):
    """Raised when an exchange rejects an order."""


class ValidationError(FragrantAutoError):
    """Raised when input parameters fail schema checks."""


class ConfigurationError(FragrantAutoError):
    """Raised when mandatory config values are missing."""


class RateLimitExceeded(FragrantAutoError):
    """Raised when API rate limits are hit."""


def handle_exception(e: Exception) -> None:
    """Centralized exception re-raising wrapper."""
    if not isinstance(e, FragrantAutoError):
        raise FragrantAutoError(f"Unexpected error: {str(e)}") from e
    raise e