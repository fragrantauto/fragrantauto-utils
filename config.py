import json
import os
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "rpc_url": "https://eth-mainnet.g.alchemy.com/v2/demo",
    "chain_id": 1,
    "request_timeout": 30,
    "max_retries": 3,
    "gas_limit_multiplier": 1.15,
    "slippage_tolerance": 0.5,
}


class Config:
    def __init__(self, settings: Optional[Dict[str, Any]] = None):
        self._settings = DEFAULT_CONFIG.copy()
        if settings:
            self._settings.update(settings)

    @classmethod
    def from_file(cls, filepath: str) -> "Config":
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Config file not found: {filepath}")
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls(data)

    @classmethod
    def from_env(cls, prefix: str = "FRAGRANTAUTO_") -> "Config":
        env_settings = {}
        for key, default_val in DEFAULT_CONFIG.items():
            env_key = f"{prefix}{key.upper()}"
            if env_key in os.environ:
                val = os.environ[env_key]
                if isinstance(default_val, int):
                    env_settings[key] = int(val)
                elif isinstance(default_val, float):
                    env_settings[key] = float(val)
                else:
                    env_settings[key] = val
        return cls(env_settings)

    def get(self, key: str, default: Any = None) -> Any:
        return self._settings.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self._settings[key]

    def to_dict(self) -> Dict[str, Any]:
        return self._settings.copy()
