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
    logger.debug(f'Executed command: {command}')
    subprocess.run(command, check=True)
