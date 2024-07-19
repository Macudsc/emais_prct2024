from .forms import DoctorProfileForm
from django.contrib.auth.models import User
import logging

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from core.decorators import group_required
from django.http import JsonResponse
from .models import DoctorProfile
from patient.models import Appointment, MedicalRecord

from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML

from django.conf import settings
from django.templatetags.static import static
from weasyprint import HTML, CSS

#from django.http import HttpResponse
from docx import Document
from docx.shared import Inches
import os
#from .models import MedicalRecord

logger = logging.getLogger(__name__)

#Моя информация
@login_required
@group_required('doctor')
def doctor_myinfo(request):
    user = request.user
    profile, created = DoctorProfile.objects.get_or_create(user=user)  # Получаем или создаем профиль
    if request.method == 'POST':
        form = DoctorProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('doctor:myinfo')
    else:
        form = DoctorProfileForm(instance=profile)
    groups = user.groups.all()
    return render(request, 'doctor/myinfo.html', {'user': user, 'groups': groups, 'form': form, 'profile': profile})

# Приём пациентов
@login_required
@group_required('doctor')
def doctor_mypatients(request):
    doctor = DoctorProfile.objects.get(user=request.user)
    appointments = Appointment.objects.filter(doctor=doctor)
    context = {
        'doctor': doctor,
        'appointments': appointments,
    }
    return render(request, 'doctor/mypatients.html', context)

# Заполнить исследование
@login_required
@group_required('doctor')
def complete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        description = request.POST.get('description')
        conclusion = request.POST.get('conclusion')
        image = request.FILES.get('upload')

        # Save image if provided
        if image:
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            image_url = fs.url(filename)
            logger.debug(f"Image saved at {image_url}")
        else:
            filename = None

        medical_record = MedicalRecord(
            patient=appointment.patient,
            doctor=appointment.doctor,
            appointment=appointment,
            description=description,
            conclusion=conclusion,
            image=filename  # сохраняем имя файла в БД
        )
        medical_record.save()
        appointment.delete() # ! ИГРУШКА ДЬЯВОЛА

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed', 'error': 'Invalid request method'})

# Просмотр медкарты
@login_required
@group_required('doctor')
def view_medical_records(request, patient_id):
    patient = get_object_or_404(User, id=patient_id)
    medical_records = MedicalRecord.objects.filter(patient=patient)
    context = {
        'patient': patient,
        'medical_records': medical_records,
    }
    return render(request, 'doctor/medical_records.html', context)

@login_required
@group_required('doctor')
def export_medical_record_pdf(request, record_id):
    record = get_object_or_404(MedicalRecord, id=record_id)
    html_string = render_to_string('patient/medical_record_pdf.html', {'record': record})
    html = HTML(string=html_string, base_url=request.build_absolute_uri('/'))
    
    # Get the correct path to the CSS file
    css_url = static('core/styles.css')  # Ensure this matches your static file path
    css_path = os.path.join(settings.STATIC_ROOT, css_url.replace(settings.STATIC_URL, ''))

    # Ensure static and media files are properly loaded
    css_files = [
        CSS(string='@page { size: A4; margin: 1cm }'),
        CSS(css_path),
    ]
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="medical_record_{record_id}.pdf"'
    html.write_pdf(response, stylesheets=css_files)
    return response

@login_required
@group_required('doctor')
def export_medical_record_doc(request, record_id):
    record = get_object_or_404(MedicalRecord, id=record_id)
    document = Document()
    document.add_heading('Медицинская запись', 0)

    document.add_heading('Описание приёма', level=1)
    document.add_paragraph(record.description)

    document.add_heading('Заключение', level=1)
    document.add_paragraph(record.conclusion)

    document.add_heading('Дата завершения', level=1)
    document.add_paragraph(str(record.date_completed))

    if record.image:
        document.add_heading('Изображение', level=1)
        document.add_picture(os.path.join(settings.MEDIA_ROOT, record.image.name), width=Inches(4.0))

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename="medical_record_{record_id}.docx"'
    document.save(response)
    return response