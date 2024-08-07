from django.db import models
from django.contrib.auth.models import User

class AdministratorProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number=models.CharField(max_length=15, default="+71234567890")
    email=models.EmailField(max_length=15, default="+mail@mail.com")

    def __str__(self):
      return self.user.username