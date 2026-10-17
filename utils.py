import hashlib
import hmac
import time
from typing import Any, Dict


def satoshi_to_btc(satoshi: int) -> float:
    return satoshi / 100_000_000.0


def btc_to_satoshi(btc: float) -> int:
    return int(btc * 100_000_000)


def wei_to_eth(wei: int) -> float:
    return wei / 10**18


def eth_to_wei(eth: float) -> int:
    return int(eth * 10**18)


def generate_signature(secret: str, message: str) -> str:
    return hmac.new(
        secret.encode("utf-8"),
        message.encode("utf-8"),
        hashlib.sha256
    ).hexdigest()


def prepare_signed_payload(params: Dict[str, Any], secret: str) -> Dict[str, Any]:
    payload = params.copy()
    payload["timestamp"] = int(time.time() * 1000)
    query_string = "&".join(f"{k}={v}" for k, v in sorted(payload.items()))
    payload["signature"] = generate_signature(secret, query_string)
    return payload
