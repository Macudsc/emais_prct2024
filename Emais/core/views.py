#from rest_framework import viewsets
#from .models import User, Appointment, MedicalRecord
#from .serializers import UserSerializer, AppointmentSerializer, MedicalRecordSerializer

#import pandas as pd
#from django.http import HttpResponse

from django.conf import settings
from django.shortcuts import render, redirect
from .models import Product, User
from django.contrib.auth.decorators import login_required

#class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer

#class AppointmentViewSet(viewsets.ModelViewSet):
#    queryset = Appointment.objects.all()
#    serializer_class = AppointmentSerializer

#class MedicalRecordViewSet(viewsets.ModelViewSet):
#    queryset = MedicalRecord.objects.all()
#    serializer_class = MedicalRecordSerializer

# основные функции
def export_records_csv(request):
    #records = MedicalRecord.objects.all().values()
    #df = pd.DataFrame(records)
    #response = HttpResponse(content_type='text/csv')
    #response['Content-Disposition'] = 'attachment; filename="medical_records.csv"'
    #df.to_csv(path_or_buf=response, index=False)
    #return response
    pass

def export_records_pdf(request):
    # добавить экспорт в PDF с ReportLab
    pass

def home(request):
    return render(request, 'core/home.html')

@login_required
def doctor_page(request):
    return render(request, 'core/Doctor.html')

# Подгрузка данных из БД
@login_required
def admin_page(request):
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
    
    context2 = {
        'users': users,
        'current_sort': request.GET.get('sort_by', 'id'),
        'current_order': request.GET.get('sort_order', 'asc')
    }
    return render(request, 'core/Administrator.html', context=context2)



# тестовые функции
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

def add_item(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES['upload']
        item=Product(name=name, price=price, description=description, image=image)
        item.save()
    return render(request, 'core/additem.html',)