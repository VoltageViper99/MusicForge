from pathlib import Path

from scan import scan_library


def main():
    library = Path("/mnt/mediaserver/Music")
    scan_library(library)


if __name__ == "__main__":
    main()