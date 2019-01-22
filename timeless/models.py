from timeless import db

class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    def __init__(self, id):
        self.id = id;
