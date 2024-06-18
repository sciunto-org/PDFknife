#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Francois Boulogne
# License: GPLv3

import logging
import shutil
import tempfile
from PyPDF2 import PdfWriter, PdfReader


def tearpages(filename, first=False, last=False):
    """
    Copy filename to a tempfile, write pages startpage..N to filename.

    :param filename: PDF filepath
    :param first: remove the first page
    :param last: remove the last page
    """

    # Handle first/last page
    if first:
        startpage = 1
    else:
        startpage = 0

    if last:
        lastpage = 1
    else:
        lastpage = 0

    # Copy the pdf to a tmp file
    with tempfile.NamedTemporaryFile() as tmp:
        shutil.copy(filename, tmp.name)

        # Read the copied pdf
        input_file = PdfReader(tmp.name)
        # Seek for the number of pages
        #num_pages = input_file.getNumPages()
        num_pages = len(input_file.pages)

        if startpage >= num_pages - lastpage:
            raise ValueError('Incorrect number of pages')

        # Write pages excepted the first one
        output_file = PdfWriter()
        for i in range(startpage, num_pages-lastpage):
            output_file.add_page(input_file.pages[i])

    with open(filename, "wb") as outputStream:
        output_file.write(outputStream)

