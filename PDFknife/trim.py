#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import logging

logger = logging.getLogger()


def trim(filename, top=1, bottom=1, right=1, left=1, output=None):
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
