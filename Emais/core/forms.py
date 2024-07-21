from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.forms import AuthenticationForm

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class":"shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline", 'placeholder': "mail@mail.com"}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline", 'placeholder': "Введите имя пользователя"}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class":"shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline", 'placeholder': "Введите пароль"}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class":"shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline", 'placeholder': "Повторите пароль"}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        errors = []
        if len(password) <= 7:
            errors.append("более 7 символов")
        if not re.search(r'[A-Za-z]', password):
            errors.append("хотя бы одну букву")
        if not re.search(r'[0-9]', password):
            errors.append("хотя бы одну цифру")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            errors.append("хотя бы один специальный символ")
        if errors:
            raise ValidationError(f"Пароль должен содержать {', '.join(errors)}.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают.")

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': 'Введите имя пользователя',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'placeholder': 'Введите пароль',
        })
    )