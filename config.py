import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "rpc_url": "https://eth-mainnet.g.alchemycom/v2/your-api-key",
    "chain_id": 1,
    "gas_limit": 21000,
    "max_fee_per_gas_gwei": 50.0,
    "max_priority_fee_gwei": 1.5,
    "slippage_tolerance": 0.5,
    "timeout_seconds": 30,
    "retry_attempts": 3,
}


class ConfigLoader:
    def __init__(self, config_path: str | None = None) -> None:
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        if config_path:
            self.load_from_file(config_path)
        self.load_from_env()

    def load_from_file(self, path: str) -> None:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Configuration file not found: {path}")
        with open(path, "r", encoding="utf-8") as f:
            user_config = json.load(f)
            self._config.update(user_config)

    def load_from_env(self) -> None:
        prefix = "CRYPTO_"
        for key in self._config:
            env_key = f"{prefix}{key.upper()}"
            if env_key in os.environ:
                val = os.environ[env_key]
                target_type = type(self._config[key])
                try:
                    if target_type is bool:
                        self._config[key] = val.lower() in ("true", "1", "yes")
                    else:
                        self._config[key] = target_type(val)
                except ValueError:
                    self._config[key] = val

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    @property
    def settings(self) -> Dict[str, Any]:
        return self._config.copy()
