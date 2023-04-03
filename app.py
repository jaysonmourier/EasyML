import easyml
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='Input file name')
    args = parser.parse_args()

    if not args.file:
        easyml.fatal(1, "Please specify a file name")

    print('OK')