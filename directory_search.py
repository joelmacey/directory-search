import os
import argparse
import logging
from typing import List

logging.basicConfig(filename=f"{__file__}.log", filemode="w", level=logging.DEBUG)


def _crawl_directory(directory: str) -> List:
    logging.debug("Crawling Directory %s", directory)
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_paths.append(file)
    return file_paths


def main(directory: str):
    file_paths = _crawl_directory(directory)
    print(file_paths)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--directory", type=str, default=".", help="the directory to search"
    )
    args = parser.parse_args()
    main(args.directory)
