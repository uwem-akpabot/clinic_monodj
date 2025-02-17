# Generated by Django 4.1.7 on 2023-06-03 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0026_recordtestaction_delete_recordtest_action'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dispensedrugs',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='dispensedrugs',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='dispensedrugs',
            name='date_of_visit',
        ),
        migrations.RemoveField(
            model_name='dispensedrugs',
            name='diagnosis',
        ),
        migrations.RemoveField(
            model_name='dispensedrugs',
            name='med1_dose',
        ),
        migrations.RemoveField(
            model_name='dispensedrugs',
            name='med2_dose',
        ),
        migrations.RemoveField(
            model_name='dispensedrugs',
            name='med3_dose',
        ),
        migrations.RemoveField(
            model_name='dispensedrugs',
            name='med4_dose',
        ),
        migrations.RemoveField(
            model_name='dispensedrugs',
            name='med5_dose',
        ),
        migrations.RemoveField(
            model_name='dispensedrugs',
            name='med6_dose',
        ),
        migrations.RemoveField(
            model_name='dispensedrugs',
            name='medicine_1',
        ),
        migrations.RemoveField(
            model_name='dispensedrugs',
            name='medicine_2',
        ),
        migrations.RemoveField(
            model_name='dispensedrugs',
            name='medicine_3',
        ),
        migrations.RemoveField(
            model_name='dispensedrugs',
            name='medicine_4',
        ),
        migrations.RemoveField(
            model_name='dispensedrugs',
            name='medicine_5',
        ),
        migrations.RemoveField(
            model_name='dispensedrugs',
            name='medicine_6',
        ),
        migrations.RemoveField(
            model_name='dispensedrugs',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='recordlabresult',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='recordlabresult',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='recordlabresult',
            name='date_of_visit',
        ),
        migrations.RemoveField(
            model_name='recordlabresult',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='recordtestaction',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='recordtestaction',
            name='test',
        ),
        migrations.RemoveField(
            model_name='recordtestaction',
            name='test_result',
        ),
        migrations.RemoveField(
            model_name='requestdrugdispensing',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='requestdrugdispensing',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='requestdrugdispensing',
            name='date_of_visit',
        ),
        migrations.RemoveField(
            model_name='requestdrugdispensing',
            name='diagnosis',
        ),
        migrations.RemoveField(
            model_name='requestdrugdispensing',
            name='medicine_dosage',
        ),
        migrations.RemoveField(
            model_name='requestdrugdispensing',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='requestlabtest_lab',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='requestlabtest_lab',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='requestlabtest_lab',
            name='date_of_visit',
        ),
        migrations.RemoveField(
            model_name='requestlabtest_lab',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='requestlabtest_lab',
            name='tests',
        ),
        migrations.RemoveField(
            model_name='requesttriagenurse',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='requesttriagenurse',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='requesttriagenurse',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='requesttriagenurse',
            name='date_of_visit',
        ),
        migrations.RemoveField(
            model_name='requesttriagenurse',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='soapnotes',
            name='assessment',
        ),
        migrations.RemoveField(
            model_name='soapnotes',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='soapnotes',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='soapnotes',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='soapnotes',
            name='date_of_visit',
        ),
        migrations.RemoveField(
            model_name='soapnotes',
            name='objective',
        ),
        migrations.RemoveField(
            model_name='soapnotes',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='soapnotes',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='soapnotes',
            name='subjective',
        ),
        migrations.RemoveField(
            model_name='triage',
            name='bmi',
        ),
        migrations.RemoveField(
            model_name='triage',
            name='bp',
        ),
        migrations.RemoveField(
            model_name='triage',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='triage',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='triage',
            name='date_of_visit',
        ),
        migrations.RemoveField(
            model_name='triage',
            name='height',
        ),
        migrations.RemoveField(
            model_name='triage',
            name='lmp',
        ),
        migrations.RemoveField(
            model_name='triage',
            name='medication',
        ),
        migrations.RemoveField(
            model_name='triage',
            name='nurse_report',
        ),
        migrations.RemoveField(
            model_name='triage',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='triage',
            name='pulse',
        ),
        migrations.RemoveField(
            model_name='triage',
            name='respiration',
        ),
        migrations.RemoveField(
            model_name='triage',
            name='spo2',
        ),
        migrations.RemoveField(
            model_name='triage',
            name='temp',
        ),
        migrations.RemoveField(
            model_name='triage',
            name='weight',
        ),
    ]
