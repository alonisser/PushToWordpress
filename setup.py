#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION = '0.1'

# Grab requirments.
with open('require.txt') as f:
    required = f.readlines()

# Publish Helper.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name = "Push_To_Wordpress",
    version = VERSION,
    scripts = ['presser.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = required,

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.md', '*.rst'],
    }

    # metadata for upload to PyPI
    author = "Alonisser",
    author_email = "alonisser@gmail.com",
    description = "a commandline tool to post to wordpress with XML-RPC",
    license = "permissive",
    keywords = "blogging wordpress commandline",
    url = "https://github.com/alonisser/PushToWordpress",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)
