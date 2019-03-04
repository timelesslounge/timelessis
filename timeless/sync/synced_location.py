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
        poster_locations = self.poster_sync.locations()
        db_location = self.db_session.query(Location).get(self.location.id)
        for poster_location in poster_locations:
            if poster_location["id"] == db_location.id:
                db_location.name = poster_location["name"]
                db_location.code = poster_location["code"]
                db_location.company_id = poster_location["company_id"]
                db_location.country = poster_location["country"]
                db_location.region = poster_location["region"]
                db_location.city = poster_location["city"]
                db_location.address = poster_location["address"]
                db_location.longitude = poster_location["longitude"]
                db_location.latitude = poster_location["latitude"]
                db_location.type = poster_location["type"]
                db_location.status = poster_location["status"]
                db_location.comment = poster_location["comment"]
                self.db_session.commit()
