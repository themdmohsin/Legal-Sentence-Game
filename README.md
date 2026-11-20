[![Built with askThili](https://msrit.ask.thili.ai/api/v1/public/projects/7vve49et44/badge.svg)](https://msrit.ask.thili.ai/b/7vve49et44)
# Legal Sentence Game

Draft a short contract clause in the terminal. Each round gives a purpose and a partial sentence. Add your own words or use numbered next-word suggestions. Submit the full clause to a trained GPT-2 classifier and compare its reading with the objective.

## Start on Windows

From the extracted source or the cloned repository:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m app.cli demo
.\.venv\Scripts\python.exe -m app.cli play
```

If Python 3.12 is missing, install it with `winget install --exact --id Python.Python.3.12`, then reopen PowerShell. The first demo or game downloads about 550 MB of public GPT-2 weights from Hugging Face. Subsequent runs use the local cache. The fitted classifier parameters are bundled. No API key or training step is required.

## Play

1. Read the round objective and partial clause.
2. Enter a number to append a suggestion, or type a continuation. Use /undo to remove the last word.
3. Enter /done to classify the whole draft. A matching category earns one point. The game shows the predicted category, model score, drafting cue and an example.
4. Use /skip to reveal an example for zero points, or /quit to finish early.

Try `python -m app.cli play --rounds 5 --seed 42` to practice all five categories in a repeatable order. Use `python -m app.cli classify "The buyer must settle the invoice on receipt."` to classify one sentence.

## Models and evidence

The next-word predictor counts adjacent tokens in 40 original fictional clauses. It uses two preceding words, then one, then overall frequency. Suggestions and scoring serve different purposes: a valid free-text completion can earn full credit.

The classifier loads GPT-2 small at revision 607a30d783dfa663caf39e06633721c8d4cfcd7e. Training freezes its transformer blocks, updates its final layer-normalization weights and bias, and learns a five-class linear head over mean-pooled token features. The saved checkpoint is combined with the original weights at runtime.

The model correctly labeled 10/10 separate, hand-written evaluation clauses, two per category. This small exercise measures category recognition on the supplied examples. The displayed softmax score is uncalibrated. A category match scores the drafting exercise and does not assess enforceability.

## Reproduce

```powershell
.\.venv\Scripts\python.exe -m app.cli evaluate
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe -m app.train
```

Corpus, objectives and held-out examples are in app/corpus.py. The predictor is in app/ngram.py. The transformer, fitted classifier and training routine are in app/base.py, app/classifier.py and app/train.py. Game controls and scoring are in app/game.py.

Base checkpoint: https://huggingface.co/gpt2

