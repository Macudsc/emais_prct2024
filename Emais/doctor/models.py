from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DoctorProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    patronymic=models.CharField(max_length=100)
    #gender=models.CharField(max_length=100,default="-")
    specialization=models.CharField(max_length=100,default="-")
    hospital_address=models.CharField(max_length=100,default="-")
    contact_number=models.CharField(max_length=15, default="+71234567890")
    email=models.EmailField(max_length=15, default="+mail@mail.com")

    def __str__(self):
      return self.user.username