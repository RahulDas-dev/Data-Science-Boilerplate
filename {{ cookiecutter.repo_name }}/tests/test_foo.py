"""Unittesting for foo."""

import unittest

from src.foo import foo


def setUpModule():
    print(f"Module {__name__} Testing start")


def tearDownModule():
    print(f"Module {__name__} Testing Complete")


class TestFoo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("TestFoo Setup")

    @classmethod
    def tearDownClass(cls):
        print("TestFoo tearDown")

    def test_foo_case_1(self):
        foo_return = foo()
        self.assertIsNone(foo_return, "Foo should return None")


if __name__ == "__main__":
    unittest.main()
