from rest_framework import serializers

from apis.models import Student


class StudentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    degree = serializers.CharField(required=True)
    cgpa = serializers.FloatField(required=True)

    class Meta:
        model = Student
        fields = ("username", "password", "name", "degree", "cgpa")


class UsernameSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
