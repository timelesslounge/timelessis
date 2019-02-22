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

    def get(self, user_id):
        """Get the user with user_id"""
        raise Exception("Abstractions methods sould not be called")

    def list(self, **conditions):
        """List the users with the conditions"""
        raise Exception("Abstractions methods sould not be called")

    def create(self, user):
        """Create the user in database"""
        raise Exception("Abstractions methods sould not be called")

    def edit(self, user):
        """Edit the user in database"""
        raise Exception("Abstractions methods sould not be called")

    def delete(self, user):
        """Delete the user in database"""
        raise Exception("Abstractions methods sould not be called")
