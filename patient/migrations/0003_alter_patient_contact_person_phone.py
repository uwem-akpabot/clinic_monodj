# Generated by Django 4.1.7 on 2023-05-21 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_remove_patient_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='contact_person_phone',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
