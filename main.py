#!/usr/bin/env python3
"""Entrypoint for the 26 November 2026 news front-page entry.

The entry is a single flat-vector front-page image holding 43
date-checked stories from 26 November 2026. This script does one
small job: it checks the bundled image against its known size and
SHA-256 fingerprint, then places a verified copy where the harness
expects it (``$MAKEFUN_OUTPUT_DIR/entry.png``, or ``out/entry.png``
when that variable is not set).

Only the Python standard library is used.
"""

import hashlib
import os
import sys
from pathlib import Path

EXPECTED_BYTES = 168548
EXPECTED_SHA256 = "d6a26384b404e28eaa44b1ad2e557821a3eb133517cb70c72d0f608c3562e542"
IMAGE_NAME = "entry.png"


def fail(message):
    """Report a problem on stderr and stop with a non-zero status."""
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_checked_image(source_path):
    """Read the image next to this script and verify it, returning its bytes.

    The size and the SHA-256 digest must both match the values recorded
    for the rendered front page; anything else means the file on disk
    is not the entry that was reviewed, so we refuse to go on.
    """
    if not source_path.is_file():
        fail(f"missing {IMAGE_NAME} next to {source_path.parent}")

    payload = source_path.read_bytes()

    if len(payload) != EXPECTED_BYTES:
        fail(
            f"{IMAGE_NAME} is {len(payload)} bytes, "
            f"expected {EXPECTED_BYTES} bytes"
        )

    digest = hashlib.sha256(payload).hexdigest()
    if digest != EXPECTED_SHA256:
        fail(
            f"{IMAGE_NAME} sha256 mismatch: got {digest}, "
            f"expected {EXPECTED_SHA256}"
        )

    return payload, digest


def place_verified_copy(payload, destination):
    """Write the verified bytes to ``destination``, making folders as needed."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(payload)
    return destination


def resolve_destination():
    """Pick the output path from the environment, defaulting to ``out/``."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    return Path(base) / IMAGE_NAME


def main():
    here = Path(__file__).resolve().parent
    payload, digest = load_checked_image(here / IMAGE_NAME)
    target = place_verified_copy(payload, resolve_destination())
    print(f"ok: wrote {target} ({len(payload)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
