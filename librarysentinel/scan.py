from pathlib import Path
from .constants import AUDIO_TYPES, IMAGE_TYPES








def scan_library(path: Path):
    return {
        "artists": count_artists(path),
        "albums": count_albums(path),
        "audio": count_audio_types(path),
        "cue_files": count_cue_files(path),
        "empty_albums": count_empty_albums(path),
        "audio_types": count_audio_types(path),
       

    }
                         



def count_artists(path: Path) -> int:

    artist_count = 0   
    
    for artist in path.iterdir():
        if artist.is_dir():
            artist_count += 1

    return artist_count


def count_albums(path: Path) -> int:

    album_count = 0

    for album in path.rglob("*"):
        if album.is_dir():
            album_count += 1

    return album_count


def count_audio_types(path: Path) -> dict:

    audio_counts = {ext: 0 for ext in AUDIO_TYPES}

    for file in path.rglob("*"):
        if file.is_file():
            suffix = file.suffix.lower()

            if suffix in AUDIO_TYPES:
                audio_counts[suffix] += 1

    return audio_counts



def count_cue_files(path: Path) -> int:
    cue_count = 0

    for file in path.rglob("*.cue"):
        cue_count += 1

    return cue_count

def image_exists(path: Path) -> bool:
    for file in path.iterdir():
        if file.is_file() and file.suffix.lower() in IMAGE_TYPES:
            return True
    return False

def has_no_audio_files(path: Path) -> bool:
    for file in path.iterdir():
        if file.is_file() and file.suffix.lower() in AUDIO_TYPES:
            return False
    return True

def has_audio_files(path: Path) -> list:
    audio_files = []
    for file in path.iterdir():
        if file.is_file() and file.suffix.lower() in AUDIO_TYPES:
            audio_files.append(file)
    return audio_files


def count_empty_albums(path: Path) -> int:
    empty_count = 0

    for album in path.rglob("*"):
        if not album.is_dir():
            continue

        has_image = False
        has_audio = False
        has_cue = False

        for file in album.iterdir():
            if not file.is_file():
                continue

            suffix = file.suffix.lower()

            if suffix in IMAGE_TYPES:
                has_image = True
            elif suffix in AUDIO_TYPES:
                has_audio = True
            elif suffix == ".cue":
                has_cue = True

        if has_image and not has_audio and not has_cue:
            empty_count += 1

    return empty_count







