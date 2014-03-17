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
import time


MAGNITUDE = {0: "Micro", 1: "Micro", 2: "Minor", 3: "Minor", 4: "Light", 5: "Mod.", 6: "Strong", 7: "Major", 8: "!Great!", 9: "!!Great!!", 10: "!!!GREAT!!!"}
LOCAL_REGIONS = ["California", "Alaska", "Oregon", "Washington"]

class QuakeList(object):
    """
    all - return a json object containing all earthquake data
    local - return a json object containing data for quakes in states listed in LOCAL_REGIONS
    fubar - returns a string object, 'Fubar'
    """
    def __init__(self):
        self.URL = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
        opener = urllib.FancyURLopener({})
        try:
            f = opener.open(self.URL)
            content = f.read()
        except IOError as error:
            print(" \n!ZOINKS!  %s" % error)
            sys.exit(-1)
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
        print("Mag.\tInt.\t\t\tLocation\t\t\tTime")
        print "=" * 82

        for quake in quake_list:
            magnitude_index = int(quake['mag'])
            magnitude_name = MAGNITUDE[magnitude_index]
            if magnitude_name != 'Micro': # Leave out the innumerable minor quakes for now
                quake_time =  time.strftime("%a, %d %b %H:%M:%S +0000", time.localtime(float((str(quake['time'])[0:10]))))
                #embed()
                print("%s\t%1.1f\t%-40s%s") % (magnitude_name, quake['mag'], quake['place'][0:39], quake_time)

    parser = argparse.ArgumentParser(description='Shows recent earthquake activity')
    parser.add_argument('-a','--area', help="Select AREA of 'local' (for PNW) or 'all' (for global)", required=False)
    args = vars(parser.parse_args())

    current_quakes = QuakeList()

    if args['area'] == 'all':
        print("\n== All Quakes ==\n")
        printQuake(current_quakes.all())
        print("\n\n")
    else:
        print("\n== Local Quakes ==\n")
        printQuake(current_quakes.local())
        print("\n\n")

if __name__ == '__main__':
    main()
