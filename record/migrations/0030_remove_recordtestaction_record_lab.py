# Generated by Django 4.1.7 on 2023-06-03 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0029_rename_test_recordtestaction_record_lab'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recordtestaction',
            name='record_lab',
        ),
    ]
