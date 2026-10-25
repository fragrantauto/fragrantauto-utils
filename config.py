import os
import json
from typing import Any, Dict

DEFAULTS = {
    "RPC_URL": "https://api.mainnet-beta.solana.com",
    "TIMEOUT": 30,
    "MAX_RETRIES": 3,
    "DEBUG": False
}

def load_config(path: str = "config.json") -> Dict[str, Any]:
    config = DEFAULTS.copy()
    if os.path.exists(path):
        with open(path, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    return config

class Config:
    def __init__(self, path: str = "config.json"):
        self._data = load_config(path)

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    def __getattr__(self, name: str) -> Any:
        if name in self._data:
            return self._data[name]
        raise AttributeError(f"config has no attribute {name}")