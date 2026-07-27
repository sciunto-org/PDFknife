import argparse
import logging

from PDFknife import __version__
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

    if args.debug:
        llevel = logging.DEBUG
    else:
        llevel = logging.INFO
    logger = logging.getLogger()
    logger.setLevel(llevel)

    steam_handler = logging.StreamHandler()
    steam_handler.setLevel(llevel)
    logger.addHandler(steam_handler)

    logger.debug(f'Script arguments: {args}')

    tearpages(args.pdf, first=args.first, last=args.last)
