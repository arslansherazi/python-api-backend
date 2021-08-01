import uuid

from django.db import models, transaction
from django.db.models.signals import pre_save, post_save, pre_init, post_init, pre_delete, post_delete


class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    item_code = models.CharField(max_length=50)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'inventory'
        app_label = 'apis'

    @classmethod
    def minus_item_quantity(cls, item_id, quantity):
        """
        Minus item quantity after order
        """
        inventory_item = cls.objects.get(id=item_id)
        inventory_item.quantity -= quantity
        inventory_item.save()


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_number = models.CharField(max_length=50)
    item = models.ForeignKey(Inventory, on_delete=models.CASCADE, db_index=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'order'
        app_label = 'apis'

    @classmethod
    def save_order_into_db(cls, item_id, quantity):
        """
        Saves order into db

        :param int item_id: item id
        :param int quantity: quantity
        """
        try:
            order = cls(order_number=str(uuid.uuid4()).split('-')[0], item_id=item_id, quantity=quantity)
            order.save()
            return True
        except Exception as e:
            return False

    @staticmethod
    def validate_order(sender, instance, **kwargs):
        """
        Validates order

        :param sender: sender
        :param instance: sender instance
        """
        if instance.quantity < instance.item.quantity:
            return
        raise

    @staticmethod
    def post_order(sender, instance, **kwargs):
        """
        Post order

        :param sender: sender
        :param instance: sender instance
        """
        Inventory.minus_item_quantity(instance.item.id, instance.quantity)

    @staticmethod
    def func_before_model_obj(sender, **kwargs):
        print('func before model obj')

    @staticmethod
    def func_after_model_obj(sender, instance, **kwargs):
        print('func after model obj')

    @classmethod
    def delete_order(cls, order_id):
        """
        Deletes order

        :param int order_id: order id
        """
        try:
            order = cls.objects.get(id=order_id)
            order.delete()
            return True
        except Exception:
            return False

    @staticmethod
    def func_before_deleting_model_obj(sender, **kwargs):
        print('func before deleting model obj')

    @staticmethod
    def func_after_deleting_model_obj(sender, instance, **kwargs):
        print('func after deleting model obj')


pre_init.connect(Order.func_before_model_obj, sender=Order)
post_init.connect(Order.func_after_model_obj, sender=Order)
pre_save.connect(Order.validate_order, sender=Order)
post_save.connect(Order.post_order, sender=Order)
pre_save.connect(Order.validate_order, sender=Order)
pre_delete.connect(Order.func_before_deleting_model_obj, sender=Order)
post_delete.connect(Order.func_after_deleting_model_obj, sender=Order)
