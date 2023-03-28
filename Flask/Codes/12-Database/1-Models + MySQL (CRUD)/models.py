from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(256), unique=True, nullable=False)
    name = db.Column(db.String(256))
    author = db.Column(db.String(256))
    price = db.Column(db.Float)
    is_available = db.Column(db.Boolean)
