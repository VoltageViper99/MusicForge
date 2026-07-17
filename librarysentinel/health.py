from pathlib import Path
from .scan import has_no_audio_files, image_exists, has_audio_files
from .constants import AUDIO_TYPES, IMAGE_TYPES


def library_health(path: Path):
    return {
        "missing_artwork": count_missing_artwork(path),
        "folders_without_audio": count_audioless_folders(path),
    }

def count_missing_artwork(path:Path)-> dict:
    """Count artwork files by image extension. Returns dict with totals and breakdown."""
    missing_artwork = 0
    total_artwork = {ext: 0 for ext in IMAGE_TYPES}

    for album in path.rglob("*"):
        if not album.is_dir():
            continue

        if has_audio_files(album) and not image_exists(album):
            missing_artwork += 1

    return {"total": missing_artwork}

def count_audioless_folders(path:Path)-> dict:
    """Count folders that contain no audio files. Returns dict with total and list of folder paths."""
    audioless_count = 0
    total_audioless_folders = []

    for entry in path.rglob("*"):
        if not entry.is_dir():
            continue

        # Check for any audio files directly under this folder (non-recursive)
        has_audio = False
        for child in entry.iterdir():
            if child.is_file() and child.suffix.lower().lstrip('.') in AUDIO_TYPES:
                has_audio = True
                break

        if not has_no_audio_files(entry):
            audioless_count += 1
            total_audioless_folders.append(str(entry))

    return {"total": audioless_count, "folders": total_audioless_folders}