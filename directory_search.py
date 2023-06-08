import argparse

def main(directory):
    print(directory)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=str, default='.', help="the directory to search")
    args = parser.parse_args()
    main(args.directory)