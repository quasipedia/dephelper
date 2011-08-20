#!/usr/bin/env python
# -*- coding: utf-8  -*-

# Needed in case the target system doesn't have setuptools installed
from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

setup(
    name = "dephelper",
    version = "1.0dev",
    description = "Find debian external dependency in python programs",
    packages = find_packages(),
    include_package_data = True,
    package_dir = {'':'.'},
    package_data = {'': ['data/*.yml']},
    install_requires = ['PyYAML >= 3.9', 'Pygame >= 1.9.1'],
    # metadata for upload to PyPI
    author = "Mac Ryan",
    author_email = "quasipedia@gmail.com",
    license = "MIT",
    keywords = "aeroplane game videogame air-traffic-control",
    url = "https://github.com/quasipedia/dephelper",
    entry_points = {
        'console_scripts': [
            'dephelp = src.getdeps:main',
        ]
    },
    classifiers = ['Development Status :: 3 - Alpha',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Software Development :: Build Tools',
                   'Topic :: Utilities'],
    long_description = '''Dephelper is a script that helps finding what are the
dependencies of a python program other than those to its modules and those in
the standard lib. It is meant to be used during the process of packaging python
software for debian.'''
)
