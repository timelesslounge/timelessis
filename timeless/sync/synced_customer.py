from timeless.customers.models import Customer

"""
    Customer synced to database.
    
    @todo #262:30min Continue synchronization between Poster and Database for
     Customers. Create tests for poster Customer retrieval, Customer storage
     in database and the sync between the two.
"""


class SyncedCustomer:

    def __init__(self, poster_sync, customer):
        pass

    def sync(self):
        raise Exception("sync for customer not implemented yet")
