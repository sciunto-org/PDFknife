#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import shutil

logger = logging.getLogger()


def find_available_engine(engines=('pdftk', 'gs', 'pdfunite', 'pdfjam')):
    """
    Build a list of available engines.


    """
    available = []
    for engine in engines:
        if shutil.which(engine) is not None:
            available.append(engine)
    return available
