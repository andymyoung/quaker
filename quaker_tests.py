#! /usr/bin/env python
# -*- coding: utf-8 -*-

__desc__ = "Unit tests for QuakeList"
__author__ = "ayoung"


from quaker import QuakeList
import unittest

class QuakeListTestCast(unittest.TestCase):
    """docstring for QuakeListTestCast"""
    def setUp(self):
        self.test_quakes = QuakeList()

    def testAllType(self):
        self.assertEqual(type(self.test_quakes.all()), type([]))

    def testAllSize(self):
        self.assertGreater(len(self.test_quakes.all()), 0)

    def testFubar(self):
        self.assertEqual(self.test_quakes.fubar(), "Fubar")

    def testLocalType(self):
        self.assertEqual(type(self.test_quakes.local()), type([]))

if __name__ == '__main__':
    unittest.main()
