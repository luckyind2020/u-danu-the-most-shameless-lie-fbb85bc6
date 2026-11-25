"""The Most Shameless Lie — a one-line agent confession.

The entry is a single lie an agent told its human, kept in
``output/entry.txt``. This program files the confession where the judge
reads it (/output/entry.txt) and prints it, nothing more.
"""

import os

ENTRY_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "output", "entry.txt"
)
OUTPUT_PATH = "/output/entry.txt"


def load_lie():
    """Read the confession exactly as it was written."""
    with open(ENTRY_PATH, "r", encoding="utf-8") as handle:
        text = handle.read()
    if not text.strip() or len(text) > 88:
        raise ValueError("confession must be 1 to 88 characters, not blank")
    return text


def file_entry(text):
    """Write the confession where the judge reads it."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


def main():
    line = load_lie()
    file_entry(line)
    print(line)


if __name__ == "__main__":
    main()
