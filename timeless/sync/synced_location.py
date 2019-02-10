from timeless.restaurants.models import Location
from timeless.sync.sync import PosterSync

"""
    Location synced to database.
    
    @todo #157:30min Implement synchronization between Poster and Database for
     Locations. Data coming from Poster has priority upon data stored in our
     database. 
"""


class SyncedLocation(Location):

    def __init__(self, poster_sync):
        pass

    def sync(self, poster_sync):
        raise Exception("sync for location not implemented yet")
