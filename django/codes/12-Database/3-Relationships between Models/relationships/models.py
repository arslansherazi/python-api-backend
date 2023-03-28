from django.db import models


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    cnic_no = models.BigIntegerField()

    class Meta:
        db_table = 'customer'


class CustomerTranslations(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.TextField()
    phone_no = models.BigIntegerField()
    # one-one relationship
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)

    class Meta:
        db_table = 'customer_translations'


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
    # many-many relationship
    supplier = models.ManyToManyField(Supplier)

    class Meta:
        db_table = 'item'


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    # one-many relationship
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        db_table = 'order'
