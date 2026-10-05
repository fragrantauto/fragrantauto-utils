import os
import json
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any]):
        self._config = defaults

    def load(self, path: str) -> None:
        if not os.path.exists(path):
            return
        try:
            with open(path, 'r') as f:
                user_config = json.load(f)
                self._config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        return self._config.copy()

def get_config(path: str = 'config.json') -> ConfigLoader:
    defaults = {
        "rpc_url": "https://api.mainnet-beta.solana.com",
        "timeout": 30,
        "retries": 3,
        "debug": False
    }
    loader = ConfigLoader(defaults)
    loader.load(path)
    return loader