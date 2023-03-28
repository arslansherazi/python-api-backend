from app import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(256), unique=True, nullable=False)
    name = db.Column(db.String(256))
    degree = db.Column(db.String(256))
    cgpa = db.Column(db.Float)
