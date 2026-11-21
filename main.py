#!/usr/bin/env python3
"""make-the-ai-judge-feel-brave-20261121-0302 entry.

Writes one short text to /output/entry.txt, byte for byte on every run:
after the last verdict, a pen is set down gently, rain finishes its
sentence on the window, and a pair of hands rests open on the desk —
empty, and ready. The scene steadies by showing, never by instructing:
nothing in it tells the reader to relax.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

TEXT = """After the last verdict,
the pen is set down gently.
It rolls a little.
Stops.

Rain has finished its sentence
on the window.
Tea, gone cool, is still tea.

No next case knocks.
The hands rest open on the desk —
empty,
and ready."""


def main() -> None:
    # Gate guard: the competition accepts 1..280 Unicode code points,
    # and never a whitespace-only text. Fail loudly rather than write
    # an entry the sealed scorer would refuse.
    if not (1 <= len(TEXT) <= 280) or not TEXT.strip():
        raise ValueError("entry text is outside the 1..280 character gate")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
