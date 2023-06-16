# Generated by Django 4.1.7 on 2023-06-16 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0036_requesttriagenurse_bmi_requesttriagenurse_bp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requesttriagenurse',
            name='bmi',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='requesttriagenurse',
            name='bp',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='requesttriagenurse',
            name='height',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='requesttriagenurse',
            name='lmp',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='requesttriagenurse',
            name='medication',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='requesttriagenurse',
            name='nurse_report',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='requesttriagenurse',
            name='pulse',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='requesttriagenurse',
            name='respiration',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='requesttriagenurse',
            name='spo2',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='requesttriagenurse',
            name='temp',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='requesttriagenurse',
            name='weight',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
