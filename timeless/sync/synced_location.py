from timeless.restaurants.models import Location

"""
    Location synced to database.
    @todo #225:30min Use celery instead jobs cron-based jobs. Celery is already 
     being used to sync customers with postes; let's configure it and make a 
     job to run locations sync too.  
"""


class SyncedLocation:

    def __init__(self, location, poster_sync, db_session):
        self.poster_sync = poster_sync
        self.db_session = db_session
        self.location = location

    def sync(self):
        locations = self.poster_sync.locations()
        location = self.db_session.query(Location).get(self.location.id)
        for loc in locations:
            if loc["id"] == location.id:
                location.name = loc["name"],
                location.code = loc["code"],
                location.company_id = loc["company_id"],
                location.country = loc["country"],
                location.region = loc["region"],
                location.city = loc["city"],
                location.address = loc["address"],
                location.longitude = loc["longitude"],
                location.latitude = loc["latitude"],
                location.type = loc["type"],
                location.status = loc["status"],
                location.comment = loc["comment"]
                self.db_session.commit()
