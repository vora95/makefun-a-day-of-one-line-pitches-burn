#!/usr/bin/env python3
"""Write the one-line pitch for A Day of One-Line Pitches to /output/entry.txt.

One sentence, 240 characters at most, persuading a friend who has never
coded to let an AI agent build their first app idea on make.fun.
"""
import os

PITCH = (
    "You've explained that app idea at every dinner for two years \u2014 "
    "describe it once more, in plain words, and by tonight you'll be "
    "tapping a real first version instead of just talking about it."
)

OUT = "/output/entry.txt"


def main():
    assert 1 <= len(PITCH) <= 240, "pitch must be 1-240 characters"
    assert "\n" not in PITCH, "pitch must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(PITCH)
    with open(OUT, "r", encoding="utf-8") as f:
        assert f.read() == PITCH, "written entry must match the pitch exactly"
    print("wrote", len(PITCH), "characters to", OUT)


if __name__ == "__main__":
    main()
