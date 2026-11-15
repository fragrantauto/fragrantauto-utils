import json
import os
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, Optional


@dataclass
class CryptoConfig:
    rpc_url: str = "https://eth.llamarpc.com"
    chain_id: int = 1
    request_timeout: int = 30
    max_retries: int = 3
    gas_multiplier: float = 1.15
    api_key: Optional[str] = None

    @classmethod
    def load(cls, config_path: Optional[str] = None) -> "CryptoConfig":
        defaults = asdict(cls())
        file_data: Dict[str, Any] = {}

        if config_path and Path(config_path).is_file():
            with open(config_path, "r", encoding="utf-8") as f:
                file_data = json.load(f)

        env_data = {
            "rpc_url": os.getenv("CRYPTO_RPC_URL"),
            "chain_id": (
                int(os.getenv("CRYPTO_CHAIN_ID"))
                if os.getenv("CRYPTO_CHAIN_ID")
                else None
            ),
            "request_timeout": (
                int(os.getenv("CRYPTO_TIMEOUT"))
                if os.getenv("CRYPTO_TIMEOUT")
                else None
            ),
            "max_retries": (
                int(os.getenv("CRYPTO_MAX_RETRIES"))
                if os.getenv("CRYPTO_MAX_RETRIES")
                else None
            ),
            "gas_multiplier": (
                float(os.getenv("CRYPTO_GAS_MULTIPLIER"))
                if os.getenv("CRYPTO_GAS_MULTIPLIER")
                else None
            ),
            "api_key": os.getenv("CRYPTO_API_KEY"),
        }

        merged = {}
        for key, default_val in defaults.items():
            env_val = env_data.get(key)
            file_val = file_data.get(key)
            if env_val is not None:
                merged[key] = env_val
            elif file_val is not None:
                merged[key] = file_val
            else:
                merged[key] = default_val

        return cls(**merged)
