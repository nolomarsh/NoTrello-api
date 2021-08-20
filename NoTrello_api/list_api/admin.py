from django.contrib import admin

# Register your models here.
from .models import Card
from .models import List
admin.site.register(List)
admin.site.register(Card)
