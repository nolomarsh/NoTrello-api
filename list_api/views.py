from django.db.models.query import QuerySet
from rest_framework import generics
from .serializers import CardSerializer, ListSerializer
from .models import Card, List

# Create your views here.
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
