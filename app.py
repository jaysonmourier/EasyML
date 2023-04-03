import easyml
import argparse
from art import text2art

def load_script(filepath: str):
    easyml.log.info("Initialization...")
    statebuilder = easyml.ContextBuilder(filepath=filepath)

def home():
    ascii_art = text2art("EasyML")
    print(ascii_art)
    print("Simplify your machine learning journey with EasyML!")
    print("\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='Input file name')
    args = parser.parse_args()

    if not args.file:
        easyml.log.fatal(1, "Please specify a file name")

    filepath: str = args.file

    home()

    # load dataset
    load_script(filepath=filepath)

    # OK
    print('OK')