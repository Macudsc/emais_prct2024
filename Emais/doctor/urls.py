from django.urls import path
from .views import *

app_name="doctor"

urlpatterns = [
    path('myinfo/', doctor_myinfo, name='myinfo'),
    path('mypatients/', doctor_mypatients, name='mypatients'),
    path('complete_appointment/<int:appointment_id>/', complete_appointment, name='complete_appointment'),
    path('export_medical_record_pdf/<int:record_id>/', export_medical_record_pdf, name='export_medical_record_pdf'),
    path('export_medical_record_doc/<int:record_id>/', export_medical_record_doc, name='export_medical_record_doc'),
    path('view_medical_records/<int:patient_id>/', view_medical_records, name='view_medical_records'),
    path('load_image/<str:image_id>/', load_image, name='load_image'),
]