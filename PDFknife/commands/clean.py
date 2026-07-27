import argparse
import logging

from PDFknife import __version__, find_available_engine
from PDFknife import clean


def main():
    parser = argparse.ArgumentParser(
        description='Recompress and clean a PDF with Ghostscript',
        epilog='Uses gs -dPDFSETTINGS=/prepress. Useful to fix metadata or reduce file size.')
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-d', '--debug', action='store_true',
                        default=False, help='enable debug logging')
    parser.add_argument('pdf', metavar='PDF', help='input PDF file')
    parser.add_argument('-o',
                        required=False, default=None,
                        help='output PDF file (default: CLEANED-<input>)')
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

    available_engines = find_available_engine(engines=('gs',))
    logger.debug(f'Available engine: {available_engines}')
    clean(args.pdf, output=args.o)
