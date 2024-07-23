import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Emais.settings')
django.setup()

from django.contrib.auth.models import User, Group
from patient.models import PatientProfile
from doctor.models import DoctorProfile
from administrator.models import AdministratorProfile

# Создать пользователей
users_data = [
    {'username': 'doctor1', 'password': '1234', 'group': 'doctor'},
    {'username': 'doctor2', 'password': '1234', 'group': 'doctor'},
    {'username': 'administrator1', 'password': '1234', 'group': 'administrator'},
    {'username': 'administrator2', 'password': '1234', 'group': 'administrator'},
]

for user_data in users_data:
    user, created = User.objects.get_or_create(username=user_data['username'])
    if created:
        user.set_password(user_data['password'])
        user.save()
        group = Group.objects.get(name=user_data['group'])
        user.groups.add(group)

        # Создание профиля пользователя
        if user_data['group'] == 'doctor':
            DoctorProfile.objects.create(user=user)
        elif user_data['group'] == 'administrator':
            AdministratorProfile.objects.create(user=user)
    else:
        print(f"User {user_data['username']} already exists")
