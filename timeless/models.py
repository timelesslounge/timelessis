"""File for all models in Timeless"""

from timeless import DB

class Company(DB.Model):
    """"Model for company business entity"""
    __tablename__ = 'companies'

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)

    def __init__(self, id):
        """Initialization method"""
        self.id = id
