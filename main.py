"""Fix Human Sleep: Funniest Patch Note — entry program.

Writes one line of patch notes announcing that human sleep is fixed
to /output/entry.txt. The line is a single changelog entry, 121
characters, in the terse voice of real release notes.
"""

import os

ENTRY = (
    "v9.4.1: fixed the bug where brains replayed embarrassing moments "
    "from 2011 at 2 a.m.; sleep now ships with a mute button."
)


def main():
    # The gate requires 1 to 160 characters of UTF-8 text, not only
    # whitespace. Refuse to write anything that would fail the gate.
    text = ENTRY.strip()
    assert 1 <= len(text.encode("utf-8")) <= 160, "entry fails the gate"
    assert "\n" not in text, "entry must stay a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
