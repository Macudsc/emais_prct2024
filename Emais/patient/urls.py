from django.urls import path
#from .views import register
from .views import *

app_name="patient"

urlpatterns = [
    path('register/', register, name='register'),
    path('myinfo/',patient_page, name="myinfo"),
]