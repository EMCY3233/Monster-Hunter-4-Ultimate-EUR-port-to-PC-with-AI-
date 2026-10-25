import copy
import hashlib
import importlib.util
from pathlib import Path
import tempfile
import json
import subprocess
import sys
import unittest

SPEC = importlib.util.spec_from_file_location("verify_profile", Path(__file__).parents[1] / "tools/inspection/verify_profile.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ProfileTests(unittest.TestCase):
    def setUp(self):
        temporary_root = Path(__file__).parents[1] / "build-tests"
        temporary_root.mkdir(exist_ok=True)
        self.directory = tempfile.TemporaryDirectory(dir=temporary_root)
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        files = {}
        for name, data in (("code", bytes(range(32))), ("exheader", b"synthetic-header")):
            (self.root / name).write_bytes(data)
            files[name] = {"path": name, "size": len(data), "sha256": hashlib.sha256(data).hexdigest()}
        self.profile = {"schema_version": 1, "provenance": "Generated synthetic bytes, not game data", "files": files,
                        "architecture": "ARMv6K", "instruction_set": "ARM", "entry_point": 4096,
                        "segments": [{"name": "text", "address": 4096, "size": 16, "offset": 0},
                                     {"name": "rodata", "address": 8192, "size": 8, "offset": 16},
                                     {"name": "data", "address": 12288, "size": 8, "offset": 24},
                                     {"name": "bss", "address": 16384, "size": 16}]}

    def invalid(self, mutate, message):
        profile = copy.deepcopy(self.profile)
        mutate(profile)
        with self.assertRaisesRegex(MODULE.ProfileError, message):
            MODULE.verify(profile, self.root)

    def test_valid(self):
        self.assertEqual(MODULE.verify(self.profile, self.root)["status"], "consistent")

    def test_hash(self):
        self.invalid(lambda p: p["files"]["code"].update(sha256="0" * 64), "SHA-256 mismatch")

    def test_size(self):
        self.invalid(lambda p: p["files"]["code"].update(size=31), "size mismatch")

    def test_escape(self):
        self.invalid(lambda p: p["files"]["code"].update(path=str(self.root / "code")), "relative")
        with tempfile.NamedTemporaryFile(dir=self.root.parent) as outside:
            self.invalid(lambda p: p["files"]["code"].update(path="../" + Path(outside.name).name), "escapes")

    def test_memory_overlap(self):
        self.invalid(lambda p: p["segments"][1].update(address=4100), "memory overlap")

    def test_file_overlap(self):
        self.invalid(lambda p: p["segments"][1].update(offset=4), "file overlap")

    def test_out_of_file(self):
        self.invalid(lambda p: p["segments"][2].update(size=9), "outside code")

    def test_entry(self):
        self.invalid(lambda p: p.update(entry_point=8192), "lie in text")
        self.invalid(lambda p: p.update(entry_point=4097), "alignment")

    def test_bss_offset(self):
        self.invalid(lambda p: p["segments"][3].update(offset=32), "bss")

    def test_duplicate_segment(self):
        self.invalid(lambda p: p["segments"][3].update(name="text"), "duplicate")

    def test_overflow(self):
        self.invalid(lambda p: p["segments"][3].update(address=2**32 - 1), "32-bit")

    def test_boolean_size(self):
        self.invalid(lambda p: p["files"]["code"].update(size=True), "integer")

    def test_missing_provenance(self):
        self.invalid(lambda p: p.update(provenance=""), "provenance")

    def test_schema(self):
        self.invalid(lambda p: p.update(schema_version=True), "schema_version")

    def test_cli(self):
        profile_path = self.root / "profile.json"
        profile_path.write_text(json.dumps(self.profile), encoding="utf-8")
        command = [sys.executable, str(Path(MODULE.__file__)), str(profile_path), "--root", str(self.root)]
        success = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(success.returncode, 0, success.stderr)
        self.assertEqual(json.loads(success.stdout)["files_checked"], 2)
        profile_path.write_text("[]", encoding="utf-8")
        failure = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(failure.returncode, 1)
        self.assertIn("profile must be an object", failure.stderr)

    def test_missing_input(self):
        (self.root / "code").unlink()
        with self.assertRaises(FileNotFoundError):
            MODULE.verify(self.profile, self.root)

    def test_architecture(self):
        self.invalid(lambda p: p.update(architecture="ARMv7"), "ARMv6K")

    def test_distinct_files(self):
        self.invalid(lambda p: p["files"].update(exheader=p["files"]["code"]), "distinct")

    def test_malformed_types(self):
        self.invalid(lambda p: p.update(instruction_set=[]), "instruction_set")
        self.invalid(lambda p: p["segments"][0].update(name=[]), "segment name")

    def test_negative(self):
        self.invalid(lambda p: p["segments"][0].update(address=-1), "nonnegative")


if __name__ == "__main__":
    unittest.main()
