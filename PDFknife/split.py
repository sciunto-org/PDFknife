#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import logging
import os.path
from ._utils import default_output

logger = logging.getLogger()


def split(filename, output=None, outpath=None):
    """
    Split PDFs

    :param filename: PDF filepath
    :param output: PDF output
    ;param path: path output
    """
    logger.debug(f'Split {filename}, with {output} in {outpath}')
    if output is None:
        output = default_output('PAGE-%05d_', filename)
    if outpath is not None:
            output = os.path.join(outpath, output)
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
