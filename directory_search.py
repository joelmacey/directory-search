import os
import argparse
import logging
from typing import List, Dict

logging.basicConfig(filename=f"{__file__}.log", filemode="w", level=logging.DEBUG)


def _crawl_directory(directory: str) -> List:
    logging.debug("Crawling Directory %s", directory)
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_paths.append(file)
    return file_paths


def _count_occurrences(file_paths: List) -> Dict:
    logging.debug("Counting occurance of each file")
    string_count_dict = {}
    for filename in file_paths:
        string_count_dict[filename] = string_count_dict.get(filename, 0) + 1
    return string_count_dict


def main(directory: str):
    logging.debug("Starting Directory Search")
    file_paths = _crawl_directory(directory)
    string_count_dict = _count_occurrences(file_paths)
    print(string_count_dict)
    logging.debug("Directory Search Finished")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--directory", type=str, default=".", help="the directory to search"
    )
    args = parser.parse_args()

    main(args.directory)
