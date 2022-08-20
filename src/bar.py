import logging

from .foo import foo

logger = logging.getLogger(__name__)


def bar():
    logger.info("from Bar")
    foo()
    print(f"this is bar ")


if __name__ == "__main__":
    bar()
