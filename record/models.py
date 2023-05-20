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
	# recorded_by = models.CharField(max_length=15)
	# user = models.OneToOneField(User, related_name='SoapNotes', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class Triage(models.Model):
	patient = models.ForeignKey(Patient, related_name='triage', on_delete=models.CASCADE)
	date_of_visit = models.CharField(max_length=15)
	# subjective = models.TextField()

	# recorded_by = models.CharField(max_length=15)
	# user = models.OneToOneField(User, related_name='SoapNotes', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)