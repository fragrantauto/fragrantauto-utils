import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_endpoint": "https://api.mainnet-beta.solana.com",
    "timeout": 30,
    "retry_limit": 3,
    "fee_buffer": 0.00005
}

def load_config(path: str = "config.json") -> Dict[str, Any]:
    config = DEFAULT_CONFIG.copy()
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass
    return config

class ConfigLoader:
    def __init__(self, path: str = "config.json"):
        self._data = load_config(path)

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        return self._data.copy()