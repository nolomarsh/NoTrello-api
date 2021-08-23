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


#get api/useraccount will return all users 
    #post will add new user to the db
    #requires an email an email and password field 
    #email must be unique
    #pw will be hashed using bcrypt prior to being stored in db
    #if username already exist an array is returned 
        #username: [0]
#get api/useraccount/id will return a single user
    #put will update a single user - password revisions will be hashed prior to being put in the db
    #both email and pw must be sent in request
    #delete will delete one user
#get api/useraccount/login that will return an empty object
    #put will find a user in the db by their email and compare their hashed pw to pw in the request
    #if match a user obj will be returned that contains the user email and id but not the pw
    #if they do not match an empty obj will be returned 
    #if user email does not exist in the db and empty obj will be returned