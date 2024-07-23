# Generated by Django 4.2 on 2024-07-21 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("patient", "0013_telegramuser"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="medicalrecord",
            name="image_id",
        ),
        migrations.AlterField(
            model_name="telegramuser",
            name="username",
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name="MedicalRecordImage",
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
                ("image_id", models.CharField(max_length=255)),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                (
                    "medical_record",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="patient.medicalrecord",
                    ),
                ),
            ],
        ),
    ]