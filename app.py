import easyml
import argparse
from art import text2art

def load_script(filepath: str):
    easyml.log.info("Initialization...")
    return easyml.contextbuilder(filepath=filepath)

def home():
    ascii_art = text2art("EasyML")
    print(ascii_art)
    print("Simplify your machine learning journey with EasyML!")
    print("\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='Input file name')
    parser.add_argument('-o', '--output', help='Output file name')
    args = parser.parse_args()

    if not args.file:
        easyml.log.fatal(1, "Please specify a file name")

    filepath: str = args.file

    home()

    # load dataset
    state = load_script(filepath=filepath)
    state.export_model("outputs/" + args.output if args.output is not None else "model.save")
