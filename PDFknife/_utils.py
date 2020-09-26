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
