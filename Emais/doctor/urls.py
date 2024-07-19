from django.urls import path
from .views import *
#from django.contrib.auth.views import LoginView, LogoutView

app_name="doctor"

urlpatterns = [
    path('myinfo/', doctor_myinfo, name='myinfo'),
    path('mypatients/', doctor_mypatients, name='mypatients'),
]