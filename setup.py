#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import logging

try:
    from setuptools import setup, find_packages
except ImportError, ie:
    import ez_setup
    ez_setup.use_setuptools()

# Startup
appname = "python-graph"
appversion = "1.4.0"
docfiles = []
for each in os.listdir('docs/'):
	docfiles = docfiles + ['docs/'+each]

setup(
        name = appname,
        version = appversion,
        packages = [ 'graph' ],
        data_files = [('share/doc/'+appname+appversion+'/docs',docfiles),
					   ('share/doc/'+appname+appversion,['README', 'Changelog', 'COPYING'])],
        author = "Pedro Matiello",
        author_email = "pmatiello@gmail.com",
        description = "A library for working with graphs in Python",
        license = "MIT",
        keywords = "python graph algorithms library",
        url = "http://code.google.com/p/python-graph/",
        classifiers = ["License :: OSI Approved :: MIT License","Topic :: Software Development :: Libraries :: Python Modules"],
        long_description = "python-graph is a library for working with graphs in Python. This software provides a suitable data structure for representing graphs and a whole set of important algorithms.",
        test_suite = "graph.tests",
)