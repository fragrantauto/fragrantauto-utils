import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://mainnet.infura.io/v3/",
    "timeout": 30,
    "retries": 3,
    "log_level": "INFO"
}

class ConfigLoader:
    def __init__(self, path: str = "config.json"):
        self.path = path
        self.settings = self._load()

    def _load(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            return DEFAULT_CONFIG.copy()
        
        with open(self.path, "r") as f:
            try:
                data = json.load(f)
                return {**DEFAULT_CONFIG, **data}
            except json.JSONDecodeError:
                return DEFAULT_CONFIG.copy()

    def get(self, key: str, default: Any = None) -> Any:
        return self.settings.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self.settings[key]