"""
   Abstractions for Item objects
"""


class ItemAbstraction:
    """ An item abstraction """
    id = None
    name = None
    stock_date = None
    comment = None
    company_id = None
    created_on = None
    updated_on = None
    company = None
    employee_id = None
    empolyee = None
    history = None


class ItemsAbstractions:
    """An Items abstraction"""

    def get(self, item_id):
        """Get the item with item_id"""
        raise Exception("Abstractions methods sould not be called")

    def list(self, **conditions):
        """List the items with the conditions"""
        raise Exception("Abstractions methods sould not be called")

    def create(self, item):
        """Create the item in database"""
        raise Exception("Abstractions methods sould not be called")

    def edit(self, item):
        """Edit the item in database"""
        raise Exception("Abstractions methods sould not be called")

    def delete(self, item):
        """Delete the item in database"""
        raise Exception("Abstractions methods sould not be called")
