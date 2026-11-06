import os
import json
from typing import Any, Dict

DEFAULTS = {
    "RPC_URL": "https://api.mainnet-beta.solana.com",
    "TIMEOUT": 30,
    "MAX_RETRIES": 3,
    "DEBUG": False
}

class ConfigLoader:
    def __init__(self, path: str = "config.json"):
        self.path = path
        self._config = self._load()

    def _load(self) -> Dict[str, Any]:
        config = DEFAULTS.copy()
        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                try:
                    user_config = json.load(f)
                    config.update(user_config)
                except json.JSONDecodeError:
                    pass
        return config

    def get(self, key: str) -> Any:
        return self._config.get(key)

    def __getitem__(self, key: str) -> Any:
        return self._config[key]