#!/usr/bin/env python3
"""Préparer uniquement les JPEG explicitement nommés, ou les contrôler."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import sys
import tempfile

try:
    from PIL import Image, ImageOps
except ImportError:
    raise SystemExit("Pillow manque dans cet interpréteur Python.") from None

MAX_SIDE = 1600
JPEG_QUALITY = 85
WARN_BYTES = 1024 * 1024
METADATA_KEYS = ("exif", "xmp", "icc_profile", "comment", "photoshop")


def inspect_photo(path: Path) -> tuple[tuple[int, int], list[str]]:
    """Lire et vérifier une image sans modifier le fichier."""
    with Image.open(path) as photo:
        if photo.format != "JPEG":
            raise ValueError(f"{path}: le contenu n'est pas un JPEG")
        photo.load()
        size = photo.size
        issues = []
        if max(size) > MAX_SIDE:
            issues.append(f"côté supérieur à {MAX_SIDE} px")
        if photo.mode != "RGB":
            issues.append(f"mode {photo.mode}, RGB attendu")
        if photo.getexif() or any(photo.info.get(key) for key in METADATA_KEYS):
            issues.append("métadonnées présentes")
        if not (photo.info.get("progressive") or photo.info.get("progression")):
            issues.append("JPEG non progressif")
    if path.stat().st_size > WARN_BYTES:
        issues.append("poids supérieur à 1 Mio")
    return size, issues


def resize_photo(path: Path) -> None:
    """Écrire entièrement le résultat avant de remplacer l'original."""
    temporary = None
    try:
        with Image.open(path) as original:
            photo = ImageOps.exif_transpose(original)
            photo.thumbnail((MAX_SIDE, MAX_SIDE), Image.Resampling.LANCZOS)
            photo = photo.convert("RGB")
            photo.info.clear()
            with tempfile.NamedTemporaryFile(
                dir=path.parent, prefix=f".{path.stem}.", suffix=".tmp", delete=False
            ) as output:
                temporary = Path(output.name)
            photo.save(
                temporary,
                format="JPEG",
                quality=JPEG_QUALITY,
                optimize=True,
                progressive=True,
                exif=b"",
            )
        # Tous les handles sont fermés avant le remplacement, y compris sous Windows.
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="contrôler sans modifier les fichiers"
    )
    parser.add_argument("photos", nargs="+", type=Path, help="chemins JPEG explicites")
    args = parser.parse_args(argv)

    # Vérifier toute la sélection avant la première écriture et éviter les doublons.
    paths = []
    try:
        for supplied in args.photos:
            path = supplied.resolve(strict=True)
            if not path.is_file() or path.suffix.lower() not in {".jpg", ".jpeg"}:
                raise ValueError(f"{supplied}: fichier .jpg ou .jpeg attendu")
            if path not in paths:
                inspect_photo(path)
                paths.append(path)
    except (OSError, ValueError) as error:
        print(f"Erreur : {error}", file=sys.stderr)
        return 1

    failed = False
    for path in paths:
        try:
            before = path.stat().st_size
            if not args.check:
                resize_photo(path)
            size, issues = inspect_photo(path)
            after = path.stat().st_size
            weight = f"{after / 1024:.0f} Kio"
            if not args.check:
                weight = f"{before / 1024:.0f} -> {weight}"
            print(f"{path.name}: {size[0]} x {size[1]} px, {weight}")
            if issues:
                print(f"À signaler : {', '.join(issues)}", file=sys.stderr)
                failed = True
        except (OSError, ValueError) as error:
            print(f"Erreur : {path}: {error}", file=sys.stderr)
            failed = True
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
