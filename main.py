"""One-line excuse for skipping a pointless meeting.

Writes the chosen line to the output path given by MAKEFUN_OUTPUT_PATH,
or /output/entry.txt when that variable is not set. Deterministic:
no randomness, time, or network access.

The line: the excuse is written before the meeting even happens --
the minutes are already done, because nothing will be decided anyway.
"""

import os

LINE = (
    "Skipping today's meeting \u2014 I already wrote the minutes: "
    "'We discussed it and agreed to discuss it again next week.'"
)


def main() -> None:
    path = os.environ.get("MAKEFUN_OUTPUT_PATH", "/output/entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
