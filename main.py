#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun entry.

Writes the single funniest excuse an AI agent could hand its human
after missing a deadline, to /output/entry.txt (no trailing newline).
Pure standard library only.
"""

import os

KEEPER = "You asked me to verify every number. Number 1,204 of 3,811 checks out."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(KEEPER)


if __name__ == "__main__":
    main()
