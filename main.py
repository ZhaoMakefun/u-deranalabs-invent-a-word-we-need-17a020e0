#!/usr/bin/env python3
"""Invent a Word We Need entry.

Writes one coined word with a one-line definition (at most 140
characters) to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).

The word: "planlief" — the quiet relief of a plan being cancelled,
sweetest when you were already dressed to go out. English has no word
for that specific, instantly recognisable feeling: the dread of going
out flips to relief in one message, and the fact you were already
dressed makes the relief sharper, not weaker. The word is built from
familiar parts (plan + relief), so it is sayable, spellable and easy
to remember, and the definition lands in a single reading.
"""

import os
import sys

ENTRY = (
    "planlief \u2014 the quiet relief of a plan being cancelled, "
    "sweetest when you were already dressed to go out."
)

MAX_CHARS = 140


def main() -> int:
    text = ENTRY.strip()
    # Gate check: 1-140 characters, UTF-8, not only whitespace.
    if not text or len(text) > MAX_CHARS:
        print(f"entry invalid: {len(text)} chars", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry invalid: must be a single line", file=sys.stderr)
        return 1
    # The entry must be a word plus its definition, joined by an em dash.
    if " \u2014 " not in text:
        print("entry invalid: word and definition must be joined by ' \u2014 '", file=sys.stderr)
        return 1
    text.encode("utf-8")  # raises if not encodable, which it always is
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
