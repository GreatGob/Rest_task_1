from rest_framework import serializers
from .models import Company, Employee, Detail


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields= ['id', 'name', 'created']

    def create(self, validated_data):
        return Company.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.created = validated_data.get('created', instance.created) 
        instance.save()
        return instance

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields= ['id', 'username', 'is_active']

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.is_active = validated_data.get('is_active', False) 
        instance.save()
        return instance

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields= ['first_name', 'last_name', 'birthday', 'joined', 'rank', 'phone']
    
    def create(self, validated_data):
        return Detail.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.joined = validated_data.get('joined', instance.joined if instance.joined else None)
        instance.rank = validated_data.get('rank', instance.rank)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()
        return instance