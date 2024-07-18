from django.db import models
from django.contrib.auth.models import User

#Profile
class PatientMyInfo(models.Model):
  user=models.OneToOneField(User, on_delete=models.CASCADE)
  image=models.ImageField(blank=True, upload_to='_myinfo_images')
  contact_number=models.CharField(max_length=50, default="+123456789")

  def __str__(self):
      return self.user.username