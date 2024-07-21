from django.conf import settings
from django.shortcuts import render, redirect
from .models import Product, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import NewUserForm
from django.contrib.auth.models import User, Group
from patient.models import PatientProfile  # Импортируем модель профиля пациента
from core.decorators import group_required

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            patient_group = Group.objects.get(name='patient')
            user.groups.add(patient_group)

            PatientProfile.objects.create(user=user)  # Создаем профиль пациента

            login(request, user)
            return redirect('patient:myinfo')
    else:
        form = NewUserForm()
    context = {'form': form}
    return render(request, 'core/register.html', context)

def home(request):
    return render(request, 'core/home.html')

# тестовые функции
@login_required
@group_required('administrator')
def index(request):
    #item=['patient', 'doc', 'admini']
    items=Product.objects.all()
    context={
        'items':items,
    }
    return render(request, 'core/index.html', context)

def indexItem(request, my_id):
    #return HttpResponse("Your item id is: " + str(id))
    item=Product.objects.get(id=my_id)
    context={
        'item':item,
    }
    return render(request, 'core/detail.html', context=context)

@login_required
@group_required('administrator')
def add_item(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES['upload']
        seller = request.user
        item=Product(name=name, price=price, description=description, image=image, seller=seller)
        item.save()
    return render(request, 'core/additem.html',)