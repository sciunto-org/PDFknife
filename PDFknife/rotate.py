import logging

import pypdf

from ._utils import default_output

logger = logging.getLogger()


def rotate(filename, angle=90, output=None):
    if output is None:
        output = default_output('ROTATED', filename)

    reader = pypdf.PdfReader(filename)
    writer = pypdf.PdfWriter()

    for page in reader.pages:
        page.rotate(angle)
        writer.add_page(page)
        writer.add_page(page)

    with open(output, 'wb') as f:
        writer.write(f)
