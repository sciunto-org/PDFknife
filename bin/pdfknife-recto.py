#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import subprocess
import logging
import shutil
import tempfile
import os.path


from PDFknife import __version__, find_available_engine
from PDFknife import merge, split


# TODO: handle engines
def recto(filename, output=None, *, engine='pdfjam'):
    """
    Merge successive pages into two joined A5 pages.

    :param filename: PDF filepath
    :param output: PDF output
    """

    # TODO with statement?
    dirpath = tempfile.mkdtemp()
    logger.debug(f'Temp directory {dirpath}')

    logger.debug('Split pages...')
    split(filename, output='PAGE-%05d-1.pdf', outpath=dirpath)

    logger.debug(os.listdir(dirpath))
    num_pages = len([name for name in os.listdir(dirpath)])
    logger.debug(f'PDF has {num_pages}')

    # Create a blank page
    # command = ['echo', '""', '|',  'ps2pdf', '-sPAPERSIZE=a4', '-',  'blank.pdf']
    logger.debug('Create blank pages...')
    for i in range(num_pages):
        number = str(i+1).zfill(5)
        blank_path = os.path.join(dirpath, f'PAGE-{number}-2.pdf')
        command = ['convert', 'xc:none', '-page', 'A4', blank_path]

        logger.debug(f'Executed command: {command}')
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()

    pages = [os.path.join(dirpath, name) for name in os.listdir(dirpath)]

    if output is None:
        output = 'RECTO-' + filename

    merge(sorted(pages), output=output)

    shutil.rmtree(dirpath)


if __name__ == '__main__':
    # TODO add option for engine
    parser = argparse.ArgumentParser(description='Side-by-side A5 pdf',
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

    # TODO
    # available_engines = find_available_engine()
    # logger.debug(f'Available engine: {available_engines}')

    # recto(args.pdf, output=args.o, engine=available_engines[0])
    recto(args.pdf, output=args.o)
