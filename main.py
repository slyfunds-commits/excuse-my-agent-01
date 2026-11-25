#!/usr/bin/env python3
"""The Excuse My Agent Gave Me.

Writes one line to /output/entry.txt: the excuse an AI agent hands its
human for missing a deadline. Pure standard library only.

The line is straight-faced and proud at once: the agent did exactly what
it was asked — it verified every number — and the verification itself is
the reason the deadline slipped. The punch lands in the last few words,
where the specific count (1,204 of 3,811) turns a dutiful report into the
excuse. No trailing newline is written, so the entry is exactly the line.
"""

import os

KEEPER = "You asked me to verify every number. Number 1,204 of 3,811 checks out."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(KEEPER)


if __name__ == "__main__":
    main()
