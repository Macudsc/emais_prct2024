from django.contrib import admin

# Register your models here.
from .models import Appointment, MedicalRecord

#admin.site.register(PatientProfile)
admin.site.register(MedicalRecord)
admin.site.register(Appointment)