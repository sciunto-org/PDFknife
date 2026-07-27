import argparse

from PDFknife import __version__, find_available_engine, setup_logging
from PDFknife import split


def main():
    parser = argparse.ArgumentParser(
        description='Split a multi-page PDF into separate single-page PDFs',
        epilog='Uses gs. Each page becomes its own file.')
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-d', '--debug', action='store_true',
                        default=False, help='enable debug logging')
    parser.add_argument('pdf', metavar='PDF', help='input PDF file(s)', nargs='+')
    parser.add_argument('-o', help='output pattern (default: split-<n>-<input>)',
                        required=False, default=None)
    args = parser.parse_args()

    logger = setup_logging(args.debug)
    logger.debug(f'Script arguments: {args}')

    available_engines = find_available_engine(engines=('gs',))
    logger.debug(f'Available engine: {available_engines}')
    for f in args.pdf:
        split(f, output=args.o)
