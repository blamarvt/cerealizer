#! /usr/bin/env python

# Cerealizer
# Copyright (C) 2005-2012 Jean-Baptiste LAMY
#
# This program is free software.
# It is available under the Python licence.

import os.path
import setuptools
import sys


setuptools.setup(
    name = "Cerealizer",
    version = "0.9.0",
    license = "Python licence",
    description = "A secure pickle-like module",
    long_description = """A secure pickle-like module.
It support basic types (int, string, unicode, tuple, list, dict, set,...),
old and new-style classes (you need to register the class for security), object cycles,
and it can be extended to support C-defined type.""",
    author = "Lamy Jean-Baptiste (Jiba)",
    author_email = "jibalamy@free.fr",
    url = "http://home.gna.org/oomadness/en/cerealizer/index.html",
    classifiers  = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Python Software Foundation License",
        "Programming Language :: Python :: 2",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    package_dir = {"cerealizer" : "."},
    packages = ["cerealizer"],
    include_package_data = True,
)
