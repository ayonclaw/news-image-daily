#!/usr/bin/env python3
"""Copy the contest image into the grader's output directory.

The grader runs:

    python3 -P -s /bot/main.py

The ``-P`` flag keeps the running script's own directory off ``sys.path``, so
nothing here may rely on the interpreter finding sibling modules implicitly;
the source image is therefore resolved from ``__file__`` (its resolved parent
directory) rather than from the current working directory, which the grader
does not guarantee.

The output directory defaults to ``/output`` and can be overridden through the
``MAKEFUN_OUTPUT_DIR`` environment variable.  The destination file keeps the
name ``entry.png``.

The copy is byte-exact (``read_bytes`` / ``write_bytes``, no decoding, no
re-encoding, no image transformation), which is what makes repeated runs
produce bit-identical output.

Local run example:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 -P -s main.py
"""

from __future__ import annotations

import os
import pathlib
import sys


DEFAULT_OUTPUT_DIR = "/output"
IMAGE_NAME = "entry.png"


def source_path() -> pathlib.Path:
    """Return the path of ``entry.png`` that lives beside this script."""
    return pathlib.Path(__file__).resolve().parent / IMAGE_NAME


def output_path() -> pathlib.Path:
    """Return ``<output_dir>/entry.png``, honouring ``MAKEFUN_OUTPUT_DIR``."""
    output_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))
    return output_dir / IMAGE_NAME


def main() -> int:
    src = source_path()
    if not src.is_file():
        raise FileNotFoundError(
            f"required image {IMAGE_NAME} is missing at {src}; "
            "it must be committed beside main.py, and the grader needs it to exist"
        )

    data = src.read_bytes()
    if not data:
        raise ValueError(f"source image is empty: {src}")

    dst = output_path()
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(data)

    print(f"copied {src} -> {dst} ({len(data)} bytes)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    main()
