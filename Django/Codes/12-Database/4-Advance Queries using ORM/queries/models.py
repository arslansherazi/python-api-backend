from django.db import models


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    cnic_no = models.BigIntegerField()

    class Meta:
        db_table = 'customer'


class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    cnic_no = models.BigIntegerField()
    address = models.CharField(max_length=255)
    phone_no = models.BigIntegerField()

    class Meta:
        db_table = 'supplier'


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.IntegerField()
    supplier = models.ManyToManyField(Supplier)

    class Meta:
        db_table = 'item'


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        db_table = 'order'


# this model is used for self join
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    contact_no = models.BigIntegerField()
    manager = models.ForeignKey('self', on_delete=models.CASCADE)

    class Meta:
        db_table = 'employee'