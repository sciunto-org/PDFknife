import argparse

from PDFknife import __version__, find_available_engine, setup_logging
from PDFknife import reverse


def main():
    parser = argparse.ArgumentParser(
        description='Reverse page order of a PDF',
        epilog='Uses pdftk or pdfjam. Last page becomes first, etc.')
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-d', '--debug', action='store_true',
                        default=False, help='enable debug logging')
    parser.add_argument('pdf', metavar='PDF', help='input PDF file')
    parser.add_argument('-o', help='output PDF file (default: REVERSE-<input>)',
                        required=False, default=None)
    args = parser.parse_args()

    logger = setup_logging(args.debug)
    logger.debug(f'Script arguments: {args}')

    available_engines = find_available_engine(engines=('pdftk', 'pdfjam'))
    logger.debug(f'Available engine: {available_engines}')

    reverse(args.pdf, output=args.o, engine=available_engines[0])
