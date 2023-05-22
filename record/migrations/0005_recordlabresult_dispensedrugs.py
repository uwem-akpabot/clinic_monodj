# Generated by Django 4.1.7 on 2023-05-22 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_alter_patient_contact_person_phone'),
        ('record', '0004_triage_bmi_triage_bp_triage_created_by_triage_height_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordLabResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_visit', models.CharField(max_length=15)),
                ('created_by', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='record_labresult', to='patient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='DispenseDrugs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_visit', models.CharField(max_length=15)),
                ('diagnosis', models.TextField()),
                ('medicine_1', models.CharField(max_length=40)),
                ('med1_dose', models.CharField(max_length=15)),
                ('medicine_2', models.CharField(blank=True, max_length=40)),
                ('med2_dose', models.CharField(blank=True, max_length=15)),
                ('medicine_3', models.CharField(blank=True, max_length=40)),
                ('med3_dose', models.CharField(blank=True, max_length=15)),
                ('medicine_4', models.CharField(blank=True, max_length=40)),
                ('med4_dose', models.CharField(blank=True, max_length=15)),
                ('medicine_5', models.CharField(blank=True, max_length=40)),
                ('med5_dose', models.CharField(blank=True, max_length=15)),
                ('medicine_6', models.CharField(blank=True, max_length=40)),
                ('med6_dose', models.CharField(blank=True, max_length=15)),
                ('created_by', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dispense_drug', to='patient.patient')),
            ],
        ),
    ]
