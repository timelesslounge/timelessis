
class FloorMock():
    """Floor mock"""

    query = None

    def __init__(self, **kwargs):
        self.floors = kwargs.get("floors", [])
        self.query = FloorQuery(floors=self.floors)


class FloorQuery:
    """ Mocking for query object of Model """

    floors = None

    def __init__(self, **kwargs):
        self.floors = kwargs.get("floors", [])

    def all(self):
        return self.floors
