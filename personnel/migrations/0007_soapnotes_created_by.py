# Generated by Django 4.1.7 on 2023-05-20 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personnel', '0006_soapnotes_created_at_soapnotes_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='soapnotes',
            name='created_by',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='soap', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
