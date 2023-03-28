from app import db


class Student(db.Model):
    roll_no = db.Column(db.String(256), primary_key=True)
    name = db.Column(db.String(256))
    degree = db.Column(db.String(256))
    cgpa = db.Column(db.String(256))
