import argparse

from PDFknife import __version__, find_available_engine, setup_logging
from PDFknife import cut


def main():
    parser = argparse.ArgumentParser(
        description='Cut margin marks and toolbox artefacts off a PDF',
        epilog='Uses mutool. Useful to clean up pages printed with crop/registration marks.')
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-d', '--debug', action='store_true',
                        default=False, help='enable debug logging')
    parser.add_argument('pdf', metavar='PDF', help='input PDF file')
    parser.add_argument('-o',
                        required=False, default=None,
                        help='output PDF file (default: CUT-<input>)')
    args = parser.parse_args()

    logger = setup_logging(args.debug)
    logger.debug(f'Script arguments: {args}')

    available_engines = find_available_engine(engines=('mutool',))
    logger.debug(f'Available engine: {available_engines}')
    cut(args.pdf, output=args.o)
