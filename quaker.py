#! /usr/bin/env python
# -*- coding: utf-8 -*-
__desc__ = "A simple program to return the most current earthquake data."
__author__ = "ayoung"


# from IPython import embed  # embed() -- Using PyCharm for now, so no ipython debugger
import unittest
import urllib
import json
import pprint as p
import sys

URL = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

MAGNITUDE = {0: "Micro", 1: "Micro", 2: "Minor", 3: "Minor", 4: "Light", 5: "Moderate", 6: "Strong", 7: "Major", 8: "!Great!", 9: "!!Great!!", 10: "!!!GREAT!!!"}


class QuakeList(object):
    """
    all - return a json object containing all earthquake data
    """
    def __init__(self):
        opener = urllib.FancyURLopener({})
        try:
            f = opener.open(URL)
            content = f.read()
        except IOError as error:
            print("ZOINKS! \n %s" % error)
            sys.exit(0)
        self.response = json.loads(content)

    def all(self):
        return self.response

    def fubar(self):
        return("Fubar")


current_quakes = QuakeList()
current_quakes_JSON = current_quakes.all()
for quake in current_quakes_JSON['features']:
    magnitude_index = int(quake['properties']['mag'])
    magnitude_name = MAGNITUDE[magnitude_index]
    print("%s quake of intensity %1.1f reported at %s") % (magnitude_name, quake['properties']['mag'], quake['properties']['place'])
print("\n\n")



#
# UNIT TESTS
#
class QuakeListTestCast(unittest.TestCase):
    """docstring for QuakeListTestCast"""
    def setUp(self):
        self.test_quakes = QuakeList()

    def testAllType(self):
        self.assertEqual(type(self.test_quakes.all()), type({1:1}))

    def testAllSize(self):
        self.assertGreater(len(self.test_quakes.all()), 0)

    def testFubar(self):
        self.assertEqual(self.test_quakes.fubar(), "Fubar")

if __name__ == '__main__':
    unittest.main()
