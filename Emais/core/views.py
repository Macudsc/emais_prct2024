#from rest_framework import viewsets
#from .models import User, Appointment, MedicalRecord
#from .serializers import UserSerializer, AppointmentSerializer, MedicalRecordSerializer

#import pandas as pd
#from django.http import HttpResponse

from django.conf import settings
from django.shortcuts import render, redirect
from .models import Product, User
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login
#from .models import PatientMyInfo
from .forms import NewUserForm
#from django.shortcuts import render, redirect
from django.contrib.auth.models import User

#class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer

#class AppointmentViewSet(viewsets.ModelViewSet):
#    queryset = Appointment.objects.all()
#    serializer_class = AppointmentSerializer

#class MedicalRecordViewSet(viewsets.ModelViewSet):
#    queryset = MedicalRecord.objects.all()
#    serializer_class = MedicalRecordSerializer

def register(request):
    if request.method == 'POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('core:index')
    form=NewUserForm()
    context={'form':form}
    return render(request, 'core/register.html', context)

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

@login_required
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