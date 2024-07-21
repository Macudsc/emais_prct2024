from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Product(models.Model):
    seller=models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.CharField(max_length=200)
    image=models.ImageField(blank=True, upload_to='images')

    # меняем имя текущего экземпляра
    def __str__(self) -> str: # Чтобы возвращался строчный тип
        return self.name