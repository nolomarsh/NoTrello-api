from django.urls import path 
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/card/<int:pk>', views.CardDetail.as_view(), name='card_detail'),
    path('api/card', views.CardList.as_view(), name='card_list'),
    path('api/list', views.List_list.as_view(), name='list'),
    path('api/list/<int:pk>', views.List_Detail.as_view(), name='list_detail'),
    path('api/useraccount', views.UserAccountList.as_view(), name='useraccount_list'),
    path('api/useraccount/<int:pk>', views.UserAccountDetail.as_view(), name='useraccount_detail'),
    # api/useraccount/login will be routed to the check_login function for auth
    path('api/useraccount/login', csrf_exempt(views.check_login), name="check_login") 
]


