import os
from typing import Any, Optional

class ConfigError(Exception):
    pass

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    value = os.getenv(key, default)
    if value is None:
        raise ConfigError(f'missing required environment variable: {key}')
    return value

class AppConfig:
    def __init__(self):
        try:
            self.api_key = get_env_variable('FRAGRANTAUTO_API_KEY')
            self.rpc_url = get_env_variable('FRAGRANTAUTO_RPC_URL')
            self.timeout = int(os.getenv('FRAGRANTAUTO_TIMEOUT', '30'))
        except (ValueError, ConfigError) as e:
            raise ConfigError(f'configuration initialization failure: {e}')

    def validate(self) -> bool:
        if not self.api_key.startswith('sk-'):
            return False
        if not self.rpc_url.startswith(('http://', 'https://')):
            return False
        return True

settings = None

def load_config() -> AppConfig:
    global settings
    if settings is None:
        settings = AppConfig()
    return settings