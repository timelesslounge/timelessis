from timeless.restaurants.models import Location

"""
    Syncs Poster with database.
    @todo #88:30min Implement synchronization between Poster and Databse for
     Locations. Data coming from Poster has priority upon data stored in our
     database. Create integration tests for database layer executing
     sync_location passing an database backed company object. Suggestion:
     start by creating structure for integration tests with database
    @todo #24:30min Implement synchronization between Poster and Database for
     Tables. Data coming from Poster has priority upon data stored in our
     database. Do not forget to create periodic script and
     put int into scripts folder to make this sync periodically.
"""


class PosterSync():
    def sync_location(poster, company):
        synced = []
        for location in company.locations:
            for poster_location in poster.locations():
                if location.id == poster_location["id"]:
                    synced.append(
                        Location(
                            id=location.id,
                            name=poster_location["name"],
                            code=poster_location["code"],
                            company_id=location.company_id,
                            country=poster_location["country"],
                            region=poster_location["region"],
                            city=poster_location["city"],
                            address=poster_location["address"],
                            longitude=poster_location["longitude"],
                            latitude=poster_location["latitude"],
                            type=poster_location["type"],
                            status=poster_location["status"],
                            comment=poster_location["comment"]
                        )
                    )
        company.locations = synced
