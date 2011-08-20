#!/usr/bin/env python
# -*- coding: utf-8  -*-

'''
This utility scrapes official docs of python.org for a complete list of modules
from the standard library.

Source: http://docs.python.org/modindex.html
'''

from BeautifulSoup import BeautifulSoup as Soup
from collections import OrderedDict
from textwrap import dedent
from datetime import datetime as dt
import openanything
import yaml
import re

__author__ = "Mac Ryan"
__copyright__ = "Copyright 2011, Mac Ryan"
__license__ = "GPL v3"
#__version__ = "1.0.0"
__maintainer__ = "Mac Ryan"
__email__ = "quasipedia@gmail.com"
__status__ = "Development"

HEADER = '''\
    # Modules names from python stdlib
    #
    # ©2011 Mac Ryan - Licensed under GPL v.3
    #
    # This file is intended to work with the getdeps utility, which helps
    # finding out what are the dependencies of a python project when packaging
    # it for Debian.
    #
    '''

def main():
    # Get the page content, this requires changing the user-agent, as the
    # default one might be filtered by certain sites.
    url = 'http://docs.python.org/modindex.html'
    result = openanything.fetch(url)
    if result['status'] != 200:
        exit('The server returned: %s' % result['status'])
    soup = Soup(result['data'])
    # Find the table and parse the data
    module_names = [i.text.encode('UTF-8') for i in \
                    soup.findAll('tt', {'class':'xref'})]
    data = yaml.dump(module_names, default_flow_style=False,
                     allow_unicode=False, width = 79)
    f = open('data/stdlib-modules.yml', 'w')
    f.write(dedent(HEADER))
    now = dt.now().strftime('%d %B %Y')
    f.write('# Last scraped from docs.python.org on: %s\n\n' % now)
    f.write(data)
    f.close()

if __name__ == '__main__':
    main()
