from django.urls import path
#from .views import register
#from .views import *
from . import views
#from django.contrib.auth.views import LoginView, LogoutView

app_name="patient"

urlpatterns = [
    #profile
    path('myinfo/', views.patient_myinfo, name="myinfo"),
    path('myrecords/', views.patient_myrecords, name='myrecords'),
    path('mymedicalcard/', views.patient_mymedicalcard, name='mymedicalcard'),

    path('new_appointment/', views.new_appointment, name='new_appointment'),
    path('get_doctors/', views.get_doctors, name='get_doctors'),
    path('get_available_times/', views.get_available_times, name='get_available_times'),

    path('export_medical_record_pdf/<int:record_id>/', views.export_medical_record_pdf, name='export_medical_record_pdf'),
    path('export_medical_record_doc/<int:record_id>/', views.export_medical_record_doc, name='export_medical_record_doc'),

    path('load_image/<str:image_id>/', views.load_image, name='load_image'),

    path('delete_appointment/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
]
