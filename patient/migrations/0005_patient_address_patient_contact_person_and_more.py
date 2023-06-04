# Generated by Django 4.1.7 on 2023-06-03 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_remove_patient_address_remove_patient_contact_person_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='address',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='patient',
            name='contact_person',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='contact_person_phone',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='patient',
            name='created_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.CharField(blank=True, max_length=45),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='phone',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='patient',
            name='sname',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
