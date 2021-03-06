# -*- coding: utf-8 -*-

"""
    station.py
    ~~~~~~~~~~

    Helper file for retrieving and returning data
    about MTA subway stations.
"""

_stations = {}

class Station(object):

    def __init__(self, line):
        data = line.split(',')
        id = data[0]

        self.name = data[2]
        self.coords = [data[4], data[5]]


# Parses CSV from stops.txt and saves it in memory

def load_stations():
    f = open('./subway/google_transit/stops.txt', 'r')
    contents = f.read()

    i = -1
    for line in contents.split('\n'):
        i += 1

        if i == 0:
            continue

        data = line.split(',')
        if len(data) == 10:
            id = data[0]

            if id.endswith('N') or id.endswith('S'):
                continue

            station = Station(line)
            _stations[id] = station


# Provides a more public method of retrieving a station

def get_station(id):
    if len(_stations) == 0:
        load_stations()

    return _stations[id]
