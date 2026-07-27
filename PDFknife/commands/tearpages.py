import argparse

from PDFknife import __version__, setup_logging
from PDFknife import tearpages


def main():
    parser = argparse.ArgumentParser(
        description='Remove the first and/or last page of a PDF',
        epilog='Useful to strip blank pages from scanned documents.')
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-d', '--debug', action='store_true',
                        default=False, help='enable debug logging')
    parser.add_argument('pdf', metavar='PDF', help='input PDF file')
    parser.add_argument('--first', action='store_true',
                        default=False, help='remove the first page')
    parser.add_argument('--last', action='store_true',
                        default=False, help='remove the last page')
    args = parser.parse_args()

    logger = setup_logging(args.debug)
    logger.debug(f'Script arguments: {args}')

    tearpages(args.pdf, first=args.first, last=args.last)
