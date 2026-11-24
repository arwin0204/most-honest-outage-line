"""The Most Honest Outage Line — make.fun program/v1 entry.

Writes a single honest status-page line (at most 160 characters) to
/output/entry.txt. The line is fixed and deterministic: every run writes
the exact same bytes, with no trailing newline.
"""

import os

ENTRY = (
    "Every server I run on is down, so I can't check what's broken "
    "or when we'll be back \u2014 I'll update this page the moment I "
    "can see anything again."
)

MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"


def validate_entry(entry: str) -> None:
    """Check the entry against the gate: 1-160 chars, one line, not blank."""
    if not 1 <= len(entry) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(entry)}")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")


def write_entry(entry: str, path: str = OUTPUT_PATH) -> None:
    """Write the entry exactly as given: no trailing newline added."""
    validate_entry(entry)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)


def main() -> None:
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
