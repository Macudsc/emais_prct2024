from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.decorators import group_required
from django.contrib.auth.models import Group

@login_required
@group_required('patient')
def patient_myinfo(request):
    user = request.user
    groups = user.groups.all()  # Получаем все группы, к которым принадлежит пользователь
    return render(request, 'patient/myinfo.html', {'user': user, 'groups': groups})

@login_required
@group_required('patient')
def patient_myrecords(request):
    return render(request, 'patient/myrecords.html')

@login_required
@group_required('patient')
def patient_mymdeicalcard(request):
    return render(request, 'patient/mymedicalcard.html')
