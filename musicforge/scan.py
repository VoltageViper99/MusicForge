from pathlib import Path


def scan_library(path: Path) -> None:
    print(f"Scanning {path}")

    artist_count = 0

    for artist in path.iterdir():
        if artist.is_dir():
            artist_count += 1

    print(f"Artists found: {artist_count}")