#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from pypdf import PdfWriter, PdfReader

from ._utils import default_output

def even_page(filename, output=None):

    if output is None:
        output = default_output('EVEN', filename)

    reader = PdfReader(filename)
    writer = PdfWriter()
    for i in range(len(reader.pages)):
        writer.add_page(reader.pages[i])
    if len(reader.pages) % 2 == 1:
        _, _, w, h = reader.pages[0]['/MediaBox']
        writer.add_blank_page(w, h)
    with open(output, 'wb') as fd:
        writer.write(fd)
