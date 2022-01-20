from rest_framework import serializers
from .models import Notes


class NotesSerializer(serializers.ModelSerializer):
    """
       Description: This Class using for serializer
    """
    class Meta:
        model = Notes
        fields = '__all__'
