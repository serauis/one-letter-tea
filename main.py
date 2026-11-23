#!/usr/bin/env python3
"""Entry for make.fun — One Letter: Coffee or Tea.

The competition asks for exactly one letter: A for coffee, B for tea.
This entry answers B, for tea.

The program writes a single byte, the letter "B", into the file the
grader reads, /output/entry.txt. It creates the output folder when
needed, and writes in binary mode so that no newline or extra byte
can sneak in. An ENTRY_OUTPUT environment variable may point the
output elsewhere for local testing; the default is /output/entry.txt.
"""

import os

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
LETTER = b"B"


def write_letter() -> None:
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as out:
        out.write(LETTER)


if __name__ == "__main__":
    write_letter()
