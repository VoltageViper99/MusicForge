from pathlib import Path

from .scan import scan_library
from .health import library_health


def main():
    library = Path("/mnt/mediaserver/Music")

    stats = scan_library(library)

    print(f"Artists found: {stats['artists']}")
    print(f"Albums found: {stats['albums']}")
    print(f"Cue files found: {stats['cue_files']}")
    print(f"Empty albums found: {stats['empty_albums']}")

    print("\nAudio file types:")
    for ext, count in stats["audio_types"].items():
        print(f"  {ext}: {count}")

    health_stats = library_health(library)

    print(f"Missing Artwork: {health_stats['missing_artwork']['total']}")
   

if __name__ == "__main__":
    main()