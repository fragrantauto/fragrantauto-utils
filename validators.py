import re
from functools import lru_cache

ETH_ADDRESS_RE = re.compile(r"^0x[a-fA-F0-9]{40}$")
BTC_ADDRESS_RE = re.compile(r"^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,39}$")


@lru_cache(maxsize=2048)
def validate_eth_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    return bool(ETH_ADDRESS_RE.match(address))


@lru_cache(maxsize=2048)
def validate_btc_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    return bool(BTC_ADDRESS_RE.match(address))


def fast_batch_validate(addresses: list[str], coin_type: str) -> list[bool]:
    validator_map = {
        "eth": validate_eth_address,
        "btc": validate_btc_address,
    }
    validator = validator_map.get(coin_type.lower())
    if not validator:
        raise ValueError(f"Unsupported currency: {coin_type}")
    return [validator(addr) for addr in addresses]
