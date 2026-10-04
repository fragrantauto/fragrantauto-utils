"""Common utilities I keep reaching for.

Nothing fancy — just the small helpers I always end up rewriting.
"""
from pathlib import Path
from typing import Iterable


def human_bytes(n: int) -> str:
    """Format a byte count as a human-readable string."""
    units = ("B", "KB", "MB", "GB", "TB")
    i = 0
    while n >= 1024 and i < len(units) - 1:
        n /= 1024.0
        i += 1
    return f"{n:.1f} {units[i]}"


def chunked(seq: Iterable, n: int):
    """Yield successive n-sized chunks from an iterable."""
    buf = []
    for x in seq:
        buf.append(x)
        if len(buf) == n:
            yield buf
            buf = []
    if buf:
        yield buf


def read_lines(p: Path) -> list[str]:
    """Read a file and return its lines, stripped and non-empty."""
    return [ln.strip() for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()]
