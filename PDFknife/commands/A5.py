import argparse
import logging

from PDFknife import __version__, find_available_engine
from PDFknife import A5


def main():
    parser = argparse.ArgumentParser(
        description='Arrange two A5 pages side by side on A4 paper',
        epilog='Uses pdfjam. Intended for booklets printed on A5.')
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-d', '--debug', action='store_true',
                        default=False, help='enable debug logging')
    parser.add_argument('pdf', metavar='PDF', help='input PDF file')
    parser.add_argument('-o', help='output PDF file (default: A5-<input>)',
                        required=False, default=None)
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

    available_engines = find_available_engine(engines=('pdfjam',))
    logger.debug(f'Available engine: {available_engines}')

    A5(args.pdf, output=args.o, engine=available_engines[0])
