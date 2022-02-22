#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import logging

from PDFknife import __version__, find_available_engine


def scale(filename, scale, output=None):
    """
    # If fails, needs to comment gs line in
    # /etc/ImageMagick-7/policy.xml
    """
    from PDFknife._utils import default_output
    import subprocess
    if output is None:
        output = default_output('SCALED', filename)

    command = ['pdfjam',
	           '--scale', scale,
               filename,
               '--outfile',
               output,
               ]

    print(command)

    #logger.debug(command)
    #logger.debug(f'Executed command: {command}')
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    stdout, stderr = process.communicate()


def main():
    parser = argparse.ArgumentParser(description='rescale a pdf',
                                     epilog='')
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-d', '--debug', action='store_true',
                        default=False, help='Run in debug mode')
    parser.add_argument('pdf', metavar='PDF', help='Filename')
    parser.add_argument('-s', help='Scale value',
                        required=True, default='.9')
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

    scale(args.pdf, scale=args.s)


if __name__ == '__main__':
    main()
