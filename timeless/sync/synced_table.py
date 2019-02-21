from timeless.restaurants.models import Table
from timeless.sync.sync import PosterSync

"""
    Table synced to database.
    
    @todo #342:30min Implement synchronization between Poster and Database for
     Tables. Data coming from Poster has priority upon data stored in our
     database. Synchronization must be done via celery job. See sync of 
     Location implementation as reference. Tests for poster sync are already 
     created in it_sync_tables_test.py    
  
"""


class SyncedTable(Table):

    def __init__(self, poster_sync):
        pass

    def sync(self, poster_sync):
        raise Exception("sync for table not implemented yet")
