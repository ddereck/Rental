from rest_framework import serializers
from .models import Users, Drivers


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class UsersSerializerAdd(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drivers
        fields = '__all__'