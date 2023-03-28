from rest_framework import serializers


class DeleteOrderSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
