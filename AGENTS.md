# Collaboration

Use an independent branch and a reviewed pull request. Do not merge automatically.
Check main and active owners before editing. Do not alter STT or another owner's
branch, original game files, active REA installations, or PS Vita resources.

Only original project code and explicitly reviewed, license-compatible external
code may enter this repository. Record source commit, license, attribution and
review before importing code. No external implementation is vendored initially.
Do not infer permission to redistribute code from a public repository's visibility.

Keep commercial inputs, keys, resources, derived native code and private reports
outside the checkout. Ignore rules are defense in depth, not publication review.
Review the explicit file list and diff before every push.

Run `python -m unittest discover -s tests -v` for profile tooling changes.
When CMake is available, configure and run CTest as used by CI. Report what was
actually run; synthetic tests do not demonstrate a real game function or menu.
Track owner, branch, commit, tests, dependencies, blockers and next action.
Use completed / in progress / pending / blocked / experimental states with evidence.
Do not aggregate overlapping campaigns into global coverage or a playable port.
