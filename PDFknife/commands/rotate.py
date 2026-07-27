import argparse
import logging

from PDFknife import __version__
from PDFknife import rotate


def main():
    parser = argparse.ArgumentParser(description='Rotate a pdf',
                                     epilog='')
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-d', '--debug', action='store_true',
                        default=False, help='Run in debug mode')
    parser.add_argument('pdf', metavar='PDF', help='Filename')
    parser.add_argument('-a', '--angle',
                        default=90, type=int, choices=[0, 90, 180, 270],
                        help='Rotation angle (default: 90)')
    parser.add_argument('-o',
                        required=False, default=None,
                        help='output')
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

    rotate(args.pdf, angle=args.angle, output=args.o)
