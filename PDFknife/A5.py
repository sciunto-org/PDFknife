#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import logging

logger = logging.getLogger()


def A5(filename, output=None, *, engine='pdfjam'):
    """
    Merge successive pages into two joined A5 pages.

    :param filename: PDF filepath
    :param output: PDF output
    """
    if output is None:
        output = 'A5-' + filename

    if engine == 'pdfjam':
        command = ['pdfjam',
                   '--nup', '2x1', '--landscape',
                   filename,
                   '--outfile',
                   output,
                   ]
    else:
        raise ValueError(f'Wrong engine name: {engine}')

    logger.debug(f'Executed command: {command}')
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    stdout, stderr = process.communicate()
