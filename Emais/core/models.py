from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('admin', 'Administrator'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )
    role = models.CharField(max_length=10, choices=ROLES)
    
    # Переопределяем обратные связи для groups и user_permissions
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')

class Appointment(models.Model):
    patient = models.ForeignKey(User, related_name='appointments', on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name='appointments_as_doctor', on_delete=models.CASCADE)
    date = models.DateTimeField()
    notes = models.TextField()

class MedicalRecord(models.Model):
    patient = models.ForeignKey(User, related_name='medical_records', on_delete=models.CASCADE)
    document = models.FileField(upload_to='medical_records/')
    created_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.CharField(max_length=200)
    image=models.ImageField(blank=True, upload_to='images')

    # меняем имя текущего экземпляра
    def __str__(self) -> str: # Чтобы возвращался строчный тип
        return self.name
