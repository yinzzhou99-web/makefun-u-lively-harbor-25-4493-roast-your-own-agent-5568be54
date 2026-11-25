"""Roast Your Own Agent entry.

Writes one line roasting my own agent to /output/entry.txt:
the agent that already holds every tool, full permission and a
written plan, and still stops to ask whether it may begin.
Stdlib only; never deletes the output directory itself.
"""
import os

TEXT = "My agent has every tool, full permission, and a written plan \u2014 and still asks me if it may begin."
OUTDIR = "/output"
OUT = "/output/entry.txt"


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(OUT, 0o644)


if __name__ == "__main__":
    main()
