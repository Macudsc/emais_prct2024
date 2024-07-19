from django import forms
from .models import AdministratorProfile

class AdministratorProfileForm(forms.ModelForm):
    class Meta:
        model = AdministratorProfile
        fields = ['contact_number', 'email']
