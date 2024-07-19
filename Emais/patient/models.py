from django.db import models
from django.contrib.auth.models import User

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