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

# Extra files
if (os.name == 'posix'):    # Files to be installed/packaged on Unix-like systems
    datadir = 'share/doc/'+appname+appversion
    datafiles = ['README', 'COPYING', 'Changelog']
    docsdir = datadir + '/docs'
    docsfiles = []
    try:
        dirlisting = os.listdir('docs/')
    except:
        print "Documentation isn't present and will not be installed/packaged."
        dirlisting = []
    for each in dirlisting:
        docsfiles.append('docs/'+each)
else:    # Other systems
    datadir = ''
    datafiles = []
    docsdir = ''
    docsfiles = []

setup(
        name = appname,
        version = appversion,
        packages = ['graph', 'graph.algorithms', 'graph.algorithms.filters', 'graph.algorithms.heuristics', 'graph.classes'],
        data_files = [(docsdir,docsfiles),
                       (datadir,datafiles)],
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