# Generated by Django 4.1.7 on 2023-05-21 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_triage'),
    ]

    operations = [
        migrations.AddField(
            model_name='soapnotes',
            name='created_by',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
