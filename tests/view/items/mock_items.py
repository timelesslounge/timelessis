from timeless.items.abstractions import ItemAbstraction, ItemsAbstractions


class ItemMock(ItemAbstraction):
    """Item mock"""

    items = None
    query = None

    def __init__(self, **kwargs):
        self.items = kwargs.get("items", [])
        self.query = ItemQuery(items=self.items)


class ItemQuery:
    """ Mocking for query object of Model """

    items = None

    def __init__(self, **kwargs):
        self.items = kwargs.get("items", [])

    def all(self):
        return self.items
