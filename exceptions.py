class FragrantAutoError(Exception):
    pass

class ExchangeConnectionError(FragrantAutoError):
    pass

class RateLimitExceeded(FragrantAutoError):
    pass

class DataProcessingError(FragrantAutoError):
    pass

class ValidationError(FragrantAutoError):
    pass

EXCEPTION_MAP = {
    'connection': ExchangeConnectionError,
    'ratelimit': RateLimitExceeded,
    'processing': DataProcessingError,
    'validation': ValidationError
}

def get_exception(exc_type: str) -> type[FragrantAutoError]:
    return EXCEPTION_MAP.get(exc_type, FragrantAutoError)

class ExceptionHandler:
    __slots__ = ('logger',)

    def __init__(self, logger):
        self.logger = logger

    def handle(self, e: Exception) -> None:
        if isinstance(e, FragrantAutoError):
            self.logger.error(f'FragrantAuto internal error: {e}')
        else:
            self.logger.critical(f'Unhandled system error: {e}')