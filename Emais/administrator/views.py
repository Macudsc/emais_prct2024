from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from core.decorators import group_required

@login_required
@group_required('administrator')
def administrator_myinfo(request):
    #return render(request, 'administrator/myinfo.html')
    user = request.user
    groups = user.groups.all()  # Получаем все группы, к которым принадлежит пользователь
    return render(request, 'administrator/myinfo.html', {'user': user, 'groups': groups})

# Подгрузка данных из БД
@login_required
@group_required('administrator')
def administrator_myusers(request):
    sort_by = request.GET.get('sort_by', 'id')  # По умолчанию сортировка по ID
    sort_order = request.GET.get('sort_order', 'asc')

    if request.GET.get('clear_sort'):
        sort_by = 'id'
        sort_order = 'asc'
    else:
        if sort_by not in ['first_name', 'role', 'id']:
            sort_by = 'id'
        if sort_order == 'desc':
            sort_by = f'-{sort_by}'
    
    users = User.objects.all().order_by(sort_by)
    
    user = request.user
    groups = user.groups.all() 

    context2 = {
        'users': users,
        'current_sort': request.GET.get('sort_by', 'id'),
        'current_order': request.GET.get('sort_order', 'asc'),
        'user': user,
        'groups': groups,
    }
    return render(request, 'administrator/myusers.html', context=context2)