# Library Sentinel Roadmap

Library Sentinel is being developed as a safe, modular toolkit for auditing and
maintaining large music libraries. The project will remain read-only by default;
features that modify a library must support previews and backups before they can
be considered stable.

This roadmap describes direction rather than fixed release dates. Priorities may
change as the scanner encounters real-world library layouts and file formats.

## Guiding principles

- Never modify a library during a scan.
- Provide a dry-run preview for every write operation.
- Require explicit confirmation before destructive actions.
- Preserve metadata and source files unless deletion is explicitly requested.
- Produce clear reports that explain every detected issue and proposed change.
- Keep scanners and checks independently usable and testable.

## v0.3 — Configurable scanner

Turn the current proof-of-concept scanner into a reliable command-line tool.

- [ ] Load the library path and scanner settings from `config.toml`
- [ ] Allow the library path to be supplied as a command-line argument
- [ ] Validate that the selected path exists and is readable
- [ ] Replace global audio counters with per-scan state
- [ ] Distinguish artist, album, disc, and miscellaneous directories
- [ ] Detect empty directories
- [ ] Handle inaccessible files and directories without terminating the scan
- [ ] Add concise and detailed output modes
- [ ] Return meaningful process exit codes
- [ ] Add automated tests for scanner behavior

Completion criteria:

- A user can scan any chosen library without editing source code.
- Repeated scans produce independent and consistent results.
- Invalid paths and permission errors produce useful messages.

## v0.4 — Reports and Cue Hunter

Make scan results actionable and expand cue-sheet auditing.

- [ ] Export reports as JSON
- [ ] Export human-readable reports as text or Markdown
- [ ] Find single-file albums that do not have a cue sheet
- [ ] Detect cue sheets that reference missing audio files
- [ ] Detect audio files referenced by multiple cue sheets
- [ ] Validate cue-sheet syntax and track boundaries
- [ ] Report unsupported audio extensions separately
- [ ] Add filtering by artist, format, or issue type

Completion criteria:

- Scan results can be saved and compared outside the application.
- Cue Hunter identifies missing, broken, and ambiguous cue-sheet relationships
  without changing any files.

## v0.5 — Library Doctor

Add deeper, read-only health and metadata checks.

- [ ] Verify FLAC files using an available integrity-checking backend
- [ ] Detect missing or unreadable artwork
- [ ] Validate required tags such as artist, album, title, and track number
- [ ] Detect inconsistent album-level metadata
- [ ] Find invalid or conflicting disc and track numbers
- [ ] Identify files whose extension does not match their detected format
- [ ] Group issues by severity
- [ ] Recommend a resolution for each supported issue

Completion criteria:

- Health checks identify corrupt or inconsistent files without producing false
  claims that a file was repaired.
- Reports clearly separate errors, warnings, and informational findings.

## v0.6 — Duplicate Finder

Identify likely duplicate tracks and releases without relying on filenames alone.

- [ ] Detect exact file duplicates using cryptographic hashes
- [ ] Detect matching audio with different metadata or containers
- [ ] Group likely duplicate albums
- [ ] Explain why each pair or group was classified as a duplicate
- [ ] Allow known duplicates to be ignored in future reports
- [ ] Export duplicate groups for manual review

Completion criteria:

- Exact and probable duplicates are reported separately.
- No duplicate is automatically deleted or replaced.

## v0.7 — Splitter

Safely split single-file albums using verified cue sheets.

- [ ] Detect an available supported audio-splitting backend
- [ ] Preview output filenames, formats, and metadata
- [ ] Split into a staging directory instead of the source directory
- [ ] Transfer album and track metadata to generated files
- [ ] Preserve or copy album artwork
- [ ] Verify the generated tracks before reporting success
- [ ] Keep original files by default
- [ ] Honor the `splitter.delete_original` setting only with explicit confirmation
- [ ] Record a machine-readable operation log

Completion criteria:

- A supported album can be split reproducibly into a staging directory.
- The original audio and cue sheet remain untouched by default.
- Partial failures leave enough information to diagnose or safely retry the job.

## v0.8 — Repair workflows and backups

Introduce controlled library changes after the audit tools are mature.

- [ ] Create a backup manifest before modifying files
- [ ] Back up affected metadata and small supporting files
- [ ] Support dry-run and interactive confirmation modes
- [ ] Remove confirmed empty directories
- [ ] Apply approved metadata corrections
- [ ] Restore changes from an operation manifest where practical
- [ ] Add structured logs with operation IDs
- [ ] Prevent concurrent write operations against the same library

Completion criteria:

- Every supported modification can be previewed before execution.
- Every operation records what changed, when it changed, and why.
- Recoverable files are backed up before modification.

## v1.0 — Stable release

Deliver a documented and dependable command-line application suitable for
regular library audits.

- [ ] Stabilize the configuration format and command-line interface
- [ ] Package Library Sentinel for standard Python installation
- [ ] Complete end-to-end tests using representative test libraries
- [ ] Document supported platforms, formats, and external tools
- [ ] Publish migration notes for earlier configuration files
- [ ] Provide a security and data-safety review
- [ ] Document backup and recovery procedures

Completion criteria:

- All documented commands have automated coverage.
- Read-only commands are safe to run unattended.
- Write-enabled commands require deliberate opt-in and produce auditable logs.
- Installation, configuration, scanning, and recovery are fully documented.

## Future ideas

The following ideas are intentionally outside the initial stable-release scope:

- Acoustic fingerprinting and MusicBrainz integration
- Optional online cue-sheet lookup
- Scheduled or incremental scans
- A local web dashboard
- Notifications for newly detected issues
- Multiple library profiles
- Plugin support for additional validators and repair tools


