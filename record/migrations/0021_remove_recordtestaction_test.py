# Generated by Django 4.1.7 on 2023-06-03 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0020_recordtestaction_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recordtestaction',
            name='test',
        ),
    ]
