from django import forms
from .models import DoctorProfile

class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = ['first_name', 'last_name', 'patronymic', 'specialization', 'hospital_address', 'contact_number', 'email']
