import argparse

from PDFknife import __version__, setup_logging
from PDFknife import rotate


def main():
    parser = argparse.ArgumentParser(
        description='Rotate all pages of a PDF by a given angle',
        epilog='Uses mutool clean -R or pdftk. Angles: 0, 90, 180, 270 (clockwise).')
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-d', '--debug', action='store_true',
                        default=False, help='enable debug logging')
    parser.add_argument('pdf', metavar='PDF', help='input PDF file')
    parser.add_argument('-a', '--angle',
                        default=90, type=int, choices=[0, 90, 180, 270],
                        help='rotation angle in degrees clockwise (default: 90)')
    parser.add_argument('-o',
                        required=False, default=None,
                        help='output PDF file (default: ROTATED-<input>)')
    args = parser.parse_args()

    logger = setup_logging(args.debug)
    logger.debug(f'Script arguments: {args}')

    rotate(args.pdf, angle=args.angle, output=args.o)
