import json
from pathlib import Path
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, filepath: str, defaults: Dict[str, Any] = None):
        self.path = Path(filepath)
        self.defaults = defaults or {}
        self.config = self._load()

    def _load(self) -> Dict[str, Any]:
        if not self.path.exists():
            return self.defaults
        try:
            with open(self.path, 'r') as f:
                data = json.load(f)
            return {**self.defaults, **data}
        except (json.JSONDecodeError, IOError):
            return self.defaults

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self.config[key]

    def save(self) -> None:
        with open(self.path, 'w') as f:
            json.dump(self.config, f, indent=4)