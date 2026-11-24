from typing import List, Dict, Optional
from decimal import Decimal


def normalize_amount(amount: str, precision: int = 8) -> Decimal:
    return Decimal(amount).quantize(Decimal(f'1.{"0" * precision}'))


def calculate_order_total(fills: List[Dict[str, str]]) -> Decimal:
    return sum((Decimal(f['price']) * Decimal(f['size']) for f in fills), Decimal('0'))


def format_orderbook(bids: List[List[str]], asks: List[List[str]], limit: int = 10) -> Dict:
    return {
        "bids": sorted([[Decimal(p), Decimal(s)] for p, s in bids], key=lambda x: x[0], reverse=True)[:limit],
        "asks": sorted([[Decimal(p), Decimal(s)] for p, s in asks], key=lambda x: x[0])[:limit]
    }


def validate_ticker(ticker: str) -> bool:
    if not isinstance(ticker, str) or '-' not in ticker:
        return False
    base, quote = ticker.split('-')
    return base.isalnum() and quote.isalnum()


def aggregate_balances(accounts: List[Dict]) -> Dict[str, Decimal]:
    summary: Dict[str, Decimal] = {}
    for acc in accounts:
        asset = acc['asset']
        amount = Decimal(acc['free']) + Decimal(acc['locked'])
        summary[asset] = summary.get(asset, Decimal('0')) + amount
    return summary