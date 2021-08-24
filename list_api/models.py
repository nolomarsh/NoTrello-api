from django.db import models

# Create your models here.

class List(models.Model):
    title = models.CharField(max_length=155, blank=True)
    description = models.CharField(max_length=320, blank=True,)    

class Card(models.Model):
    name = models.CharField(max_length=155, blank=True, )
    body = models.CharField(max_length=320, blank=True, )
    labels = models.CharField(max_length=155, blank=True,)
    image = models.URLField(blank=True, )
    status = models.BooleanField(blank=True,)
    list = models.ForeignKey(List, on_delete=models.CASCADE, null=True,)

class UserAccount(models.Model):
    username = models.CharField(max_length=75, unique=True)
    password = models.CharField(max_length=1000)

entry_list = list(UserAccount.objects.all())
