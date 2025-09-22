# run.py
import argparse
from src.pipeline import SimplePipeline

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--question", type=str, required=True)
    args = parser.parse_args()

    pipe = SimplePipeline()
    pipe.add_docs([
        "The Eiffel Tower is in Paris.",
        "The Colosseum is in Rome.",
        "The Statue of Liberty is in New York."
    ])
    print(pipe.query(args.question))