#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import subprocess
import logging


def main(filename, top=1, bottom=1, right=1, left=1, output=None):
    """
    Trim a PDF

    :param filename: PDF filepath
    :param output: PDF output
    """
    if output is None:
        output = 'TRIMMED-' + filename
    command = ['pdfjam',
               filename,
               '--trim',
               f'\'{left}mm {bottom}mm {right}mm {top}mm\'',
               '--clip',
               'true',
               '--outfile',
               output,
               ]
    logger.debug(command)
    logger.debug(f'Executed command: {command}')
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    stdout, stderr = process.communicate()


if __name__ == '__main__':
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

    main(args.pdf,
         top=args.top, bottom=args.bottom,
         right=args.right, left=args.left,
         output=args.o)
