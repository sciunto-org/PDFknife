#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import subprocess
import logging


def main(filenames, level='printer'):
    """
    Compress PDFs

    screen : 72dpi
    ebook : 150dpi
    printer : 300dpi
    prepress : 300dpi

    :param filenames: PDF filepaths
    """
    if level == 'all':
        levels = ['screen', 'ebook', 'printer', 'prepress']
    else:
        levels = [level, ]

    for level in levels:
        for filename in filenames:
            output = 'shrinked-' + level + '-' + filename
            command = ['gs',
                       '-sDEVICE=pdfwrite',
                       '-dCompatibilityLevel=1.4',
                       '-dPDFSETTINGS=/' + level,
                       '-dNOPAUSE',
                       '-dQUIET',
                       '-dBATCH',
                       '-sOutputFile=' + output,
                       filename]
            logger.debug(command)
            process = subprocess.Popen(command, stdout=subprocess.PIPE)
            stdout, stderr = process.communicate()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Shrink a pdf',
                                     epilog='')
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-d', '--debug', action='store_true',
                        default=False, help='Run in debug mode')
    parser.add_argument('pdf', metavar='PDF', help='Filename', nargs='+')
    parser.add_argument('-l', help='Quality level (1, 2, 3, 4 or all), 1=low',
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

    main(args.pdf, compression)
