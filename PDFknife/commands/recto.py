import argparse

from PDFknife import __version__, setup_logging
from PDFknife import recto


def main():
    parser = argparse.ArgumentParser(
        description='Arrange two A5 recto pages side by side on A4 (top-to-bottom)',
        epilog='Used together with pdfknife-A5 for booklet printing.')
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-d', '--debug', action='store_true',
                        default=False, help='enable debug logging')
    parser.add_argument('pdf', metavar='PDF', help='input PDF file')
    parser.add_argument('-o', help='output PDF file (default: RECTO-<input>)',
                        required=False, default=None)
    args = parser.parse_args()

    logger = setup_logging(args.debug)
    logger.debug(f'Script arguments: {args}')

    recto(args.pdf, output=args.o)
