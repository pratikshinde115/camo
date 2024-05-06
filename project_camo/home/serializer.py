from rest_framework import serializers
from .models import Contact
class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'subject', 'email' , 'message']