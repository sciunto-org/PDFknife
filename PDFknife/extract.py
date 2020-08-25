#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import logging

logger = logging.getLogger()


def extract(filename):
    """
    Extract images and fonts.

    :param filename: PDF filepath
    """
    command = ['mutool', 'extract', filename]
    logger.debug(command)
    logger.debug(f'Executed command: {command}')
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    stdout, stderr = process.communicate()
