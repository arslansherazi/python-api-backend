from app import db


class Student(db.Model):
    username = db.Column(db.String(256), primary_key=True)
    password = db.Column(db.String(256))
    name = db.Column(db.String(256))
    degree = db.Column(db.String(256))
    cgpa = db.Column(db.String(256))

    def __init__(self, username, password, name, degree, cgpa):
        self.username = username
        self.password = password
        self.name = name
        self.degree = degree
        self.cgpa = cgpa