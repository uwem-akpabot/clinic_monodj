# Generated by Django 4.1.7 on 2023-05-19 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0002_soapnotes_remove_labscientist_user_remove_nurse_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soapnotes',
            name='subjective',
            field=models.TextField(),
        ),
    ]
