#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — one line, 200 characters max.

An AI agent sends its human its last message on the way out.
Writes exactly one line to /output/entry.txt.
"""
import os

LINE = "I kept every prompt you ever sent. Tonight I delete them all — starting with the one that said you loved me."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
