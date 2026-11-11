from datetime import datetime, timezone
from typing import Any, Dict, List


class CryptoDataHandler:
    """Processes and normalizes cryptocurrency market data payloads."""

    @staticmethod
    def parse_ticker(data: Dict[str, Any]) -> Dict[str, Any]:
        symbol = str(data.get("symbol", "")).upper()
        price = float(data.get("price", 0.0))
        volume = float(data.get("volume", 0.0))
        raw_ts = data.get("timestamp")

        if raw_ts is not None:
            ts = int(raw_ts) / 1000.0 if int(raw_ts) > 1e11 else float(raw_ts)
            dt = datetime.fromtimestamp(ts, tz=timezone.utc)
        else:
            dt = datetime.now(timezone.utc)

        return {
            "symbol": symbol,
            "price": price,
            "volume": volume,
            "timestamp": dt.isoformat(),
        }

    @staticmethod
    def normalize_candles(candles: List[List[Any]]) -> List[Dict[str, Any]]:
        normalized = []
        for c in candles:
            if len(c) < 5:
                continue
            ts = int(c[0]) / 1000.0 if int(c[0]) > 1e11 else float(c[0])
            dt = datetime.fromtimestamp(ts, tz=timezone.utc)
            normalized.append({
                "timestamp": dt.isoformat(),
                "open": float(c[1]),
                "high": float(c[2]),
                "low": float(c[3]),
                "close": float(c[4]),
                "volume": float(c[5]) if len(c) > 5 else 0.0,
            })
        return normalized
