# Generated by Django 4.1.7 on 2023-05-09 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=45)),
                ('sname', models.CharField(max_length=30)),
                ('gender', models.CharField(blank=True, max_length=6)),
                ('phone', models.CharField(blank=True, max_length=12)),
                ('created_by', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Pharmacist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=45)),
                ('sname', models.CharField(max_length=30)),
                ('gender', models.CharField(blank=True, max_length=6)),
                ('phone', models.CharField(blank=True, max_length=12)),
                ('created_by', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Nurse', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Labscientist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=45)),
                ('sname', models.CharField(max_length=30)),
                ('gender', models.CharField(blank=True, max_length=6)),
                ('phone', models.CharField(blank=True, max_length=12)),
                ('created_by', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Labscientist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=45)),
                ('sname', models.CharField(max_length=30)),
                ('gender', models.CharField(blank=True, max_length=6)),
                ('phone', models.CharField(blank=True, max_length=12)),
                ('created_by', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Doctor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
