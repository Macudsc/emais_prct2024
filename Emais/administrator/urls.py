from django.urls import path
from .views import *
#from django.contrib.auth.views import LoginView, LogoutView

app_name="administrator"

urlpatterns = [
    path('myinfo/', administrator_myinfo, name='myinfo'),
    path('myusers/', administrator_myusers, name='myusers'),
]