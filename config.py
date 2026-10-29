import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://mainnet.infura.io/v3/",
    "timeout": 30,
    "retry_attempts": 3,
    "gas_buffer": 1.2
}

class ConfigLoader:
    def __init__(self, path: str = "config.json"):
        self.path = path
        self.data = self._load()

    def _load(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            return DEFAULT_CONFIG
        with open(self.path, "r") as f:
            try:
                user_config = json.load(f)
                return {**DEFAULT_CONFIG, **user_config}
            except json.JSONDecodeError:
                return DEFAULT_CONFIG

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self.data[key]

    def __repr__(self) -> str:
        return f"ConfigLoader(data={self.data})"