# Generated by Django 4.1.7 on 2023-05-29 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_alter_patient_contact_person_phone'),
        ('record', '0009_remove_requestlabtest_lab_biochemistry_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestDrugDispensing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_visit', models.CharField(max_length=15)),
                ('drugs', models.TextField()),
                ('created_by', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_drugdispensing', to='patient.patient')),
            ],
        ),
    ]
