# Generated by Django 4.1.7 on 2023-05-20 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0002_remove_patient_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoapNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_visit', models.CharField(max_length=15)),
                ('subjective', models.TextField()),
                ('objective', models.TextField(blank=True)),
                ('assessment', models.TextField(blank=True)),
                ('plan', models.TextField(blank=True)),
                ('comments', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='soapnote', to='patient.patient')),
            ],
        ),
    ]
