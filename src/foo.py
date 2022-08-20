import logging

logger = logging.getLogger(__name__)


def foo():
    logger.info("from Foo")
    print("this is foo")
