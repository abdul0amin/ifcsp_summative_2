#Unit tests for pure functions in quiz_logic.py.
#Python's unittest framework.

import unittest
from quiz_logic import (
    clean_name,
    is_name_not_empty,
    is_valid_length,
    contains_only_letters,
    check_answer,
)


class TestQuizLogic(unittest.TestCase):
    #Tests for quiz validation and answer logic.

    def test_clean_name(self):
        self.assertEqual(clean_name("  abdul  "), "Abdul")

    def test_is_name_not_empty(self):
        self.assertTrue(is_name_not_empty("Abdul"))
        self.assertFalse(is_name_not_empty(""))

    def test_valid_length(self):
        self.assertTrue(is_valid_length("Abdul"))
        self.assertFalse(is_valid_length("A"))

    def test_contains_only_letters(self):
        self.assertTrue(contains_only_letters("Abdul Amin"))
        self.assertFalse(contains_only_letters("Abdul123"))

    def test_check_answer(self):
        self.assertTrue(check_answer("1", "1"))
        self.assertFalse(check_answer("2", "1"))


if __name__ == "__main__":
    unittest.main()
