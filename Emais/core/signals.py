from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import PatientProfile, DoctorProfile, AdministratorProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.groups.filter(name='patient').exists():
            PatientProfile.objects.create(user=instance)
        elif instance.groups.filter(name='doctor').exists():
            DoctorProfile.objects.create(user=instance)
        elif instance.groups.filter(name='administrator').exists():
            AdministratorProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.groups.filter(name='patient').exists():
        instance.patientprofile.save()
    elif instance.groups.filter(name='doctor').exists():
        instance.doctorprofile.save()
    elif instance.groups.filter(name='administrator').exists():
        instance.administratorprofile.save()
