"""Vérifications sur des images temporaires, sans toucher aux photos du dépôt."""

import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from PIL import Image

import resize_photos


class PhotoTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.root = Path(self.directory.name)
        self.addCleanup(self.directory.cleanup)

    def run_cli(self, *args):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(
            io.StringIO()
        ):
            return resize_photos.main([str(arg) for arg in args])

    def make_jpeg(self, name="photo.jpg", size=(2400, 1200), **options):
        path = self.root / name
        Image.new("RGB", size, "red").save(path, format="JPEG", **options)
        return path

    def test_orientation_dimensions_metadata_and_progressive(self):
        exif = Image.Exif()
        exif[274] = 6  # Rotation de 90 degrés vers la droite.
        exif[315] = "Métadonnée à supprimer"
        source = self.make_jpeg("photo.JPG", exif=exif, comment=b"private")
        self.assertEqual(self.run_cli(source), 0)
        with Image.open(source) as photo:
            self.assertEqual(photo.size, (800, 1600))
            self.assertEqual(photo.mode, "RGB")
            self.assertFalse(photo.getexif())
            self.assertNotIn("comment", photo.info)
            self.assertTrue(photo.info.get("progressive"))
        self.assertEqual(self.run_cli("--check", source), 0)

    def test_check_never_changes_input_and_reports_noncompliance(self):
        source = self.make_jpeg()
        before = source.read_bytes()
        self.assertEqual(self.run_cli("--check", source), 1)
        self.assertEqual(source.read_bytes(), before)

    def test_small_photo_not_enlarged_and_selection_deduplicated(self):
        source = self.make_jpeg("petite photo.jpeg", size=(120, 80))
        other = self.make_jpeg("autre.jpg")
        before_other = other.read_bytes()
        with patch.object(
            resize_photos, "resize_photo", wraps=resize_photos.resize_photo
        ) as operation:
            self.assertEqual(self.run_cli(source, source), 0)
            self.assertEqual(operation.call_count, 1)
        with Image.open(source) as photo:
            self.assertEqual(photo.size, (120, 80))
        self.assertEqual(other.read_bytes(), before_other)

    def test_invalid_selection_rejected_before_any_write(self):
        source = self.make_jpeg()
        before = source.read_bytes()
        impostor = self.root / "faux.jpg"
        Image.new("RGB", (10, 10)).save(impostor, format="PNG")
        self.assertEqual(self.run_cli(source, impostor), 1)
        self.assertEqual(self.run_cli(source, self.root / "absent.jpg"), 1)
        self.assertEqual(source.read_bytes(), before)

    def test_failed_replace_preserves_original_and_cleans_temporary(self):
        source = self.make_jpeg()
        before = source.read_bytes()
        with patch.object(resize_photos.os, "replace", side_effect=OSError("verrou")):
            self.assertEqual(self.run_cli(source), 1)
        self.assertEqual(source.read_bytes(), before)
        self.assertEqual(list(self.root.iterdir()), [source])

    def test_no_implicit_batch_and_large_file_warning(self):
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            resize_photos.main([])
        source = self.make_jpeg(size=(10, 10), progressive=True)
        with source.open("ab") as output:
            output.write(b"\0" * (1024 * 1024))
        before = source.read_bytes()
        self.assertEqual(self.run_cli("--check", source), 1)
        self.assertEqual(source.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
