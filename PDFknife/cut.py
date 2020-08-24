#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import logging

logger = logging.getLogger()


def cut(filename, output=None):
    """
    Cut PDF pages into two

    :param filename: PDF filepath
    :param output: PDF output
    """
    if output is None:
        output = 'CUT-' + filename
    command = ['mutool', 'poster', '-x', '2', filename, output]
    logger.debug(command)
    logger.debug(f'Executed command: {command}')
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    stdout, stderr = process.communicate()
