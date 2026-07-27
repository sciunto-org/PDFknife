import argparse
import logging

from PDFknife import __version__, find_available_engine
from PDFknife import margin


def main():
    parser = argparse.ArgumentParser(
        description='Add a white margin around PDF pages',
        epilog='Uses pdfjam --trim with --clip false to add margin. Default: 10 mm.')
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-d', '--debug', action='store_true',
                        default=False, help='enable debug logging')
    parser.add_argument('pdf', metavar='PDF', help='input PDF file')
    parser.add_argument('-m',
                        default=10,
                        type=float,
                        help='margin width in millimetres (default: 10)')
    parser.add_argument('-o',
                        required=False, default=None,
                        help='output PDF file (default: MARGIN-<input>)')
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
    margin(args.pdf, margin=args.m, output=args.o)
