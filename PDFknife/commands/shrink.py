import argparse
import logging

from PDFknife import __version__, find_available_engine
from PDFknife import shrink


def main():
    parser = argparse.ArgumentParser(
        description='Compress/reduce file size of PDFs with Ghostscript',
        epilog='Levels: 1=screen (72dpi), 2=ebook (150dpi), 3=printer (300dpi), 4=prepress (300dpi), all=all levels.')
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-d', '--debug', action='store_true',
                        default=False, help='enable debug logging')
    parser.add_argument('pdf', metavar='PDF', help='input PDF file(s)', nargs='+')
    parser.add_argument('-l', help='compression level: 1 (lowest quality) to 4 (highest), or all (default: all)',
                        required=False, default='all')

    args = parser.parse_args()
    if args.l == '4':
        compression = 'prepress'
    elif args.l == '3':
        compression = 'printer'
    elif args.l == '2':
        compression = 'ebook'
    elif args.l == '1':
        compression = 'screen'
    else:
        compression = 'all'

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
    shrink(args.pdf, compression)
