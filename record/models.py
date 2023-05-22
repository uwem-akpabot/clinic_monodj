from django.contrib.auth.models import User
from django.db import models
from patient.models import Patient

class SoapNotes(models.Model):
	patient = models.ForeignKey(Patient, related_name='soapnote', on_delete=models.CASCADE)
	date_of_visit = models.CharField(max_length=15)
	subjective = models.TextField()
	objective = models.TextField(blank=True)
	assessment = models.TextField(blank=True)
	plan = models.TextField(blank=True)
	comments = models.TextField(blank=True)
	created_by = models.CharField(max_length=15)
	# user = models.OneToOneField(User, related_name='SoapNotes', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class Triage(models.Model):
	patient = models.ForeignKey(Patient, related_name='triage', on_delete=models.CASCADE)
	date_of_visit = models.CharField(max_length=15)
	temp = models.CharField(max_length=12, blank=True)
	bp = models.CharField(max_length=12, blank=True)
	temp = models.CharField(max_length=12, blank=True)
	pulse = models.CharField(max_length=12, blank=True)
	respiration = models.CharField(max_length=12, blank=True)
	spo2 = models.CharField(max_length=12, blank=True)
	lmp = models.CharField(max_length=12, blank=True)
	weight = models.CharField(max_length=12, blank=True)
	height = models.CharField(max_length=12, blank=True)
	bmi = models.CharField(max_length=12, blank=True)
	medication = models.TextField()
	nurse_report = models.TextField()
	created_by = models.CharField(max_length=15)
	# user = models.OneToOneField(User, related_name='SoapNotes', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class DispenseDrugs(models.Model):
	patient = models.ForeignKey(Patient, related_name='dispense_drug', on_delete=models.CASCADE)
	date_of_visit = models.CharField(max_length=15)
	diagnosis = models.TextField()
	medicine_1 = models.CharField(max_length=40)
	med1_dose = models.CharField(max_length=15)
	medicine_2 = models.CharField(max_length=40, blank=True)
	med2_dose = models.CharField(max_length=15, blank=True)
	medicine_3 = models.CharField(max_length=40, blank=True)
	med3_dose = models.CharField(max_length=15, blank=True)
	medicine_4 = models.CharField(max_length=40, blank=True)
	med4_dose = models.CharField(max_length=15, blank=True)
	medicine_5 = models.CharField(max_length=40, blank=True)
	med5_dose = models.CharField(max_length=15, blank=True)
	medicine_6 = models.CharField(max_length=40, blank=True)
	med6_dose = models.CharField(max_length=15, blank=True)
	created_by = models.CharField(max_length=15)
	# user = models.OneToOneField(User, related_name='SoapNotes', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class RecordLabResult(models.Model):
	patient = models.ForeignKey(Patient, related_name='record_labresult', on_delete=models.CASCADE)
	date_of_visit = models.CharField(max_length=15)
	created_by = models.CharField(max_length=15)
	# user = models.OneToOneField(User, related_name='SoapNotes', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class RequestLabtest_Lab(models.Model):
	patient = models.ForeignKey(Patient, related_name='request_labtest_lab', on_delete=models.CASCADE)
	date_of_visit = models.CharField(max_length=15)
	created_by = models.CharField(max_length=15)
	# user = models.OneToOneField(User, related_name='SoapNotes', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	