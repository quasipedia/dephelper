#!/usr/bin/env python
# -*- coding: utf-8  -*-

from setuptools import setup, find_packages

setup(
    name = "dephelper",
    version = "1.0.dev",
    packages = find_packages('.'),
    include_package_data = True,
    package_dir = {'':'.'},
    # metadata for upload to PyPI
    author = "Mac Ryan",
    author_email = "quasipedia@gmail.com",
    description = "Python",
    license = "GPL",
    keywords = "aeroplane game videogame air-traffic-control",
    url = "https://github.com/quasipedia/dephelper",
    entry_points = {
        'console_scripts': [
            'dephelp = getdeps.main',
            'dephelp-updatestdlib = scrape-modulenames.main'
        ]
    }
)
