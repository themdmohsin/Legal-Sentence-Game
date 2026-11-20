import random

from .corpus import OBJECTIVES, PROMPTS, TRAIN
from .ngram import Predictor, words


def draft(prefix, predictor, read=input, write=print):
    text = prefix
    while True:
        hints = predictor.hints(text)
        write(f"\nDraft: {text}")
        write("Next words: " + "   ".join(f"{i}. {word}" for i, word in enumerate(hints, 1)))
        entry = read("Add words, pick 1-3, or enter /done, /undo, /skip, /quit > ").strip()
        if entry in ("/quit", "/skip"):
            return entry
        if entry == "/done":
            if len(words(text)) > len(words(prefix)):
                return text.rstrip(" .") + "."
            write("Add a completion first.")
        elif entry == "/undo":
            if text != prefix:
                text = text.rsplit(" ", 1)[0]
        elif entry.isdigit():
            if entry in [str(i) for i in range(1, len(hints)+1)]:
                text += " " + hints[int(entry)-1]
            else:
                write("Choose a displayed suggestion.")
        elif words(entry) and not entry.startswith("/"):
            candidate = text + " " + " ".join(entry.split())
            if len(candidate.encode("utf-8")) <= 256:
                text = candidate
            else:
                write("Keep the clause within 256 bytes.")
        else:
            write("Type a continuation or choose a listed command.")


def play(model, rounds, seed):
    predictor = Predictor(s for group in TRAIN.values() for s in group)
    labels = list(PROMPTS)
    random.Random(seed).shuffle(labels)
    points = attempts = 0
    for i, label in enumerate(labels[:rounds], 1):
        print(f"\nROUND {i}/{rounds} | {label.title()}\nObjective: {OBJECTIVES[label]}")
        sentence = draft(PROMPTS[label], predictor)
        if sentence == "/quit":
            break
        attempts += 1
        if sentence == "/skip":
            print("Skipped. Example:", TRAIN[label][0])
            continue
        prediction, score = model.predict(sentence)
        print(f"Model reading: {prediction} ({score:.0%} model score)")
        points += int(prediction == label)
        print("Objective matched." if prediction == label else "Different reading. Revisit the objective above.")
        print("Example:", TRAIN[label][0])
    print(f"\nFinal score: {points}/{attempts} attempted rounds.")

