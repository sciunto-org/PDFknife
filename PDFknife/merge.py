#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import logging

logger = logging.getLogger()


def merge(filenames, output=None, *, engine='pdftk'):
    """
    Merge PDFs

    :param filenames: PDF filepaths
    :param output: PDF output
    """
    if output is None:
        output = 'MERGED-' + filenames[0]

    if engine == 'gs':
        command = ['gs',
                   '-sDEVICE=pdfwrite',
                   '-dNOPAUSE',
                   '-dQUIET',
                   '-dBATCH',
                   '-sOutputFile=' + output,
                   ]
        command.extend(filenames)
    elif engine == 'pdftk':
        command = ['pdftk', ]
        command.extend(filenames)
        command.extend(['cat', 'output'])
        command.append(output)
    elif engine == 'pdfunite':
        command = ['pdfunite', ]
        command.extend(filenames)
        command.append(output)
    elif engine == 'pdfjam':
        command = ['pdfjam', ]
        command.extend(filenames)
        command.append('-o')
        command.append(output)
    else:
        raise ValueError(f'Wrong engine name: {engine}')

    logger.debug(f'Executed command: {command}')
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    stdout, stderr = process.communicate()
