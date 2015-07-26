# -*- coding: utf-8 -*-

from google.transit import gtfs_realtime_pb2 as gtfs
import mta_pb2 as mta
import urllib

mta_url = 'http://datamine.mta.info/files/k38dkwh992dk/gtfs'

def update():
    # f = open('gtfs', 'r')
    # response = f.read()

    response = urllib.urlopen(mta_url)

    feed = gtfs.FeedMessage()
    feed.ParseFromString(response.read())
    
    for entity in feed.entity:
        if entity.HasField('trip_update'):
            print entity

update()
