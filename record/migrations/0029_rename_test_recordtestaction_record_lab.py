# Generated by Django 4.1.7 on 2023-06-03 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0028_dispensedrugs_created_at_dispensedrugs_created_by_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recordtestaction',
            old_name='test',
            new_name='record_lab',
        ),
    ]
