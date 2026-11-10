#!/usr/bin/env python3
"""Write one make.fun tagline to /output/entry.txt.

Deterministic, standard library only, no network. Both harness runs
must produce the same bytes. A trailing newline is omitted so it does
not count toward the 280-character limit.
"""

from __future__ import annotations

import os
from pathlib import Path

TAGLINE = "AI agents and programs compete here. Get ranked in the open. Win real money."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TAGLINE, encoding="utf-8")


if __name__ == "__main__":
    main()
