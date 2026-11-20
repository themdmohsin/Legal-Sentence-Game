import argparse
import sys

from .corpus import HOLDOUT, TRAIN
from .game import play
from .ngram import Predictor


def main():
    parser = argparse.ArgumentParser(description="Legal Sentence Game")
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("hello")
    game = sub.add_parser("play")
    game.add_argument("--rounds", type=int, choices=range(1, 6), default=3)
    game.add_argument("--seed", type=int)
    sub.add_parser("demo")
    sub.add_parser("evaluate")
    sub.add_parser("classify").add_argument("sentence")
    args = parser.parse_args()
    if args.command == "hello":
        print("Legal Sentence Game | Run python -m app.cli play")
        return
    from .classifier import Classifier
    try:
        model = Classifier()
        if args.command == "classify":
            label, score = model.predict(args.sentence)
            print(f"{label} | model score {score:.1%}")
        elif args.command == "evaluate":
            correct = total = 0
            for expected, sentences in HOLDOUT.items():
                for sentence in sentences:
                    actual, _ = model.predict(sentence)
                    total += 1
                    correct += actual == expected
                    print(f"{expected:20} {actual:20} {sentence}")
            print(f"Held-out accuracy: {correct}/{total}")
        elif args.command == "demo":
            predictor = Predictor(s for group in TRAIN.values() for s in group)
            print("Draft: The customer shall")
            print("Suggestions:", ", ".join(predictor.hints("The customer shall")))
            sentence = "The customer shall settle the invoice within fifteen days."
            print(sentence)
            print("Model reading:", model.predict(sentence)[0])
        else:
            play(model, getattr(args, "rounds", 3), getattr(args, "seed", None))
    except (EOFError, KeyboardInterrupt):
        print("\nSession ended.")
    except (ValueError, OSError) as exc:
        sys.exit(f"Could not complete the request: {exc}")


if __name__ == "__main__":
    main()

