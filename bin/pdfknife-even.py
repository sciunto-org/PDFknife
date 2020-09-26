#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import logging
import PyPDF2

from PDFknife import __version__


def even_page(filename, output=None):

    if output is None:
        output = 'EVEN-' + filename

    reader = PyPDF2.PdfFileReader(filename)
    writer = PyPDF2.PdfFileWriter()
    for i in range(reader.getNumPages()):
        writer.addPage(reader.getPage(i))
    if reader.getNumPages() % 2 == 1:
        _, _, w, h = reader.getPage(0)['/MediaBox']
        writer.addBlankPage(w, h)
    with open(output, 'wb') as fd:
        writer.write(fd)


def main():
    parser = argparse.ArgumentParser(description='Make even pages PDF',
                                     epilog='')
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-d', '--debug', action='store_true',
                        default=False, help='Run in debug mode')
    parser.add_argument('pdf', metavar='PDF', help='Filename')
    parser.add_argument('-o', help='output', required=False, default=None)
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

    even_page(args.pdf, output=args.o)


if __name__ == "__main__":
    main()
