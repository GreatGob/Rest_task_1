
from rest_framework import serializers
from .models import Company, Employee, Detail


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields= ['id', 'name', 'created']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields= ['id', 'username', 'is_active']

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields= ['first_name', 'last_name', 'birthday', 'joined', 'rank', 'phone']