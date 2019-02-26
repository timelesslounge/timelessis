class TableMock:
    """Table mock"""

    query = None

    def __init__(self, **kwargs):
        self.tables = kwargs.get("tables", [])
        self.query = TableQuery(tables=self.tables)


class TableQuery:
    """ Mocking for query object of Model """

    tables = None

    def __init__(self, **kwargs):
        self.tables = kwargs.get("tables", [])

    def all(self):
        return self.tables
