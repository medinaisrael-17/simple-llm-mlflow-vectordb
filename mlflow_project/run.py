# run.py
import argparse
from src.pipeline import SimplePipeline

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--question",nargs="+", type=str, required=True)
    args = parser.parse_args()

    question = " ".join(args.question)

    pipe = SimplePipeline()
    pipe.add_docs([
        "The Eiffel Tower is in Paris.",
        "The Colosseum is in Rome.",
        "The Statue of Liberty is in New York."
    ])
    print(pipe.query(question))