from django.db import models
from django.contrib.auth.models import User
from doctor.models import DoctorProfile

#Profile
class PatientMyInfo(models.Model):
  user=models.OneToOneField(User, on_delete=models.CASCADE)
  image=models.ImageField(blank=True, upload_to='_myinfo_images')
  contact_number=models.CharField(max_length=50, default="+123456789")

  def __str__(self):
      return self.user.username

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
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, blank=True) # ! ИГРУШКА ДЬЯВОЛА
    description = models.TextField()
    conclusion = models.TextField()
    image = models.ImageField(upload_to='medical_records/', blank=True, null=True)
    date_completed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.patient.username} - {self.date_completed}'
