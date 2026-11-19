# Entry for news-image-20261119: "Sum up 19 November's world news in one image".
# The image is a newspaper front page for Thursday 19 November 2026, drawn
# in advance (entry.png beside this file); this program copies it to the
# output directory. Standard library only, no network, deterministic: the
# same bytes are written on every run. After copying, the program verifies
# the output byte for byte against the source, so a partial or truncated
# write fails loudly instead of silently entering a broken image.
import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


SRC = HERE / "entry.png"
DST = OUT / "entry.png"

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, DST)
if _sha256(SRC) != _sha256(DST):
    raise SystemExit("entry.png copy failed integrity check")
if DST.stat().st_size > 1048576:
    raise SystemExit("entry.png exceeds the 1 MiB limit")
