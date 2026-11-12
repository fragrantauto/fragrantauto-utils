import hashlib
from typing import Union


def satoshi_to_btc(satoshis: int) -> float:
    if satoshis < 0:
        raise ValueError("Satoshis cannot be negative")
    return satoshis / 100_000_000


def btc_to_satoshi(btc: Union[int, float]) -> int:
    if btc < 0:
        raise ValueError("BTC cannot be negative")
    return int(round(btc * 100_000_000))


def sha256d(data: bytes) -> bytes:
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()


def normalize_hex(hex_str: str) -> str:
    cleaned = hex_str.strip().lower()
    if cleaned.startswith("0x"):
        cleaned = cleaned[2:]
    if len(cleaned) % 2 != 0:
        cleaned = "0" + cleaned
    return cleaned


def is_valid_hex(hex_str: str) -> bool:
    try:
        bytes.fromhex(normalize_hex(hex_str))
        return True
    except ValueError:
        return False
