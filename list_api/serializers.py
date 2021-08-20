from rest_framework import serializers
from .models import List, Card
class ListSerializer(serializers.ModelSerializer): 
    class Meta:
        model = List
        fields = ('id','title', 'description',)

class CardSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Card
        fields = ('id','name', 'body', 'labels', 'image', 'status', 'list',)

