import os
from typing import Dict, Any
from dataclasses import dataclass

@dataclass(frozen=True)
class ChainConfig:
    chain_id: int
    rpc_url: str
    symbol: str

class AppConfig:
    def __init__(self) -> None:
        self.networks: Dict[str, ChainConfig] = {
            "ethereum": ChainConfig(1, os.getenv("ETH_RPC", ""), "ETH"),
            "bsc": ChainConfig(56, os.getenv("BSC_RPC", ""), "BNB"),
        }

    def get_network(self, name: str) -> ChainConfig:
        """Retrieve configuration for a specific chain."""
        if name not in self.networks:
            raise ValueError(f"Network {name} not configured")
        return self.networks[name]

    @property
    def debug_mode(self) -> bool:
        """Return global debug flag state."""
        return os.getenv("DEBUG", "false").lower() == "true"

def load_config() -> AppConfig:
    """Factory for application configuration."""
    return AppConfig()