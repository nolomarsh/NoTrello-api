from rest_framework import serializers
from .models import List, Card, UserAccount
# Allows users to create and check passwords
from django.contrib.auth.hashers import make_password, check_password

class ListSerializer(serializers.ModelSerializer): 
    class Meta:
        model = List
        fields = ('id','title', 'description',)

class CardSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Card
        fields = ('id','name', 'body', 'labels', 'image', 'status', 'list',)

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id', 'username', 'password')

    #hashes pw when they create an account
    def create(self, validated_data):
        user = UserAccount.objects.create(
            username=validated_data['username'],
            password = make_password(validated_data['password'])
        )
        user.save()
        return user

    #this makes sure pw's are hashed
    def update(self, instance, validated_data):
        user = UserAccount.objects.get(username=validated_data["username"])
        user.password = check_password(validated_data["password"])
        user.save()
        return user
