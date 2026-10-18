import json
import os
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "network": "mainnet",
    "rpc_url": "https://rpc.ankr.com/eth",
    "max_slippage": 0.5,
    "gas_limit_multiplier": 1.1,
    "request_timeout": 10,
    "max_retries": 3,
    "enable_auto_trade": False,
}


class ConfigLoader:
    def __init__(self, config_path: str | None = None) -> None:
        self.config_path = Path(config_path) if config_path else None
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        self.reload()

    def reload(self) -> None:
        if self.config_path and self.config_path.is_file():
            with open(self.config_path, "r", encoding="utf-8") as f:
                file_config = json.load(f)
                self._config.update(file_config)
        self._apply_env_overrides()

    def _apply_env_overrides(self) -> None:
        prefix = "FRAGRANT_"
        for key, default_val in DEFAULT_CONFIG.items():
            env_key = f"{prefix}{key.upper()}"
            if env_key in os.environ:
                raw_val = os.environ[env_key]
                if isinstance(default_val, bool):
                    self._config[key] = raw_val.lower() in ("true", "1", "yes")
                elif isinstance(default_val, int):
                    self._config[key] = int(raw_val)
                elif isinstance(default_val, float):
                    self._config[key] = float(raw_val)
                else:
                    self._config[key] = raw_val

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    def as_dict(self) -> Dict[str, Any]:
        return self._config.copy()
