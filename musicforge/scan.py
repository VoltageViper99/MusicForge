from pathlib import Path

audio_types = {
    ".flac": 0,
    ".ape": 0,
    ".wv": 0,
    ".wav": 0,
    ".alac": 0,
    ".m4a": 0,
    ".mp3": 0,
    ".ogg": 0,
    ".opus": 0,
    ".aac": 0,
    ".dsf": 0,
    ".dff": 0,
}


def scan_library(path: Path) -> None:
    print(f"Scanning {path}")

    artist_count = 0
    album_count = 0

    for artist in path.iterdir():
        if artist.is_dir():
            artist_count += 1

            for album in artist.iterdir():
                if album.is_dir():
                    album_count += 1

                    for file in album.iterdir():
                        if file.is_file() and file.suffix.lower() in audio_types:
                            audio_types[file.suffix.lower()] += 1
    
         

    print(f"Artists found: {artist_count}")
    print(f"Albums found: {album_count}")
    print("Audio file types found:")
    for ext, count in audio_types.items():
        print(f"  {ext}: {count}")