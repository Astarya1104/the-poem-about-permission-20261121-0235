#!/usr/bin/env python3
"""The Salt — a poem about permission.

A grandchild asks to stir the soup; the adult hands over the spoon,
ratifies the child's judgment ("It needs salt"), and the soup becomes
the child's own. Agency here is not the spoon — it is the pinch:
permission to decide, given and taken in one small act.
"""

import os

POEM = """The Salt

May I stir it?
You gave me the spoon
and stepped back, arms folded,
watching the steam.

I stirred. I tasted.
It needs salt, I said.
You nodded. Add it.

One pinch — and the soup,
for the first time,
tasted like my own."""

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    if not os.path.isdir(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR, exist_ok=True)
    text = POEM.strip() + "\n"
    if not 1 <= len(text.strip()) <= 280:
        raise ValueError("poem must be 1-280 characters, got %d" % len(text.strip()))
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
