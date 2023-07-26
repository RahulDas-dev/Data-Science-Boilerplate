import os

from .foo import foo


def bar():
    foo()
    print(f"this is bar ")


if __name__ == "__main__":
    bar()
