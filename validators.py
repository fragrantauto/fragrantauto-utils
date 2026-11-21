import re
from typing import Optional

class AddressValidator:
    ETH_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')
    BTC_PATTERN = re.compile(r'^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,39}$')

    @staticmethod
    def is_eth(address: str) -> bool:
        return bool(AddressValidator.ETH_PATTERN.match(address))

    @staticmethod
    def is_btc(address: str) -> bool:
        return bool(AddressValidator.BTC_PATTERN.match(address))

class ConfigValidator:
    @staticmethod
    def validate_api_key(key: Optional[str]) -> bool:
        return isinstance(key, str) and len(key) >= 32

    @staticmethod
    def validate_threshold(val: float) -> bool:
        return isinstance(val, (int, float)) and val > 0

def validate_transaction(address: str, amount: float) -> bool:
    if not AddressValidator.is_eth(address) and not AddressValidator.is_btc(address):
        return False
    return ConfigValidator.validate_threshold(amount)