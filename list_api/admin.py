from django.contrib import admin

# Register your models here.
from .models import Card
from .models import List
from .models import UserAccount
admin.site.register(List)
admin.site.register(Card)
admin.site.register(UserAccount)
