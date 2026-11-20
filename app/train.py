"""Fit GPT-2's final normalization and a five-class softmax head."""
import numpy as np
from .base import GPT2, softmax
from .classifier import CHECKPOINT, features
from .corpus import TRAIN


def main():
    base = GPT2()
    labels = list(TRAIN)
    x = np.stack([features(base, text) for label in labels for text in TRAIN[label]])
    y = np.repeat(np.arange(len(labels)), [len(TRAIN[label]) for label in labels])
    gamma = base.w["ln_f.weight"].copy()
    beta = base.w["ln_f.bias"].copy()
    original = x * gamma + beta
    center = original.mean(0)
    spread = np.maximum(original.std(0), 0.08)
    head = np.zeros((768, len(labels)), dtype="f")
    bias = np.zeros(len(labels), dtype="f")
    for _ in range(400):
        z = (x * gamma + beta - center) / spread
        error = softmax(z @ head + bias)
        error[np.arange(len(y)), y] -= 1
        error /= len(y)
        gradient = (error @ head.T) / spread
        gamma -= .005 * (x * gradient).sum(0)
        beta -= .005 * gradient.sum(0)
        head -= .025 * (z.T @ error + .01 * head)
        bias -= .025 * error.sum(0)
    np.savez_compressed(CHECKPOINT, labels=labels, gamma=gamma, beta=beta,
                        head=head, bias=bias, center=center, spread=spread)


if __name__ == "__main__":
    main()

