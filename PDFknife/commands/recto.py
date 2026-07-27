import argparse
import logging

from PDFknife import __version__
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

    recto(args.pdf, output=args.o)
