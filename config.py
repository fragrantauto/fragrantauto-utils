import os
import json
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any] = None):
        self.config = defaults or {}

    def load_from_env(self, prefix: str = 'FA_') -> None:
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower()
                self.config[config_key] = self._parse_value(value)

    def load_from_json(self, filepath: str) -> None:
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                self.config.update(json.load(f))

    def _parse_value(self, value: str) -> Any:
        if value.lower() in ('true', 'false'):
            return value.lower() == 'true'
        try:
            if '.' in value:
                return float(value)
            return int(value)
        except ValueError:
            return value

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

def get_config() -> ConfigLoader:
    defaults = {'rpc_url': 'http://localhost:8545', 'timeout': 30}
    loader = ConfigLoader(defaults)
    loader.load_from_json('config.json')
    loader.load_from_env()
    return loader