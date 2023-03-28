from app import db


class Company(db.Model):
    username = db.Column(db.String(256), primary_key=True)
    password = db.Column(db.String(256))
    email = db.Column(db.String(256))
    name = db.Column(db.String(256))
    subscription = db.Column(db.Integer, default=1)
    is_active = db.Column(db.Boolean, default=True)

    def __init__(self, username, password, email, name, subscription, is_active):
        self.username = username
        self.password = password
        self.email = email
        self.name = name
        self.subscription = subscription
        self.is_active = is_active
