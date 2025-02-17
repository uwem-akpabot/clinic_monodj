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

class RequestLabtest_Lab(models.Model):
	patient = models.ForeignKey(Patient, related_name='request_labtest_lab', on_delete=models.CASCADE)
	date_of_visit = models.CharField(max_length=15)
	tests = models.TextField()
	created_by = models.CharField(max_length=15)
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class RequestDrugDispensing(models.Model):
	patient = models.ForeignKey(Patient, related_name='request_drugdispensing', on_delete=models.CASCADE)
	date_of_visit = models.CharField(max_length=15)
	diagnosis = models.TextField()
	medicine_dosage = models.TextField()
	created_by = models.CharField(max_length=15)
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class RequestTriageNurse(models.Model):
	patient = models.ForeignKey(Patient, related_name='request_triagenurse', on_delete=models.CASCADE)
	date_of_visit = models.CharField(max_length=15)
	comment = models.TextField()
	temp = models.CharField(max_length=12, null=True, blank=True)
	bp = models.CharField(max_length=12, null=True, blank=True)
	temp = models.CharField(max_length=12, null=True, blank=True)
	pulse = models.CharField(max_length=12, null=True, blank=True)
	respiration = models.CharField(max_length=12, null=True, blank=True)
	spo2 = models.CharField(max_length=12, null=True, blank=True)
	lmp = models.CharField(max_length=12, null=True, blank=True)
	weight = models.CharField(max_length=12, null=True, blank=True)
	height = models.CharField(max_length=12, null=True, blank=True)
	bmi = models.CharField(max_length=12, null=True, blank=True)
	medication = models.TextField(null=True, blank=True)
	nurse_report = models.TextField(null=True, blank=True)
	created_by = models.CharField(max_length=15)
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

# class RecordTestAction(models.Model):
# 	patient = models.ForeignKey(Patient, related_name='record_testaction_pat', on_delete=models.CASCADE)
# 	requestlabtest_lab = models.ForeignKey(RequestLabtest_Lab, related_name='requestlabtest_lab', on_delete=models.CASCADE)
# 	test_result = models.TextField()
# 	created_by = models.CharField(max_length=15)
	# created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
