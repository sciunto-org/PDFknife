#!/usr/bin/env python

import setuptools

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
    name         = 'PDFknife',
    version      = '0.2.1',
    url          = "https://github.com/sciunto-org/PDFknife",
    author       = "Francois Boulogne",
    license      = "BSD",
    author_email = "devel@sciunto.org",
    description  = "Command line tools to manipulate PDF files",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages     = setuptools.find_packages(exclude=['doc', 'benchmarks']),
    scripts      = ['bin/pdfA5.py',
                    'bin/pdfmerge.py',
                    'bin/pdfrecto.py',
                    'bin/pdfreverse.py',
                    'bin/pdfsplit.py',
                    'bin/pdfshrink.py',
                    'bin/pdftrim.py',
                    ],
    install_requires = [],
)
