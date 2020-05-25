#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import subprocess
import logging
import shutil


def main(filename, output=None, *, engine='pdftk'):
    """
    reverse a PDF

    :param filenames: PDF filepath
    :param output: PDF output
    """
    if output is None:
        output = 'REVERSED-' + filename

    if engine == 'pdfjam':
        command = ['pdfjam',
                   filename,
                   'last-1',
                   '--outfile',
                   output,
                   ]
    elif engine == 'pdftk':
        command = ['pdftk', ]
        command.append(filename)
        command.extend(['cat', 'end-1', 'output'])
        command.append(output)
    else:
        raise ValueError(f'Wrong engine name: {engine}')

    logger.debug(f'Executed command: {command}')
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    stdout, stderr = process.communicate()


def find_available_engine(engines=('pdftk', 'pdfjam')):
    """
    Build a list of available engines.


    """
    available = []
    for engine in engines:
        if shutil.which(engine) is not None:
            available.append(engine)
    return available


if __name__ == '__main__':
    # TODO add option for engine
    parser = argparse.ArgumentParser(description='Reverse pdf',
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

    available_engines = find_available_engine()
    logger.debug(f'Available engine: {available_engines}')

    main(args.pdf, output=args.o, engine=available_engines[0])