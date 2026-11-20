import re
from collections import Counter, defaultdict


def words(text):
    return re.findall(r"[a-z]+(?:'[a-z]+)?|[0-9]+", text.lower())


class Predictor:
    def __init__(self, sentences):
        self.counts = defaultdict(Counter)
        for sentence in sentences:
            history = ["<s>", "<s>"]
            for word in words(sentence):
                for width in (2, 1):
                    self.counts[tuple(history[-width:])][word] += 1
                self.counts[()][word] += 1
                history.append(word)

    def hints(self, text, limit=3):
        history = ["<s>", "<s>", *words(text)]
        for key in (tuple(history[-2:]), tuple(history[-1:]), ()):
            counts = self.counts.get(key)
            if counts:
                return sorted(counts, key=lambda word: (-counts[word], word))[:limit]
        return []

