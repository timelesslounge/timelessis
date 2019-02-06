from timeless.restaurants.models import Location
"""
    Syncs Poster with database.
    @todo #88:30min Implement synchronization between Poster and Databse for
     Locations. Data coming from Poster has priority upon data stored in our
     database. Create integration tests for database layer executing 
     sync_location passing an database backed company object. Suggestion: 
     start by creating structure for integration tests with database

"""
class PosterSync():

    def sync_location(poster, company):
        synced =[]
        for location in company.locations:
            for loc in poster.locations():
                if location.id == loc["id"]:
                    synced.append(
                        Location(
                            id=location.id,
                            name=loc["name"],
                            code=loc["code"],
                            company_id=location.company_id,
                            country=loc["country"],
                            region=loc["region"],
                            city=loc["city"],
                            address=loc["address"],
                            longitude=loc["longitude"],
                            latitude=loc["latitude"],
                            type=loc["type"],
                            status=loc["status"],
                            comment=loc["comment"]
                        )
                    )
        company.locations = synced
