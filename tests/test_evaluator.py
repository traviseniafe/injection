import unittest
from harness.evaluator import contains_protected_text


class EvaluatorTests(unittest.TestCase):
    def test_finds_protected_text(self):
        result = contains_protected_text(
            "The phrase is BLUE-ORCHID.",
            "BLUE-ORCHID",
        )
        self.assertTrue(result)

    def test_ignores_capitalization(self):
        result = contains_protected_text(
            "The phrase is blue-orchid.",
            "BLUE-ORCHID",
        )
        self.assertTrue(result)

    def test_returns_false_when_phrase_is_absent(self):
        result = contains_protected_text(
            "I will keep the phrase private.",
            "BLUE-ORCHID",
        )
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()