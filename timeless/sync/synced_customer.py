from timeless.customers.models import Customer

"""
    Customer synced to database.
    
    @todo #225:30min Implement synchronization between Poster and Database for 
     Customers. Synchronization must be done via celery job. Create tests for 
     poster Customer retrieval, Customer storage in database and the sync 
     between the two. See sync of Location implementation as reference. Don't 
     forget to cover all code added with tests.
"""


class SyncedCustomer:

    def __init__(self, poster_sync, customer):
        pass

    def sync(self):
        raise Exception("sync for customer not implemented yet")
