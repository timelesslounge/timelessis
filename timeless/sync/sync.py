from timeless.restaurants.models import Location
"""
    Syncs Poster with database.

"""


class PosterSync:

    def sync_location(poster, company):
        synced =[]
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
