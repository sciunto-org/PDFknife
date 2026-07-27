import argparse

from PDFknife import __version__, find_available_engine, setup_logging
from PDFknife import merge


def main():
    parser = argparse.ArgumentParser(
        description='Merge several PDF files into one',
        epilog='Supports pdftk, gs, pdfunite and mutool as backend.')
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-d', '--debug', action='store_true',
                        default=False, help='enable debug logging')
    parser.add_argument('pdf', metavar='PDF', help='input PDF files', nargs='+')
    parser.add_argument('-o',
                        help='output PDF file (default: MERGED-<first>)',
                        required=False,
                        default=None)
    args = parser.parse_args()

    logger = setup_logging(args.debug)
    logger.debug(f'Script arguments: {args}')

    available_engines = find_available_engine()
    logger.debug(f'Available engine: {available_engines}')

    merge(args.pdf, output=args.o, engine=available_engines[0])
