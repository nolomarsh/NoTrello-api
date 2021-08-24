from django.db.models.query import QuerySet
from rest_framework import generics
from .serializers import CardSerializer, ListSerializer, UserAccountSerializer
from .models import Card, List, UserAccount


#Allows user to create and check pw
from django.contrib.auth.hashers import make_password, check_password
#Sends JSON as a response
from django.http import JsonResponse
#allows you to dictionaries into JSON
import json
# Create your views here.


class UserAccountList(generics.ListCreateAPIView):
    queryset = UserAccount.objects.all().order_by('id')
    serializer_class = UserAccountSerializer

class UserAccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAccount.objects.all().order_by('id')
    serializer_class = UserAccountSerializer

#function that performs the auth
def check_login(request):
    #if a get request is made return and empty {}
    if request.method =='GET':
        return JsonResponse({})
    #check for put
    if request.method =='PUT':
        #make the request JSON format
        jsonRequest = json.loads(request.body)
        username = jsonRequest['username']
        password = jsonRequest['password']
        #see if username exists in DB
        if UserAccount.objects.filter(username=username):
            user = UserAccount.objects.get(username=username)
            if check_password(password, user.password):
                return JsonResponse({'id':user.id, 'username': user.username})
            else: 
                return JsonResponse({'error': 'wrong password'})
        else:
            return JsonResponse({'error': 'username does not exist'})
    if request.method == 'DELETE':
        return JsonResponse({})

class List_list(generics.ListCreateAPIView):
    queryset = List.objects.all().order_by('id')
    serializer_class = ListSerializer

class List_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all().order_by('id')
    serializer_class = ListSerializer

class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all().order_by('id')
    serializer_class = CardSerializer

class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all().order_by('id')
    serializer_class = CardSerializer

