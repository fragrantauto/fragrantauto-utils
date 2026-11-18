import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://api.mainnet-beta.solana.com",
    "timeout": 30,
    "retry_limit": 3,
    "log_level": "INFO"
}

def load_config(path: str = "config.json") -> Dict[str, Any]:
    config = DEFAULT_CONFIG.copy()
    if os.path.exists(path):
        with open(path, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    return config

class ConfigManager:
    def __init__(self, path: str = "config.json"):
        self._config = load_config(path)

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        return self._config.copy()