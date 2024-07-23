from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from patient.models import PatientProfile
from doctor.models import DoctorProfile
from administrator.models import AdministratorProfile
from django.contrib.auth.models import Group
from bson import ObjectId

from pymongo import MongoClient
import pymongo
from django.conf import settings
import gridfs

from patient.models import MedicalRecord
#from django.db import models
#from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver

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

@receiver(post_delete, sender=MedicalRecord)
def delete_image_from_gridfs(sender, instance, **kwargs):
    if instance.image_id:
        try:
            client = MongoClient(settings.MONGO_DB['host'], settings.MONGO_DB['port'])
            db = client[settings.MONGO_DB['db']]
            fs = gridfs.GridFS(db)
            
            print(f"Attempting to delete image with ID: {instance.image_id}")

            # Convert image_id to ObjectId
            image_id = ObjectId(instance.image_id)

            fs.delete(image_id)
            print(f"Image {image_id} deleted successfully")
        except gridfs.errors.NoFile:
            print(f"Image {instance.image_id} not found in GridFS")
        except Exception as e:
            print(f"Error deleting image {instance.image_id}: {e}")