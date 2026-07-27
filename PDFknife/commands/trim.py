import argparse
import logging

from PDFknife import __version__, find_available_engine
from PDFknife import trim


def main():
    parser = argparse.ArgumentParser(
        description='Trim (crop) edges of PDF pages',
        epilog='Uses pdfjam --trim --clip. All values in millimetres.')
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-d', '--debug', action='store_true',
                        default=False, help='enable debug logging')
    parser.add_argument('pdf', metavar='PDF', help='input PDF file')
    parser.add_argument('-o',
                        required=False, default=None,
                        help='output PDF file (default: TRIMMED-<input>)')
    parser.add_argument('--top',
                        required=False, default=0, type=float,
                        help='amount to trim from top in mm (default: 0)')
    parser.add_argument('--bottom',
                        required=False, default=0, type=float,
                        help='amount to trim from bottom in mm (default: 0)')
    parser.add_argument('--right',
                        required=False, default=0, type=float,
                        help='amount to trim from right in mm (default: 0)')
    parser.add_argument('--left',
                        required=False, default=0, type=float,
                        help='amount to trim from left in mm (default: 0)')
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
    trim(args.pdf,
         top=args.top, bottom=args.bottom,
         right=args.right, left=args.left,
         output=args.o)
