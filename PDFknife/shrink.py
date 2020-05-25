#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import logging

logger = logging.getLogger()


def shrink(filenames, level='printer'):
    """
    Compress PDFs

    screen : 72dpi
    ebook : 150dpi
    printer : 300dpi
    prepress : 300dpi

    :param filenames: PDF filepaths
    """
    if level == 'all':
        levels = ['screen', 'ebook', 'printer', 'prepress']
    else:
        levels = [level, ]

    for level in levels:
        for filename in filenames:
            output = 'shrinked-' + level + '-' + filename
            command = ['gs',
                       '-sDEVICE=pdfwrite',
                       '-dCompatibilityLevel=1.4',
                       '-dPDFSETTINGS=/' + level,
                       '-dNOPAUSE',
                       '-dQUIET',
                       '-dBATCH',
                       '-sOutputFile=' + output,
                       filename]
            logger.debug(command)
            process = subprocess.Popen(command, stdout=subprocess.PIPE)
            stdout, stderr = process.communicate()
