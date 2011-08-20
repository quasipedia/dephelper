#!/usr/bin/env python
# -*- coding: utf-8  -*-

'''
This is a small script that tries to find the dependencies used in the source of
a python program and match them with debian packages available in repositories.
'''

import argparse
import distutils.sysconfig as sysconfig
import os
import yaml
from BeautifulSoup import BeautifulSoup as Soup

__author__ = "Mac Ryan"
__copyright__ = "Copyright 2011, Mac Ryan"
__license__ = "GPL v3"
#__version__ = "1.0.0"
__maintainer__ = "Mac Ryan"
__email__ = "quasipedia@gmail.com"
__status__ = "Development"


class Discoverer(object):

    '''
    Class for discovering and organising all dependencies in a project.
    '''

    def __init__(self, tree_base, exclude):
        '''
        tree_base : base of the source tree.
        exclude   : list of file names to exclude from dependency analysis.
        '''
        # Load list of stdlib modules
        self.__stdlib_modules = yaml.load(open('stdlib-modules.yml'))
        # Find all source files to be examined (and save internal moudules)
        files = []
        self.__internal_modules = []
        for dir_triplet in os.walk(tree_base):
            dirpath, dirnames, filenames = dir_triplet
            for name in filenames:
                if name[-3:] == '.py':
                    self.__internal_modules.append(name[:-3])
                    if name not in exclude:
                        files.append(os.path.join(dirpath, name))
        # Find all import lines and get the modulename
        modules = []
        for file in files:
            for line in open(file).readlines():
                if line.find('import') != -1 \
                and '"' not in line and "'" not in line:
                    modules.extend(self._parse_line(line))
        modules = [m[:m.index('.')] if '.' in m else m for m in modules]
        self.__modules = sorted(list(set(modules)))

    def _parse_line(self, line):
        '''
        Return a list of modules that are imported on the line, if any.
        '''
        modules = []
        # Remove commented parts
        hash = line.find('#')
        if hash != -1:
            line = line[:hash]
        # Splits multi-import lines that use `;` to separate imports
        bits = [bit for bit in line.split(';') if bit]
        for bit in bits:
            words = bit.replace(',', ' ').split()
            #remove aliases
            while 'as' in words:
                words.pop(words.index('as')+1)
                words.remove('as')
            fr = words.index('from') if 'from' in words else None
            im = words.index('import') if 'import' in words else None
            if im is None:
                continue
            elif fr is not None and fr < im:
                modules.append(words[fr+1])
            else:
                modules.extend(words[im+1:])
        return modules

    def get_imports(self, internals=False, stdlib=False):
        '''
        Return a list of the imported modules.
        Filter the list according to the kword arguments
        '''
        res = self.__modules[:]
        if stdlib == False:
            res = filter(lambda x : x not in self.__stdlib_modules, res)
        if internals == False:
            res = filter(lambda x : x not in self.__internal_modules, res)
        return res

def main():
    # General description of the program
    desc = 'Find the external dependencies of a python source tree.'
    parser = argparse.ArgumentParser(description=desc)
    # Tree base option
    hlpmsg = 'The base of the source tree to be serached for dependencies, ' + \
             'defaults to the working directory'
    parser.add_argument('-b', '--tree-base', default='.', help=hlpmsg)
    # Exclude files option
    hlpmsg = 'Files to be excluded from the source tree search, ' + \
             'defaults to none'
    parser.add_argument('-e', '--excluded-files', default='',
                                                  nargs='*', help=hlpmsg)
    # Include internal modules option
    hlpmsg = 'Includes internal modules as external dependencies'
    parser.add_argument('-i', '--include-internals', action='store_true',
                        dest='internals', help=hlpmsg)
    # Include internal modules option
    hlpmsg = 'Includes stdlib modules as external dependencies'
    parser.add_argument('-s', '--include-stdlib', action='store_true',
                        dest='stdlib', help=hlpmsg)
    # Actual command parsing
    args = parser.parse_args()
    discoverer = Discoverer(args.tree_base, args.excluded_files)
    print(discoverer.get_imports(internals=args.internals, stdlib=args.stdlib))

if __name__ == '__main__':
    main()
