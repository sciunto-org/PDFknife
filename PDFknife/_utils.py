import logging
import os.path


def default_output(prefix, filepath):
    """
    Return a default path.

    Ex:
    '/tmp/toto/foo.pdf' with 'PREFIX'
    becomes
    '/tmp/toto/PREFIX-foo.pdf'
    """

    directory, name = os.path.split(filepath)
    name = prefix + '-' + name
    return os.path.join(directory, name)


def setup_logging(debug=False):
    level = logging.DEBUG if debug else logging.INFO
    logger = logging.getLogger()
    logger.setLevel(level)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setLevel(level)
        logger.addHandler(handler)
    return logger
