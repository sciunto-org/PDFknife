#!/usr/bin/env python

import setuptools

setuptools.setup(
    name         = 'PDFknife',
    version      = '0.1',
    url          = "https://github.com/sciunto-org/PDFknife",
    author       = "Francois Boulogne",
    license      = "BSD",
    author_email = "devel@sciunto.org",
    description  = "",
    packages     = setuptools.find_packages(exclude=['doc', 'benchmarks']),
    install_requires = [],
)
