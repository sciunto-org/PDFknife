#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import logging

from ._utils import default_output

logger = logging.getLogger()


def reverse(filename, output=None, *, engine='pdftk'):
    """
    reverse a PDF

    :param filename: PDF filepath
    :param output: PDF output
    """
    if output is None:
        output = default_output('REVERSED', filename)

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
