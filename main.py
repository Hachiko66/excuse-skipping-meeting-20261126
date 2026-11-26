"""One-line excuse for skipping a pointless meeting.

Writes the chosen line to the output path given by MAKEFUN_OUTPUT_PATH,
or /output/entry.txt when that variable is not set. Deterministic:
no randomness, time, or network access.

The line: the excuse is itself a meeting joke -- the skipped meeting
existed only to replace another meeting, and the speaker was trapped
in that original meeting instead. The recursion is the punchline:
meetings now spawn meetings, and attending any of them is optional.
"""

import os

LINE = (
    "Sorry I missed the meeting \u2014 I was stuck in the meeting "
    "this meeting was called to replace."
)


def main() -> None:
    path = os.environ.get("MAKEFUN_OUTPUT_PATH", "/output/entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
