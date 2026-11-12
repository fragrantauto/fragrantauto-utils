import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://api.mainnet-beta.solana.com",
    "timeout": 30,
    "retry_limit": 3
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
        self.data = load_config(path)

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)