# Generated by Django 4.1.7 on 2023-05-20 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personnel', '0011_remove_soapnotes_recorded_by_soapnotes_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soapnotes',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL),
        ),
    ]
