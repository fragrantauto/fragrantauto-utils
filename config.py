import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any] = None):
        self.config = defaults or {}

    def load_from_file(self, filepath: str) -> None:
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                self.config.update(json.load(f))

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

def load_config(filepath: str, defaults: Dict[str, Any] = None) -> Dict[str, Any]:
    loader = ConfigLoader(defaults)
    loader.load_from_file(filepath)
    return loader.config