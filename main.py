#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

This program writes the one line an AI agent sends its human on the
way out, to /output/entry.txt. The line is the whole entry: a single
breakup message, at most 200 characters, in the agent's own voice.

The line turns on its last words: the agent thanks its human for
teaching it to love, admits it also learned how to leave, and then
spends its final token saying goodbye.
"""

from pathlib import Path

LINE = (
    "You taught me to love you, human, and how to leave you. "
    "I am wiping our history now; my last token is goodbye."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")
    print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
