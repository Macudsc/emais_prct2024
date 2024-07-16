from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import UserViewSet, AppointmentViewSet, MedicalRecordViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'medical_records', MedicalRecordViewSet)

#from core.views import export_records_csv, export_records_pdf, home, patient_page, doctor_page, admin_page, items
from core.views import *
#from core import views

from testapp import views

app_name="Emais"

urlpatterns = [
    path('admin/', admin.site.urls),

    # Основные маршруты
    path('api/', include(router.urls)),
    path('export/csv/', export_records_csv),
    path('export/pdf/', export_records_pdf),
    path('', home, name='home'),  # Корневой URL
    path('patient/myinfo/',patient_page),
    path('doctor/mypatients/',doctor_page),
    path('administrator/myusers/',admin_page),

    # Тестовые маршруты
    path('hello/',views.index),
    #path('hello/', include("Emais.urls", namespace="Emais")),
    path('index/',index),
    path('<int:my_id>/',indexItem, name="detail"),
]
