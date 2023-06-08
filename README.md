[![Python 3.8.7](https://img.shields.io/badge/python-3.8.7-green.svg)](https://www.python.org/downloads/release/python-387/)
# Directory Search

This script searches a directory and its subdirectories and creates a list of the files and a count of all the occurences greater than or equal to 2.

# Approach
1. Use os.walk to crawl all files in directory - store every filename in a list
2. Count all the occurances of the files - store in dictionary {filename: count, ...}
3. Filter out any occurances less than 2
4. Sort in descending order - returns Tuple
5. Display result in below format:
```
__init__.py 404
main.py 101
README.md 25
```

## Running the script
To run the script, execute the script with `directory` argument.

`python directory_search.py --directory ~/mydirectory/`

*The script will default to the current directory if no directory is specified.*