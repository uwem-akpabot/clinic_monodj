# Generated by Django 4.1.7 on 2023-05-20 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0015_doctor_labscientist_nurse_pharmacist_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='acct_bank',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='acct_name',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='acct_no',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='business_addr',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='home_addr',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='kin_name',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='kin_relationship',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='kin_tel',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='package',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='payment_plan',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='tel',
        ),
        migrations.RemoveField(
            model_name='labscientist',
            name='acct_bank',
        ),
        migrations.RemoveField(
            model_name='labscientist',
            name='acct_name',
        ),
        migrations.RemoveField(
            model_name='labscientist',
            name='acct_no',
        ),
        migrations.RemoveField(
            model_name='labscientist',
            name='home_addr',
        ),
        migrations.RemoveField(
            model_name='labscientist',
            name='kin_name',
        ),
        migrations.RemoveField(
            model_name='labscientist',
            name='kin_relationship',
        ),
        migrations.RemoveField(
            model_name='labscientist',
            name='kin_tel',
        ),
        migrations.RemoveField(
            model_name='labscientist',
            name='tel',
        ),
    ]
