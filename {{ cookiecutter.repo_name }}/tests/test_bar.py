"""Unittesting for foo."""

import unittest

from src.bar import bar


class TestBar(unittest.TestCase):
    def test_bar_case_1(self):
        bar_return = bar()
        self.assertIsNone(bar_return, "Bar should return None")


if __name__ == "__main__":
    unittest.main()
