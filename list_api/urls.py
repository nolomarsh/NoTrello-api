from django.urls import path 
from . import views

urlpatterns = [
    path('api/card', views.CardList.as_view(), name='card_list'),
    path('api/card/<int:pk>', views.CardDetail.as_view(), name='card_detail'),
    path('api/list', views.List_list.as_view(), name='list'),
    path('api/list/<int:pk>', views.List_Detail.as_view(), name='list_detail'),
]