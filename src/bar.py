import logging
import os

from .foo import foo

logger = logging.getLogger(__name__)


def bar():
    logger.info("Hi this is BAR")
    foo()
    print(f"this is bar ")


if __name__ == "__main__":
    bar()
