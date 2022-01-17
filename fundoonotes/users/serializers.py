from rest_framework import serializers
from .models import User
from django import forms


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True,max_length=100)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=20)
    email = serializers.CharField(max_length=60)
    age = serializers.IntegerField()
    mobile = serializers.CharField(required=False, max_length=10)

    def create(self, validate_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create_user(**validate_data)

    def update(self, instance, data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.username = data.get('username', instance.username)
        instance.first_name = data.get('first_name', instance.first_name)
        instance.last_name = data.get('last_name', instance.last_name)
        instance.password = data.get('password', instance.password)
        instance.email = data.get('email', instance.email)
        instance.age = data.get('age', instance.age)
        instance.mobile = data.get('mobile', instance.mobile)
        instance.save()
        return instance
