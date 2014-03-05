#! /usr/bin/env python
# -*- coding: utf-8 -*-
__desc__ = "A simple program to return the most current earthquake data."
__author__ = "ayoung"


from IPython import embed  # embed()
import urllib
import json
import pprint as p
import sys
import argparse

# URL = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
URL = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
MAGNITUDE = {0: "Micro", 1: "Micro", 2: "Minor", 3: "Minor", 4: "Light", 5: "Moderate", 6: "Strong", 7: "Major", 8: "!Great!", 9: "!!Great!!", 10: "!!!GREAT!!!"}
LOCAL_REGIONS = ["California", "Alaska", "Oregon", "Washington"]

class QuakeList(object):
    """
    all - return a json object containing all earthquake data
    local - return a json object containing data for quakes in states listed in LOCAL_REGIONS
    fubar - returns a string object, 'Fubar'
    """
    def __init__(self):
        opener = urllib.FancyURLopener({})
        try:
            f = opener.open(URL)
            content = f.read()
        except IOError as error:
            print(" \n!ZOINKS!  %s" % error)
            sys.exit(0)
        self.response = json.loads(content)

    def all(self):
        all_quakes = []
        for quake in self.response['features']:
            all_quakes.append(quake['properties'])
        return all_quakes

    def local(self):
        local_quakes = []
        for quake in self.response['features']:
            for region in LOCAL_REGIONS:
                if region in quake['properties']['place']:
                    local_quakes.append(quake['properties'])
        return local_quakes

    def fubar(self):
        return("Fubar")

def main():
    def printQuake(quake_list):
        for quake in quake_list:
            magnitude_index = int(quake['mag'])
            magnitude_name = MAGNITUDE[magnitude_index]
            if magnitude_name != 'Micro': # Leave out the innumerable minor quakes for now
                print("%s quake of intensity %1.1f reported at %s") % (magnitude_name, quake['mag'], quake['place'])

    parser = argparse.ArgumentParser(description='Shows recent earthquake activity')
    parser.add_argument('-a','--area', help="Select AREA of 'local' (for PNW) or 'all' (for global)", required=False)
    args = vars(parser.parse_args())
    #embed()

    current_quakes = QuakeList()
    if args['area'] == 'local':
        print("== Local Quakes ==\n")
        printQuake(current_quakes.local())
        print("\n\n")
    elif args['area'] == 'all':
        print("== All Quakes ==\n")
        printQuake(current_quakes.all())
        print("\n\n")
    else:
        print("== Local Quakes ==\n")
        printQuake(current_quakes.local())
        print("\n\n")

if __name__ == '__main__':
    main()
