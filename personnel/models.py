from django.contrib.auth.models import User
from django.db import models
from patient.models import Patient
#from contribution.models import Cust_contrb

class Doctor(models.Model):
	user = models.OneToOneField(User, related_name='Doctor', on_delete=models.CASCADE)
	#cust_contrb = models.ForeignKey(Cust_contrb, related_name='Customer', on_delete=models.CASCADE)
	name = models.CharField(max_length=45)
	gender = models.CharField(max_length=6, blank=True)
	created_by = models.CharField(max_length=100, blank=True, null=True)

User.doctorprofile = property(lambda u:Doctor.objects.get_or_create(user=u)[0])
#Cust_contrb.cust_contrbprofile = property(lambda u:Cust_contrb.objects.get_or_create(user=u)[0])

class LabScientist(models.Model):
	user = models.OneToOneField(User, related_name='LabScientist', on_delete=models.CASCADE)
	name = models.CharField(max_length=45)
	gender = models.CharField(max_length=6, blank=True)
	created_by = models.CharField(max_length=100, blank=True, null=True)

User.labscientistprofile = property(lambda u:LabScientist.objects.get_or_create(user=u)[0])

class Nurse(models.Model):
	user = models.OneToOneField(User, related_name='Nurse', on_delete=models.CASCADE)
	name = models.CharField(max_length=45)
	gender = models.CharField(max_length=6, blank=True)
	created_by = models.CharField(max_length=100, blank=True, null=True)

User.nurseprofile = property(lambda u:Nurse.objects.get_or_create(user=u)[0])

class Pharmacist(models.Model):
	user = models.OneToOneField(User, related_name='Pharmacist', on_delete=models.CASCADE)
	name = models.CharField(max_length=45)
	gender = models.CharField(max_length=6, blank=True)
	created_by = models.CharField(max_length=100, blank=True, null=True)

User.pharmprofile = property(lambda u:Pharmacist.objects.get_or_create(user=u)[0])
