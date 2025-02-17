# Generated by Django 4.1.7 on 2023-05-27 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0008_alter_requestlabtest_lab_date_of_visit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestlabtest_lab',
            name='biochemistry',
        ),
        migrations.RemoveField(
            model_name='requestlabtest_lab',
            name='haematology',
        ),
        migrations.RemoveField(
            model_name='requestlabtest_lab',
            name='microbiology',
        ),
        migrations.AddField(
            model_name='requestlabtest_lab',
            name='tests',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='requestlabtest_lab',
            name='date_of_visit',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
