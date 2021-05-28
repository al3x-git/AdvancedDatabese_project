from django.urls import path,include
from django.conf.urls import url
from .views import *

app_name = 'myapp'

urlpatterns = [

    path('', HomePageView.as_view(), name='homepage'),
    path('test1', sformview, name='s_form'),
    path('signup/', signup, name='signup'),
    path('logout_view/', logout_view, name='logout_view'),
    path('login_user/', login_user, name='login_user'),
]
