#!/usr/bin/env python
# -*- coding: utf-8  -*-

'''
Tests the get-dependencies utility.
'''

import unittest
import getdeps

class TestGetDeps(unittest.TestCase):

    disc = getdeps.Discoverer()
    dpars = disc._parse_line

    def testPlainImport(self):
        line = 'import pygame'
        res = self.dpars(line)
        self.assertEqual(res, ['pygame'], 'GOT: %s' % res)

    def testFromModuleImport(self):
        line = 'from pygame import draw'
        res = self.dpars(line)
        self.assertEqual(res, ['pygame'], 'GOT: %s' % res)

    def testCommasStraight(self):
        line = 'import pygame, yaml, distutils'
        res = self.dpars(line)
        self.assertEqual(res, ['pygame', 'yaml', 'distutils'], 'GOT: %s' % res)

    def testCommasFrom(self):
        line = 'from pygame import draw, rect, sprite'
        res = self.dpars(line)
        self.assertEqual(res, ['pygame'], 'GOT: %s' % res)

    def testSemiColon(self):
        line = 'from pygame import draw, rect, sprite; import one, two'
        res = self.dpars(line)
        self.assertEqual(res, ['pygame', 'one', 'two'], 'GOT: %s' % res)

    def testCruft(self):
        line = '    import    pygame ; from one import a,b,c    '
        res = self.dpars(line)
        self.assertEqual(res, ['pygame', 'one'], 'GOT: %s' % res)

    def testTrailingComment(self):
        line = '    import    pygame ; from one import a,b,c   #import comment'
        res = self.dpars(line)
        self.assertEqual(res, ['pygame', 'one'], 'GOT: %s' % res)

    def testCommentedLine(self):
        line = '#    import    pygame ; from one import a,b,c'
        res = self.dpars(line)
        self.assertEqual(res, [], 'GOT: %s' % res)

    def testTrickyNames(self):
        line = 'import fromm; from importer import a; from gimport import b;'
        res = self.dpars(line)
        self.assertEqual(res, ['fromm', 'importer', 'gimport'],
                        'GOT: %s' % res)

    def testDottedModules(self):
        line = 'import gimporter.basic ; from fromm.bb import fromm, importer'
        res = self.dpars(line)
        self.assertEqual(res, ['gimporter.basic', 'fromm.bb'], 'GOT: %s' % res)

    def testAliasedImports(self):
        line = 'import gimporter.gimp as gimp; from hello import world as w'
        res = self.dpars(line)
        self.assertEqual(res, ['gimporter.gimp', 'hello'], 'GOT: %s' % res)

    def testMultipleAliases(self):
        line = 'import aaa.a as a, bbb as b; from xxx import c.c as c, bb as b'
        res = self.dpars(line)
        self.assertEqual(res, ['aaa.a', 'bbb', 'xxx'], 'GOT: %s' % res)

    def testNonRealImport(self):
        line = 'I\'m an important person'
        res = self.dpars(line)
        self.assertEqual(res, [], 'GOT: %s' % res)


if __name__ == "__main__":
    unittest.main()