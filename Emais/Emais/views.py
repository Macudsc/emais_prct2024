from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import Group

def bare(request):
    user = request.user
    groups = user.groups.all()  # Получаем все группы, к которым принадлежит пользователь
    return render(request, 'Emais/bare.html', {'user': user, 'groups': groups})
    #return render(request, 'Emais/bare.html')

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

@login_required
def redirect_after_login(request):
    if request.user.is_superuser:
        return redirect('/admin/')
    elif request.user.groups.filter(name='patient').exists():
        return redirect('patient:myinfo')
    elif request.user.groups.filter(name='doctor').exists():
        return redirect('doctor:myinfo')
    elif request.user.groups.filter(name='administrator').exists():
        return redirect('administrator:myinfo')
    else:
        return redirect('core:home')  # на случай, если у пользователя нет группы