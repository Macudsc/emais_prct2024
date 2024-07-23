from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default="empty")
    last_name = models.CharField(max_length=100, default="empty")
    patronymic = models.CharField(max_length=100, default="empty")
    specialization = models.CharField(max_length=100, default="no_spec")
    hospital_address = models.CharField(max_length=100, default="-")
    contact_number = models.CharField(max_length=15, default="+71234567890")
    email = models.EmailField(max_length=100, default="mail@mail.com")

    def save(self, *args, **kwargs):
        if not self.pk:  # только если создан
            self.first_name = f"doctor_{self.user.id}"
            self.last_name = f"doctor_{self.user.id}"
            self.patronymic = f"patronymic_{self.user.id}"
            self.specialization = f"spec_{self.user.id}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username