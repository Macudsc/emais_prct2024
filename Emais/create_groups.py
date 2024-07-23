import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Emais.settings')
django.setup()

from django.contrib.auth.models import Group

groups = ['patient', 'doctor', 'administrator']

for group_name in groups:
    Group.objects.get_or_create(name=group_name)
