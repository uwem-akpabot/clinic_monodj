# Generated by Django 4.1.7 on 2023-05-21 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0003_soapnotes_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='triage',
            name='bmi',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='triage',
            name='bp',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='triage',
            name='created_by',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='triage',
            name='height',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='triage',
            name='lmp',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='triage',
            name='medication',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='triage',
            name='nurse_report',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='triage',
            name='pulse',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='triage',
            name='respiration',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='triage',
            name='spo2',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='triage',
            name='temp',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='triage',
            name='weight',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
