#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import logging

from PDFknife import __version__
from PDFknife import tearpages


def main():
    parser = argparse.ArgumentParser(description='Remove first or last page of a PDF',
                                     epilog='')
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-d', '--debug', action='store_true',
                        default=False, help='Run in debug mode')
    parser.add_argument('pdf', metavar='PDF', help='Filename')
    parser.add_argument('--first', action='store_true',
                        default=False, help='Tear the first page')
    parser.add_argument('--last', action='store_true',
                        default=False, help='Tear the last page')
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

    tearpages(args.pdf, first=args.first, last=args.last)


if __name__ == "__main__":
    main()
