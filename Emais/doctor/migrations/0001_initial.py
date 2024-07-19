# Generated by Django 4.2 on 2024-07-18 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="DoctorProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("patronymic", models.CharField(max_length=100)),
                ("specialization", models.CharField(default="-", max_length=100)),
                ("hospital_address", models.CharField(default="-", max_length=100)),
                (
                    "contact_number",
                    models.CharField(default="+71234567890", max_length=15),
                ),
                ("email", models.EmailField(default="+mail@mail.com", max_length=15)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
