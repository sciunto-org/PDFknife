#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import logging

from PDFknife import __version__
from PDFknife import trim


def main():
    parser = argparse.ArgumentParser(description='Trim a pdf',
                                     epilog='')
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-d', '--debug', action='store_true',
                        default=False, help='Run in debug mode')
    parser.add_argument('pdf', metavar='PDF', help='Filename')
    parser.add_argument('-o',
                        required=False, default=None,
                        help='output')
    parser.add_argument('--top',
                        required=False, default=0,
                        help='top length in mm')
    parser.add_argument('--bottom',
                        required=False, default=0,
                        help='bottom length in mm')
    parser.add_argument('--right',
                        required=False, default=0,
                        help='right length in mm')
    parser.add_argument('--left',
                        required=False, default=0,
                        help='left length in mm')
    args = parser.parse_args()

    # Logger level
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

    trim(args.pdf,
         top=args.top, bottom=args.bottom,
         right=args.right, left=args.left,
         output=args.o)


if __name__ == '__main__':
    main()
