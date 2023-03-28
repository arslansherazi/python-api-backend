from rest_framework import serializers

from Coding.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("username", "password", "name", "degree", "cgpa")