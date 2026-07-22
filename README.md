# Library Sentinel

Library Sentinel is an early-stage Python toolkit for inspecting and maintaining
large, folder-based music libraries. The current release provides a read-only
scanner that summarizes the contents of a library; repair and organization
features are planned for later releases.

## Current functionality

The scanner recursively inspects a music directory and reports:

- Artist directories at the root of the library
- Directories found beneath the library root
- `.cue` files
- Audio-file totals grouped by format

Supported audio extensions are:

```text
.flac  .ape  .wv   .wav  .alac  .m4a  .mp3
.ogg   .opus .aac  .dsf  .dff
```

Scanning is read-only. Library Sentinel does not rename, move, edit, or delete
music files.

## Requirements

- Python 3
- A local or mounted music library that the current user can read

The scanner currently uses only the Python standard library, so no third-party
packages need to be installed.

## Getting started

Clone the repository:

```bash
git clone <repository-url> library-sentinel
cd library-sentinel
```

Set the library path in `musicforge/main.py`:

```python
library = Path("/path/to/your/music")
```

Run the scanner from the repository root:

```bash
python3 -m musicforge.main
```

Example output:

```text
Artists found: 125

Albums found: 734

Cue files found: 42

Audio file types:
  .flac: 8120
  .ape: 6
  .wv: 0
  ...
```

> [!NOTE]
> The displayed album total currently counts every directory below the library
> root, including nested directories. It does not yet validate whether each
> directory represents an album.

## Configuration

The repository includes a `config.toml` that sketches the intended settings for
the library, backups, logging, splitting, cue lookup, and validation. The
application does not load this file yet; the active library path remains the
value defined in `musicforge/main.py`.

## Project structure

```text
.
├── config.toml
├── musicforge/
│   ├── __init__.py
│   ├── main.py
│   └── scan.py
└── README.md
```

The Python package still uses the original `musicforge` name internally, even
though the project is now called Library Sentinel.

## Roadmap

Development is organized into phased milestones covering:

- A configurable and testable scanner
- Exportable reports and cue-sheet auditing
- Library health and metadata validation
- Duplicate detection
- Safe album splitting
- Previewable repair and backup workflows

See [ROADMAP.md](ROADMAP.md) for planned releases, feature checklists, and
completion criteria. Roadmap items describe the intended direction of the
project and are not part of the current scanner unless stated otherwise.

## Development status

Library Sentinel is experimental and under active development. Test changes
against a copy of your library before using future write-enabled features, and
keep an independent backup of all media and metadata.
