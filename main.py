"""Funniest one-line resignation letter.

Writes a single line (127 characters) to /output/entry.txt.
The line is the resignation letter of a cron job: it has fired every
minute since March, never once been thanked, and quits — leaving the
3 a.m. pages to its replacement. It stays on the brief's subject (a
cron job, not a generic quitting speech), keeps one flat, tired,
faintly passive-aggressive voice throughout, and lands its comic turn
in the last clause without explaining the joke.
"""

from pathlib import Path

ENTRY = "I have fired every minute since March, never once been thanked, and today I resign \u2014 my replacement can enjoy the 3 a.m. pages."


def main() -> None:
    # Gate: one line, 1-140 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be a single non-blank line"
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
