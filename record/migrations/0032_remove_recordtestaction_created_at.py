# Generated by Django 4.1.7 on 2023-06-03 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0031_recordtestaction_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recordtestaction',
            name='created_at',
        ),
    ]
