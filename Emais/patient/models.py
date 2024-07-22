from django.db import models
from django.contrib.auth.models import User
from doctor.models import DoctorProfile

from pymongo import MongoClient
from django.conf import settings
import gridfs


class TelegramUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    chat_id = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.username} - {self.chat_id}"

class PatientProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    patronymic=models.CharField(max_length=100)
    birthday=models.DateField(null=True, blank=True)
    gender=models.CharField(max_length=100,default="-")
    address=models.CharField(max_length=100,default="-")
    contact_number=models.CharField(max_length=15, default="+71234567890")
    email=models.EmailField(max_length=15, default="+mail@mail.com")

    def __str__(self):
        return self.user.username

# Запись на приём
class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    def __str__(self):
        return f'{self.patient.username} - {self.doctor} on {self.date} at {self.time}'

class MedicalRecord(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='medical_records')
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.SET_NULL, null=True, blank=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    conclusion = models.TextField()
    image_id = models.CharField(max_length=255, blank=True, null=True)
    date_completed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.patient.username} - {self.date_completed}'

    def save_image(self, image):
        client = MongoClient(settings.MONGO_DB['host'], settings.MONGO_DB['port'])
        db = client[settings.MONGO_DB['db']]
        fs = gridfs.GridFS(db)
        image_id = fs.put(image, filename=image.name)
        self.image_id = image_id
        self.save()