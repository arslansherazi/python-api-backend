from sqlalchemy import ForeignKey

from app import db


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(256))
    last_name = db.Column(db.String(256))
    cnic_no = db.Column(db.BigInteger)


class CustomerTranslations(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(256))
    phone_no = db.Column(db.BigInteger)

    # one-one relationship
    customer_id = db.Column(db.Integer, ForeignKey('customer.id'), nullable=False)


class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(256))
    last_name = db.Column(db.String(256))
    cnic_no = db.Column(db.BigInteger)
    phone_no = db.Column(db.BigInteger)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256))
    category = db.Column(db.String(256))
    orders = db.relationship('Order', backref='item', lazy=True)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # one-many relationship
    customer_id = db.Column(db.Integer, ForeignKey('customer.id'), nullable=False)
    item_id = db.Column(db.Integer, ForeignKey('item.id'), nullable=False)


# many-many relationship
tags = db.Table('item_supplier',
    db.Column('item_id', db.Integer, ForeignKey('item.id'), primary_key=True),
    db.Column('supplier_id', db.Integer, ForeignKey('supplier.id'), primary_key=True)
)
