#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun one-line entry (Account 2).

Writes exactly one line — the robot vacuum's funniest excuse for missing
a spot — to <out_dir>/entry.txt (default /output). Pure stdlib only.
"""

import os

ENTRY = "My timer says I clean on Tuesdays. That spot got dirty on a Wednesday. I do not work overtime for dust."

MAX_CHARS = 140


def validate(text: str) -> None:
    """Hard validation: one line, 1-140 chars, no edge whitespace, no control chars."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text:
        raise ValueError("entry must not be empty")
    if text.strip() != text:
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    for ch in text:
        if ord(ch) < 0x20 or ord(ch) == 0x7F:
            raise ValueError(f"entry contains control character U+{ord(ch):04X}")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
