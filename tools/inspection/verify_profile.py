"""Validate an explicitly supplied local executable profile without publishing inputs.

This checks representation consistency, not title identity, revision, encryption,
compression, instruction semantics, or provenance authenticity.
"""
import argparse
import hashlib
import json
from pathlib import Path


class ProfileError(ValueError):
    pass


def integer(value, label):
    if type(value) is not int or value < 0:
        raise ProfileError(f"{label}: expected a nonnegative integer")
    return value


def verify(profile, root):
    if not isinstance(profile, dict):
        raise ProfileError("profile must be an object")
    root = Path(root).resolve(strict=True)
    if not root.is_dir():
        raise ProfileError("root must be a directory")
    if type(profile.get("schema_version")) is not int or profile["schema_version"] != 1:
        raise ProfileError("unsupported schema_version")
    if not isinstance(profile.get("provenance"), str) or not profile["provenance"].strip():
        raise ProfileError("provenance is required")
    files = profile.get("files")
    if not isinstance(files, dict) or set(files) != {"code", "exheader"}:
        raise ProfileError("files must contain code and exheader")
    sizes = {}
    paths = set()
    for name, record in files.items():
        if not isinstance(record, dict) or not isinstance(record.get("path"), str):
            raise ProfileError(f"{name}: invalid file record")
        relative = Path(record["path"])
        if relative.is_absolute():
            raise ProfileError(f"{name}: path must be relative")
        path = (root / relative).resolve(strict=True)
        if not path.is_relative_to(root) or not path.is_file():
            raise ProfileError(f"{name}: path escapes root or is not a file")
        if path in paths:
            raise ProfileError("code and exheader must be distinct files")
        paths.add(path)
        size = integer(record.get("size"), f"{name}.size")
        if path.stat().st_size != size:
            raise ProfileError(f"{name}: size mismatch")
        digest = record.get("sha256")
        if not isinstance(digest, str) or len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
            raise ProfileError(f"{name}: invalid SHA-256")
        with path.open("rb") as stream:
            actual = hashlib.file_digest(stream, "sha256").hexdigest()
        if digest != actual:
            raise ProfileError(f"{name}: SHA-256 mismatch")
        sizes[name] = size
    segments = profile.get("segments")
    if not isinstance(segments, list) or len(segments) != 4:
        raise ProfileError("exactly text, rodata, data, bss segments required")
    memory = []
    storage = []
    names = set()
    for segment in segments:
        if not isinstance(segment, dict):
            raise ProfileError("invalid segment")
        name = segment.get("name")
        if not isinstance(name, str) or name not in {"text", "rodata", "data", "bss"} or name in names:
            raise ProfileError("invalid or duplicate segment name")
        names.add(name)
        address = integer(segment.get("address"), f"{name}.address")
        size = integer(segment.get("size"), f"{name}.size")
        if address + size > 2**32:
            raise ProfileError(f"{name}: outside 32-bit address space")
        memory.append((address, address + size, name))
        if name == "bss":
            if "offset" in segment:
                raise ProfileError("bss must not have a file offset")
        else:
            offset = integer(segment.get("offset"), f"{name}.offset")
            if offset + size > sizes["code"]:
                raise ProfileError(f"{name}: outside code file")
            storage.append((offset, offset + size, name))
    for ranges, label in ((memory, "memory"), (storage, "file")):
        nonempty = sorted(item for item in ranges if item[0] != item[1])
        for previous, current in zip(nonempty, nonempty[1:]):
            if current[0] < previous[1]:
                raise ProfileError(f"{label} overlap: {previous[2]} / {current[2]}")
    entry = integer(profile.get("entry_point"), "entry_point")
    text = next(s for s in segments if s["name"] == "text")
    if not text["address"] <= entry < text["address"] + text["size"]:
        raise ProfileError("entry_point must lie in text")
    if not isinstance(profile.get("instruction_set"), str) or profile["instruction_set"] not in {"ARM", "Thumb"}:
        raise ProfileError("instruction_set must be ARM or Thumb")
    alignment = 4 if profile["instruction_set"] == "ARM" else 2
    if entry % alignment:
        raise ProfileError("entry_point alignment mismatch; use an untagged address")
    if profile.get("architecture") != "ARMv6K":
        raise ProfileError("architecture must explicitly be ARMv6K")
    return {"status": "consistent", "files_checked": 2, "segments_checked": 4,
            "limitations": "Identity, revision, representation and semantics require independent evidence."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile", type=Path)
    parser.add_argument("--root", type=Path, required=True)
    args = parser.parse_args()
    try:
        profile = json.loads(args.profile.read_text(encoding="utf-8"))
        if not isinstance(profile, dict):
            raise ProfileError("profile must be an object")
        result = verify(profile, args.root)
    except (OSError, ValueError, TypeError) as error:
        parser.exit(1, f"Validation failed: {error}\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
