import re
from typing import Tuple, Union


def wei_to_ether(wei: int) -> float:
    return wei / 10**18


def ether_to_wei(ether: Union[float, int, str]) -> int:
    return int(float(ether) * 10**18)


def calculate_slippage(price: float, percentage: float) -> Tuple[float, float]:
    delta = price * (percentage / 100.0)
    return max(0.0, price - delta), price + delta


def truncate_address(address: str, leading: int = 6, trailing: int = 4) -> str:
    if not address or len(address) <= leading + trailing:
        return address
    return f"{address[:leading]}...{address[-trailing:]}"


def is_valid_eth_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))
