# Generated by Django 4.2 on 2024-07-20 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("patient", "0011_alter_medicalrecord_doctor_delete_patientmyinfo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="medicalrecord",
            name="image",
        ),
        migrations.AddField(
            model_name="medicalrecord",
            name="image_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]