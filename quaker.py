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

URL = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

MAGNITUDE = {0: "Micro", 1: "Micro", 2: "Minor", 3: "Minor", 4: "Light", 5: "Moderate", 6: "Strong", 7: "Major", 8: "!Great!", 9: "!!Great!!", 10: "!!!GREAT!!!"}


class QuakeList(object):
    """
    all - return a json object containing all earthquake data
    local - return a json object containing data for quakes in Alaska, Washington, Oregon and California
    fubar - returns a string object, 'Fubar'
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
        all_quakes = []
        for quake in self.response['features']:
            all_quakes.append(quake['properties'])
        return all_quakes

    def local(self):
        local_quakes = []
        for quake in self.response['features']:
            if "Alaska" in quake['properties']['place']:
                local_quakes.append(quake['properties'])
            elif "Washington" in quake['properties']['place']:
                local_quakes.append(quake['properties'])
            elif "Oregon" in quake['properties']['place']:
                local_quakes.append(quake['properties'])
            elif "California" in quake['properties']['place']:
                local_quakes.append(quake['properties'])
        return local_quakes

    def fubar(self):
        return("Fubar")

def main():
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-a','--area', help='local or all', required=False)
    args = vars(parser.parse_args())
    #embed()

    current_quakes = QuakeList()
    current_quakes_list = current_quakes.all()


    if args['area'] == 'local':
        print("== Local Quakes ==\n")
        local_quake_list = current_quakes.local()
        for quake in local_quake_list:
            magnitude_index = int(quake['mag'])
            magnitude_name = MAGNITUDE[magnitude_index]
            print("%s quake of intensity %1.1f reported at %s") % (magnitude_name, quake['mag'], quake['place'])
        print("\n\n")
    elif args['area'] == 'all':
        print("== All Quakes ==\n")
        for quake in current_quakes_list:
            magnitude_index = int(quake['mag'])
            magnitude_name = MAGNITUDE[magnitude_index]
            print("%s quake of intensity %1.1f reported at %s") % (magnitude_name, quake['mag'], quake['place'])
        print("\n\n")
    else:
        print("== Local Quakes ==\n")
        local_quake_list = current_quakes.local()
        for quake in local_quake_list:
            magnitude_index = int(quake['mag'])
            magnitude_name = MAGNITUDE[magnitude_index]
            print("%s quake of intensity %1.1f reported at %s") % (magnitude_name, quake['mag'], quake['place'])
        print("\n\n")

if __name__ == '__main__':
    main()

