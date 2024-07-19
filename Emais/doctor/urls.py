from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
#from django.contrib.auth.views import LoginView, LogoutView

app_name="doctor"

urlpatterns = [
    path('myinfo/', doctor_myinfo, name='myinfo'),
    path('mypatients/', doctor_mypatients, name='mypatients'),

    path('complete_appointment/<int:appointment_id>/', complete_appointment, name='complete_appointment'),
    path('view_medical_records/<int:patient_id>/', view_medical_records, name='view_medical_records'),

    path('export_medical_record_pdf/<int:record_id>/', export_medical_record_pdf, name='export_medical_record_pdf'),
    path('export_medical_record_doc/<int:record_id>/', export_medical_record_doc, name='export_medical_record_doc'),
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)