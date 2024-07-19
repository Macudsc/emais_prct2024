from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.decorators import group_required

@login_required
@group_required('doctor')
def doctor_myinfo(request):
    #return render(request, 'doctor/myinfo.html')
    user = request.user
    groups = user.groups.all()  # Получаем все группы, к которым принадлежит пользователь
    return render(request, 'doctor/myinfo.html', {'user': user, 'groups': groups})

@login_required
@group_required('doctor')
def doctor_mypatients(request):
    return render(request, 'doctor/mypatients.html')