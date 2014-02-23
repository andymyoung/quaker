#! /usr/bin/env python
# -*- coding: utf-8 -*-
__desc__ = "A simple program to return the most current earthquake data."
__author__ = "ayoung"


# from IPython import embed  # embed() -- Using PyCharm for now, so no ipython debugger
import urllib
import json
import pprint as p
import sys

URL = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

MAGNITUDE = {0: "Micro", 1: "Micro", 2: "Minor", 3: "Minor", 4: "Light", 5: "Moderate", 6: "Strong", 7: "Major", 8: "!Great!", 9: "!!Great!!", 10: "!!!Great!!!"}

class QuakeList(object):

    def __init__(self):
        opener = urllib.FancyURLopener({})
        try:
            f = opener.open(URL)
            content = f.read()
        except IOError as error:
            print "ZOINKS!"
            sys.exit(0)
        self.response = json.loads(content)

    def all(self):
        return self.response



current_quakes = QuakeList()
current_quakes_JSON = current_quakes.all()
for quake in current_quakes_JSON['features']:
    magnitude_index = int(quake['properties']['mag'])
    magnitude_name = MAGNITUDE[magnitude_index]
    print("%s quake of intensity %1.1f reported at %s") % (magnitude_name, quake['properties']['mag'], quake['properties']['place'])