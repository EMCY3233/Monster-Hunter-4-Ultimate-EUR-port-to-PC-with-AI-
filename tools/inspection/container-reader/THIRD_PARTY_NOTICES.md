# Third-party notices

The inspector links statically with unmodified zlib 1.3.2, by Jean-loup Gailly
and Mark Adler. CMake downloads and checks the official source archive; the
upstream source and its LICENSE remain in the build dependency directory.
The inspector's bounded streaming wrapper is project code, not zlib code.

Source: https://zlib.net/fossils/zlib-1.3.2.tar.gz
SHA-256: bb329a0a2cd0274d05519d61c667c062e06990d72e125ee2dfa8de64f0119d16
License source: https://github.com/madler/zlib/blob/v1.3.2/LICENSE

Copyright notice:

 (C) 1995-2026 Jean-loup Gailly and Mark Adler

  This software is provided 'as-is', without any express or implied
  warranty.  In no event will the authors be held liable for any damages
  arising from the use of this software.

  Permission is granted to anyone to use this software for any purpose,
  including commercial applications, and to alter it and redistribute it
  freely, subject to the following restrictions:

  1. The origin of this software must not be misrepresented; you must not
     claim that you wrote the original software. If you use this software
     in a product, an acknowledgment in the product documentation would be
     appreciated but is not required.
  2. Altered source versions must be plainly marked as such, and must not be
     misrepresented as being the original software.
  3. This notice may not be removed or altered from any source distribution.

  Jean-loup Gailly        Mark Adler
  jloup@gzip.org          madler@alumni.caltech.edu

## Scope of this notice and system dependencies

The zlib permission above applies to zlib only. It does not license the
inspector's project code, tests, build files or documentation. Their
attribution and authorization review is recorded in PROVENANCE.md.
No general license is assigned to that code by this notice.

The Linux build links to the system OpenSSL::Crypto implementation.
The reviewed CI used OpenSSL3.0.13. No OpenSSL source or library is vendored
or distributed by this source-only pull request. OpenSSL3.x is distributed
under Apache License2.0; any future distribution of its files must preserve
the applicable upstream license and notices for the actual selected version.
Upstream license reference:
https://github.com/openssl/openssl/blob/openssl-3.0.13/LICENSE.txt

Windows links to BCrypt provided by the Windows SDK/system. SDK and runtime
files are not included in this pull request; this notice does not grant
redistribution rights to those files. Check the applicable terms before
packaging binaries or redistributable dependencies.

CMake, compilers and Python are build/test tools and are not bundled here.
zlib's fixed source and complete upstream LICENSE remain in the build
dependency directory. No game data or game-derived code is included.
