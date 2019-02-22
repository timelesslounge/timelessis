from timeless.items.abstractions import ItemAbstraction, ItemsAbstractions


class ItemsMock(ItemsAbstractions):
    """ Mock for Items """

    items = None

    def __int__(self, **kwargs):
        items = kwargs.get("items", [])

    def get(self, user_id):
        """Get the user with user_id"""
        raise Exception("get() not implemented")

    def list(self, **conditions):
        """List the users with the conditions"""
        return self.items

    def create(self, user):
        """Create the user in database"""
        raise Exception("create() not implemented")

    def edit(self, user):
        """Edit the user in database"""
        raise Exception("edit() not implemented")

    def delete(self, user):
        """Delete the user in database"""
        raise Exception("delete() not implemented")


class ItemMock(ItemAbstraction):
    """Item mock"""
