from django import forms
from .models import PatientProfile
from .models import Appointment

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ['first_name', 'last_name', 'patronymic', 'birthday', 'gender', 'address', 'contact_number', 'email']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time']