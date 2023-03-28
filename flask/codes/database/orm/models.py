from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

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
    customer_id = db.Column(db.Integer, ForeignKey('customer.id'), nullable=False)


class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(256))
    last_name = db.Column(db.String(256))
    cnic_no = db.Column(db.BigInteger)
    phone_no = db.Column(db.BigInteger)
    items = relationship('Item', secondary='item_supplier')


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256))
    category = db.Column(db.String(256))
    price = db.Column(db.Integer)
    suppliers = relationship('Supplier', secondary='item_supplier')


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, ForeignKey('customer.id'), nullable=False)
    item_id = db.Column(db.Integer, ForeignKey('item.id'), nullable=False)


class ItemSupplier(db.Model):
    __tablename__ = 'item_supplier'
    item_id = db.Column(db.Integer, ForeignKey('item.id'), primary_key=True)
    supplier_id = db.Column(db.Integer, ForeignKey('supplier.id'), primary_key=True)


# this model is used for self join
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    manager_id = db.Column(db.Integer)
    name = db.Column(db.String(256))
    department = db.Column(db.String(256))
    contact_no = db.Column(db.Integer)
