from pathlib import Path

import numpy as np

from .base import GPT2, softmax

CHECKPOINT = Path(__file__).with_name("clause_model.npz")


def features(base, sentence):
    ids = base.encode(sentence.strip())
    if not 1 <= len(ids) <= 256:
        raise ValueError("Use a clause containing 1 to 256 tokens.")
    return base.normalized_hidden(ids).mean(axis=0)


class Classifier:
    def __init__(self):
        self.base = GPT2()
        with np.load(CHECKPOINT, allow_pickle=False) as saved:
            self.params = dict(saved)

    def predict(self, sentence):
        p = self.params
        pooled = features(self.base, sentence) * p["gamma"] + p["beta"]
        logits = ((pooled - p["center"]) / p["spread"]) @ p["head"] + p["bias"]
        probs = softmax(logits)
        index = int(probs.argmax())
        return str(p["labels"][index]), float(probs[index])

