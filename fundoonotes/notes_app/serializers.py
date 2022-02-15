from rest_framework import serializers
from .models import Notes


class NotesSerializer(serializers.ModelSerializer):
    """
       Description: This Class using for serializer
    """

    class Meta:
        model = Notes
        fields = '__all__'

    def create(self, validate_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return Notes.objects.create(**validate_data)
