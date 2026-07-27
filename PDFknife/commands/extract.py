import argparse

from PDFknife import __version__, find_available_engine, setup_logging
from PDFknife import extract


def main():
    parser = argparse.ArgumentParser(
        description='Extract embedded images and fonts from a PDF',
        epilog='Uses mutool. Images and fonts are saved in the current directory.')
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-d', '--debug', action='store_true',
                        default=False, help='enable debug logging')
    parser.add_argument('pdf', metavar='PDF', help='input PDF file')
    args = parser.parse_args()

    logger = setup_logging(args.debug)
    logger.debug(f'Script arguments: {args}')

    available_engines = find_available_engine(engines=('mutool',))
    logger.debug(f'Available engine: {available_engines}')
    extract(args.pdf)
