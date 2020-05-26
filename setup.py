#!/usr/bin/env python

import setuptools

setuptools.setup(
    name         = 'PDFknife',
    version      = '0.2',
    url          = "https://github.com/sciunto-org/PDFknife",
    author       = "Francois Boulogne",
    license      = "BSD",
    author_email = "devel@sciunto.org",
    description  = "",
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
