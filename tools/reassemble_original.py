#!/usr/bin/env python3
"""Reassemble the original 2026-11-19 four-style DINO project from GitHub chunk files."""
import argparse, hashlib, pathlib, zipfile
EXPECTED_SHA256 = "48cfd510a01155bbfa7d6e40380957e3258b9895f56c1d53fe10a77127216b0e"
EXPECTED_SIZE = 9327572

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--parts-dir", default="archives/original_four_styles_parts")
    p.add_argument("--output", default="DINO_FOUR_STYLES_EDITABLE_PROJECT.zip")
    args = p.parse_args()
    parts = sorted(pathlib.Path(args.parts_dir).glob("DINO_FOUR_STYLES_EDITABLE_PROJECT.zip.part???"))
    if len(parts) != 10:
        raise SystemExit(f"Expected 10 parts, found {len(parts)} in {args.parts_dir}")
    for i, part in enumerate(parts):
        if part.name != f"DINO_FOUR_STYLES_EDITABLE_PROJECT.zip.part{i:03d}":
            raise SystemExit(f"Unexpected file order: {part.name}")
    out = pathlib.Path(args.output)
    digest = hashlib.sha256()
    count = 0
    with out.open("wb") as w:
        for part in parts:
            with part.open("rb") as f:
                while (chunk := f.read(1024 * 1024)):
                    w.write(chunk)
                    digest.update(chunk)
                    count += len(chunk)
    if count != EXPECTED_SIZE or digest.hexdigest() != EXPECTED_SHA256:
        out.unlink(missing_ok=True)
        raise SystemExit("Integrity mismatch: original ZIP NOT reconstructed; output removed")
    with zipfile.ZipFile(out) as z:
        bad = z.testzip()
        if bad:
            out.unlink(missing_ok=True)
            raise SystemExit(f"ZIP CRC mismatch in {bad}")
    print(f"Restored {out} ({count} bytes) SHA256={digest.hexdigest()}")

if __name__ == "__main__":
    main()
