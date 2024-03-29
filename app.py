from art import text2art
import easyml
import argparse
import time

def load_script(filepath: str):
    easyml.log.info("Initialization...")
    return easyml.ContextBuilder(easyml.grammar, filepath).get_context()

def home():
    ascii_art = text2art("EasyML")
    print(ascii_art)
    print("Simplify your machine learning journey with EasyML!\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='Input file name')
    parser.add_argument('-o', '--output', help='Output file name')
    args = parser.parse_args()
    output_path = f"output/model_{time.time()}.easyml"

    if not args.file:
        easyml.log.fatal(1, "Please specify a file name")

    if args.output:
        output_path = args.output

    filepath: str = args.file

    home()

    # load dataset
    state = load_script(filepath=filepath)
    state.train_model()

    #state.export_model(output_path)

    flask_app = easyml.WebRenderer(state)
    flask_app.run()