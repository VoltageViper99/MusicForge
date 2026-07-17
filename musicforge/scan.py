from pathlib import Path


AUDIO_TYPES = {
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




def scan_library(path: Path):

    artists = count_artists(path)
    albums = count_albums(path)
    audio = count_audio_types(path)
    cue_files = count_cue_files(path)
    empty_albums = count_empty_albums(path)
   

    print(f"Artists found: {artists}")
    print()
    print(f"Albums found: {albums}")
    print()
    print(f"Cue files found: {cue_files}")
    print()
    print(f"Empty albums found: {empty_albums}")

    print()
    print("Audio file types:")
    for ext, count in audio.items():
        print(f"  {ext}: {count}")
                         



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

    for ext in AUDIO_TYPES:
        AUDIO_TYPES[ext] = 0

    for file in path.rglob("*"):
        if file.is_file():
            suffix = file.suffix.lower()

            if suffix in AUDIO_TYPES:
                AUDIO_TYPES[suffix] += 1

    return AUDIO_TYPES



def count_cue_files(path: Path) -> int:
    cue_count = 0

    for file in path.rglob("*.cue"):
        cue_count += 1

    return cue_count

def image_exists(path: Path) -> bool:
    for file in path.iterdir():
        if file.is_file() and file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
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

IMAGE_TYPES = {".jpg", ".jpeg", ".png", ".webp"}

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







