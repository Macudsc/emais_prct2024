from django.contrib import admin

# Register your models here.
from .models import PatientMyInfo#, PatientProfile

admin.site.register(PatientMyInfo)
#admin.site.register(PatientProfile)