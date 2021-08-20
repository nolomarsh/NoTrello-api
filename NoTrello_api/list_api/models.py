from django.db import models

# Create your models here.

class List(models.Model):
    title = models.CharField(max_length=155)
    description = models.CharField(max_length=320)    

class Card(models.Model):
    name = models.CharField(max_length=155)
    body = models.CharField(max_length=320)
    labels = models.CharField(max_length=155)
    image = models.URLField()
    status = models.BooleanField()
    list = models.ForeignKey(List, on_delete=models.CASCADE, null=True,)

