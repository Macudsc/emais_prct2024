from django.urls import path
#from .views import register
from .views import *
#from django.contrib.auth.views import LoginView, LogoutView

app_name="patient"

urlpatterns = [
    
    #profile
    path('myinfo/', patient_myinfo, name="myinfo"),
    #path('sellerprofile/',patient_myinfo, name="sellerprofile"),
    path('myrecords/',patient_myrecords,name="myrecords"),
    path('mymedicalcard/',patient_mymdeicalcard,name="mymedicalcard"),
]