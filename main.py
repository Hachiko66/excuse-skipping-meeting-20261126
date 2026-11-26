#!/usr/bin/env python3
"""A one-line excuse for dodging a meeting that should never have existed.

The joke: the meeting being skipped was itself scheduled to stand in
for an earlier meeting. The speaker claims they could not attend
because they were busy sitting in the very meeting this one was
supposed to replace. Meetings breeding meetings is the whole gag --
skip one, and there is always another one waiting to take its place.

The script takes the excuse and drops it into a plain text file, one
line and nothing more. The destination comes from the MAKEFUN_OUTPUT_PATH environment
variable; when that variable is absent the file lands at
/output/entry.txt. Nothing here varies from run to run: no clocks,
no dice rolls, no network calls, only the standard library.
"""

import pathlib


EXCUSE = "Sorry I missed the meeting \u2014 I was stuck in the meeting this meeting was called to replace."


def resolve_destination() -> pathlib.Path:
    """Pick where the excuse goes, honouring the environment first."""
    import os

    override = os.environ.get("MAKEFUN_OUTPUT_PATH")
    if override:
        return pathlib.Path(override)
    return pathlib.Path("/output/entry.txt")


def save_excuse(destination: pathlib.Path) -> None:
    """Write the single excuse line to the given file, nothing else."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(EXCUSE, encoding="utf-8")


def run() -> None:
    save_excuse(resolve_destination())


if __name__ == "__main__":
    run()
