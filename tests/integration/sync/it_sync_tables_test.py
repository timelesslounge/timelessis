from timeless.restaurants.models import Table

"""
    Table synced to database.
    @todo #342:30min Implement synchronization between Poster and Database for
     Tables. Data coming from Poster has priority upon data stored in our
     database. Synchronization must be done via celery job. See sync of
     Location implementation as reference. Tests for poster sync are already
     created in it_sync_tables_test.py
"""

class SyncedTable:

    def __init__(self, table, poster_sync, db_session):
        self.poster_sync = poster_sync
        self.db_session = db_session
        self.table = table

    def sync(self):
        poster_tables = self.poster_sync.tables()
        db_table = self.db_session.query(Table).get(self.table.id)
        for poster_table in poster_tables:
            if poster_table["id"] == db_table.id:
                db_table.name = poster_table["name"]
                db_table.floor_id = poster_table["floor_id"]
                db_table.x = poster_table["x"]
                db_table.y = poster_table["y"]
                db_table.width = poster_table["width"]
                db_table.height = poster_table["height"]
                db_table.status = poster_table["status"]
                db_table.max_capacity = poster_table["max_capacity"]
                db_table.multiple = poster_table["multiple"]
                db_table.playstation = poster_table["playstation"]
                db_table.shape_id = poster_table["shape_id"]
                db_table.min_capacity = poster_table["min_capacity"]
                db_table.deposit_hour = poster_table["deposit_hour"]
                self.db_session.commit()
