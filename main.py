#!/usr/bin/env python3
"""The 3AM Fridge Text.

Writes the one line a smart fridge would text its owner at 3am
to /output/entry.txt. One line, 135 characters, no trailing newline
so the file holds exactly the message.
"""

import os

LINE = "3am. Fourth time tonight you've opened me just to stare. Pick something or close me \u2014 I'm cold, and I'm tired of being your nightlight."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
