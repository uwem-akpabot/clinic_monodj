# Generated by Django 4.1.7 on 2023-05-20 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_remove_patient_user'),
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Triage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_visit', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='triage', to='patient.patient')),
            ],
        ),
    ]
