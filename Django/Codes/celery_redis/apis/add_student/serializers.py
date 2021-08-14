from rest_framework import serializers

from models import Student


class StudentSerializer(serializers.ModelSerializer):
    # not included in Student model - used only for validation
    first_name = serializers.CharField(max_length=100, read_only=True)
    last_name = serializers.CharField(max_length=100, read_only=True)
    contact_no = serializers.CharField(max_length=256, read_only=True)
    address = serializers.CharField(max_length=50, read_only=True)

    class Meta:
        model = Student
        fields = ('roll_no', 'current_semester', 'session_start', 'session_end', 'first_name', 'last_name', 'address', 'contact_no')
