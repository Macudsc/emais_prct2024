from django.urls import path
from .views import *
#from django.contrib.auth.views import LoginView, LogoutView

app_name="administrator"

urlpatterns = [
    path('myinfo/', administrator_myinfo, name='myinfo'),
    path('myusers/', administrator_myusers, name='myusers'),
    path('edit_user/<int:user_id>/', edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
]