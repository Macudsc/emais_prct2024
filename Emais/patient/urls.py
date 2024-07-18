from django.urls import path
#from .views import register
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

app_name="patient"

urlpatterns = [
    path('register/', register, name='register'),
    

    path('login/', LoginView.as_view(template_name='patient/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='patient/logout.html'), name="logout"),

    #profile
    path('myinfo/',patient_myinfo, name="myinfo"),
]