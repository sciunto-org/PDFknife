#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import PyPDF2

from ._utils import default_output

def even_page(filename, output=None):

    if output is None:
        output = default_output('EVEN', filename)

    reader = PyPDF2.PdfFileReader(filename)
    writer = PyPDF2.PdfFileWriter()
    for i in range(reader.getNumPages()):
        writer.addPage(reader.getPage(i))
    if reader.getNumPages() % 2 == 1:
        _, _, w, h = reader.getPage(0)['/MediaBox']
        writer.addBlankPage(w, h)
    with open(output, 'wb') as fd:
        writer.write(fd)
