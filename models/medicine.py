from main import db

class Medicine(db.Model):
    __tablename__ = 'medicines'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100))
    price = db.Column(db.Float)
    expiry_date = db.Column(db.String(50))

    def __repr__(self):
        return f"<Medicine {self.name}>"