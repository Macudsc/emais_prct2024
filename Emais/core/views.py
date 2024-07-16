from rest_framework import viewsets
from .models import User, Appointment, MedicalRecord
from .serializers import UserSerializer, AppointmentSerializer, MedicalRecordSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer


import pandas as pd
from django.http import HttpResponse

def export_records_csv(request):
    records = MedicalRecord.objects.all().values()
    df = pd.DataFrame(records)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="medical_records.csv"'
    df.to_csv(path_or_buf=response, index=False)
    return response

def export_records_pdf(request):
    # добавить экспорт в PDF с ReportLab
    pass


from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, 'core/home.html')

def patient_page(request):
    return render(request, 'core/patient.html')

def doctor_page(request):
    return render(request, 'core/Doctor.html')

def admin_page(request):
    return render(request, 'core/Administrator.html')

def index(request):
    #item=['patient', 'doc', 'admini']
    items=Product.objects.all()
    context={
        'items':items,
    }
    return render(request, 'core/index.html', context)

def indexItem(request, id):
    return HttpResponse("Your item id is: " + str(id))

def contacts(request):
    return render(request, 'core/contacts.html')