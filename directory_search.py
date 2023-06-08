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


def _filter_occurrences(string_count_dict: Dict) -> Dict:
    logging.debug(
        "Filtering string_count_dict to only items with a count of greater than or equal to 2"
    )
    filtered_string_count_dict = {}
    # TO DO: Dict Comprehension
    for string, count in string_count_dict.items():
        if count >= 2:
            filtered_string_count_dict[string] = count
    return filtered_string_count_dict


def _sort_by_occurance(filtered_string_count_dict: Dict) -> Dict:
    logging.debug("Sorting filtered string count in descending order")
    sorted_string_count = sorted(
        filtered_string_count_dict.items(),
        key=lambda string_count: string_count[1],
        reverse=True,
    )
    sorted_string_count = dict(
        (string, count) for string, count in sorted_string_count
    )  # Converting back to a dict
    return sorted_string_count


def _display_results(sorted_string_count: Dict) -> None:
    logging.debug("Print results in line delimeted format")
    for string, count in sorted_string_count.items():
        print(string, count)


def main(directory: str) -> None:
    logging.info("Starting Directory Search")
    file_paths = _crawl_directory(directory)
    string_count_dict = _count_occurrences(file_paths)
    filtered_string_count_dict = _filter_occurrences(string_count_dict)
    sorted_string_count = _sort_by_occurance(filtered_string_count_dict)
    _display_results(sorted_string_count)
    logging.info("Directory Search Finished")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--directory", type=str, default=".", help="the directory to search"
    )
    args = parser.parse_args()

    main(args.directory)
