from django.contrib import admin
from django.urls import path, include
#from rest_framework.routers import DefaultRouter
#from core.views import UserViewSet, AppointmentViewSet, MedicalRecordViewSet
from django.conf.urls.static import static
from django.conf import settings
from .views import bare, redirect_after_login

#router = DefaultRouter()
#router.register(r'users', UserViewSet)
#router.register(r'appointments', AppointmentViewSet)
#router.register(r'medical_records', MedicalRecordViewSet)

#from core.views import export_records_csv, export_records_pdf, home, patient_page, doctor_page, admin_page, items
#from core.views import *

urlpatterns = [
    path('', bare, name="bare"), # Корневой URL
    #ковринок
    path('admin/', admin.site.urls, name="admin"),
    path("core/", include("core.urls", namespace="core")),
    path("patient/", include("patient.urls", namespace="patient")),
    path('doctor/', include('doctor.urls', namespace="doctor")),
    path('administrator/', include('administrator.urls', namespace="administrator")),
    path('redirect_after_login/', redirect_after_login, name='redirect_after_login'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)