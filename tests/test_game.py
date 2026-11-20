import unittest
from unittest.mock import patch
import io
from contextlib import redirect_stdout
from app.corpus import TRAIN, HOLDOUT
from app.ngram import Predictor
from app.game import draft, play
from app.classifier import Classifier


class GameTests(unittest.TestCase):
    def test_rank_and_backoff(self):
        model = Predictor(["shall pay rent", "shall pay fees", "shall disclose fees"])
        self.assertEqual(model.hints("unknown shall"), ["pay", "disclose"])
        self.assertEqual(model.hints("SHALL pay,"), ["fees", "rent"])

    def test_draft(self):
        model = Predictor(["buyer shall pay fees"])
        entries = iter(["/done", "1", "/undo", "settle all invoices", "/done"])
        self.assertEqual(draft("buyer shall", model, lambda _: next(entries), lambda _: None),
                         "buyer shall settle all invoices.")

    def test_data_split(self):
        self.assertTrue(set(sum(TRAIN.values(), [])).isdisjoint(sum(HOLDOUT.values(), [])))

    def test_model_and_score(self):
        model = Classifier()
        self.assertEqual(model.predict("The buyer must pay the outstanding invoice.")[0], "payment")
        with patch("app.game.draft", return_value="The buyer must pay the outstanding invoice."), redirect_stdout(io.StringIO()) as output:
            play(model, 5, 42)
        self.assertIn("Final score: 1/5", output.getvalue())

    def test_invalid_clause(self):
        with self.assertRaises(ValueError):
            Classifier().predict(" ")

