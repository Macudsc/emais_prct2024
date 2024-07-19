from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from patient.models import PatientProfile
from doctor.models import DoctorProfile
from administrator.models import AdministratorProfile
from django.contrib.auth.models import Group

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
    if hasattr(instance, 'patientprofile'):
        instance.patientprofile.save()
    elif hasattr(instance, 'doctorprofile'):
        instance.doctorprofile.save()
    elif hasattr(instance, 'administratorprofile'):
        instance.administratorprofile.save()
