from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from core.decorators import group_required
from django.shortcuts import render, redirect
from .models import AdministratorProfile
#from .forms import AdministratorProfileForm

from django.shortcuts import get_object_or_404, redirect, render
#from django.contrib.auth.decorators import login_required
from django.urls import reverse

from administrator.forms import AdministratorProfileForm
from doctor.forms import DoctorProfileForm
from patient.forms import PatientProfileForm

#from administrator.models import AdministratorProfile
from doctor.models import DoctorProfile
from patient.models import PatientProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test

from django.contrib.auth.models import User
from django.db.models import F, Case, When, Value, CharField

#from django.contrib.auth.models import User
#from django.db.models import F, Case, When, Value, CharField

@login_required
@group_required('administrator')
def administrator_myinfo(request):
    user = request.user
    profile, created = AdministratorProfile.objects.get_or_create(user=user)  #профиль
    if request.method == 'POST':
        form = AdministratorProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('administrator:myinfo')
    else:
        form = AdministratorProfileForm(instance=profile)
    groups = user.groups.all()
    return render(request, 'administrator/myinfo.html', {'user': user, 'groups': groups, 'form': form, 'profile': profile})

# Подгрузка данных из БД
@login_required
@group_required('administrator')
def administrator_myusers(request):
    sort_by = request.GET.get('sort_by', 'id')
    sort_order = request.GET.get('sort_order', 'asc')

    if request.GET.get('clear_sort'):
        sort_by = 'id'
        sort_order = 'asc'

    if sort_by not in ['username', 'role', 'id']:
        sort_by = 'id'
    if sort_order == 'desc':
        sort_order = '-'
    else:
        sort_order = ''

    users = User.objects.filter(groups__name__in=['doctor', 'patient']).distinct()

    if sort_by == 'role':
        users = users.annotate(role=Case(
            When(groups__name='doctor', then=Value('doctor')),
            When(groups__name='patient', then=Value('patient')),
            output_field=CharField()
        )).order_by(f'{sort_order}role')
    else:
        users = users.order_by(f'{sort_order}{sort_by}')

    user = request.user
    groups = user.groups.all()

    context2 = {
        'users': users,
        'current_sort': sort_by,
        'current_order': sort_order.strip('-'),
        'user': user,
        'groups': groups,
    }
    return render(request, 'administrator/myusers.html', context=context2)


@login_required
@group_required('administrator')
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if user.groups.filter(name='doctor').exists():
        profile = get_object_or_404(DoctorProfile, user=user)
        form_class = DoctorProfileForm
    elif user.groups.filter(name='patient').exists():
        profile = get_object_or_404(PatientProfile, user=user)
        form_class = PatientProfileForm
    else:
        profile = get_object_or_404(AdministratorProfile, user=user)
        form_class = AdministratorProfileForm

    if request.method == 'POST':
        form = form_class(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('administrator:myusers')
    else:
        form = form_class(instance=profile)
    
    return render(request, 'administrator/edit_user.html', {'form': form, 'user': user})

@login_required
@group_required('administrator')
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.delete()
        return redirect('administrator:myusers')

    return render(request, 'administrator/confirm_delete_user.html', {'user': user})