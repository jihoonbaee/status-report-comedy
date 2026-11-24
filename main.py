#!/usr/bin/env python3
"""Status Report Comedy Sprint entry.

Writes one original status-report line to /output/entry.txt.
No network calls, no environment secrets, no files outside this repo.
"""

import os

ENTRY = "Weekly report: 31 tasks done, 1 mistake made \u2014 I told you about it. It will not happen again."


def main():
    # Self-check the gate before writing: UTF-8 text of 1 to 200
    # characters, not only whitespace. Fail loudly instead of
    # writing an entry the gate would refuse.
    ENTRY.encode("utf-8")
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} characters, must be 1-200")
    if not ENTRY.strip():
        raise ValueError("entry is only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
