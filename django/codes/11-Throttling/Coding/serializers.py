from rest_framework import serializers

from Coding.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('username', 'password', 'name', 'email', 'subscription', 'is_active')