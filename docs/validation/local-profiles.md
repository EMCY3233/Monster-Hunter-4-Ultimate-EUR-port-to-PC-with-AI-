# Local executable profile consistency

Status: experimental local inspection format. This is not a regional runtime
contract and does not adopt or supersede any pending STT profile proposal.

Run with Python 3.11 or newer:

```
python tools/inspection/verify_profile.py /path/outside/repository/profile.json --root /path/outside/repository/inputs
python -m unittest discover -s tests -v
cmake -S . -B build
ctest --test-dir build -C Debug --output-on-failure
```

Profiles remain private. Schema version 1 requires `provenance` (nonempty string),
`architecture` (`ARMv6K`), `instruction_set` (`ARM` or `Thumb`), an untagged integer
`entry_point`, and `files` containing exactly `code` and `exheader`. Each file has
a root-relative `path`, integer byte `size`, and lowercase `sha256`.
`segments` contains exactly `text`, `rodata`, `data`, `bss`; each has integer
`address` and `size`. File-backed segments also have integer `offset` into code.
BSS has no offset. Addresses and sizes are bytes; JSON uses decimal integers.
Tests generate entirely synthetic files and serve as an executable schema example.

The validator checks file hashes/sizes, containment (including resolved symlinks),
distinct files, segment extents, non-overlap, 32-bit bounds and entry alignment.
It does not parse an exheader or prove that the two files belong together. A valid
profile proves internal consistency only. Identity, revision, decryption,
decompression, exheader correspondence, entry-point authenticity and instruction
semantics need independent evidence. It assumes files remain unchanged during
validation; use isolated immutable copies, not attacker-controlled live folders.

The initial build has no native target. `src/` and `include/` will be introduced
when reviewed original native integration code exists. No placeholder runtime or
new general recompiler is supplied.
