from decimal import Decimal
from typing import Dict, List, Tuple, Union


def calculate_vwap(trades: List[Dict[str, Union[float, str, Decimal]]]) -> Decimal:
    if not trades:
        raise ValueError("Trade list cannot be empty")

    total_volume = Decimal("0")
    total_volume_price = Decimal("0")

    for trade in trades:
        price = Decimal(str(trade["price"]))
        volume = Decimal(str(trade["volume"]))

        if price <= 0 or volume <= 0:
            continue

        total_volume += volume
        total_volume_price += price * volume

    if total_volume == Decimal("0"):
        raise ValueError("Total volume must be greater than zero")

    return total_volume_price / total_volume


def normalize_symbol(symbol: str) -> str:
    cleaned = symbol.upper().replace("-", "").replace("_", "").replace("/", "")
    if not cleaned.isalnum():
        raise ValueError(f"Invalid symbol format: {symbol}")
    return cleaned


def format_orderbook_depth(
    bids: List[Tuple[float, float]], asks: List[Tuple[float, float]], max_depth: int = 10
) -> Dict[str, List[Dict[str, Decimal]]]:
    formatted_bids = [
        {"price": Decimal(str(p)), "quantity": Decimal(str(q))}
        for p, q in sorted(bids, key=lambda x: x[0], reverse=True)[:max_depth]
    ]
    formatted_asks = [
        {"price": Decimal(str(p)), "quantity": Decimal(str(q))}
        for p, q in sorted(asks, key=lambda x: x[0])[:max_depth]
    ]
    return {"bids": formatted_bids, "asks": formatted_asks}
