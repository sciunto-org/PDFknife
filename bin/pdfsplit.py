#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import subprocess
import logging


def split(filename, output=None):
    """
    Split PDFs

    :param filename: PDF filepath
    :param output: PDF output
    """
    if output is None:
        name = filename.rstrip('.pdf')
        output = 'PAGE-%05d_' + name + '.pdf'
    command = ['gs',
               '-sDEVICE=pdfwrite',
               '-dNOPAUSE',
               '-dQUIET',
               '-dBATCH',
               '-sOutputFile=' + output,
               ]
    command.append(filename)
    logger.debug(command)
    logger.debug(f'Executed command: {command}')
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    stdout, stderr = process.communicate()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Split pdf',
                                     epilog='')
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-d', '--debug', action='store_true',
                        default=False, help='Run in debug mode')
    parser.add_argument('pdf', metavar='PDF', help='Filename', nargs='+')
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

    for f in args.pdf:
        split(f, output=args.o)
