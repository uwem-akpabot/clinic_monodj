from django.contrib.auth.models import User
from django.db import models
#from contribution.models import Cust_contrb

class Doctor(models.Model):
	user = models.OneToOneField(User, related_name='Doctor', on_delete=models.CASCADE)
	fname = models.CharField(max_length=45)
	sname = models.CharField(max_length=30)
	gender = models.CharField(max_length=6, blank=True)
	phone = models.CharField(max_length=12, blank=True)
	created_by = models.CharField(max_length=100, blank=True, null=True)

User.doctorprofile = property(lambda u:Doctor.objects.get_or_create(user=u)[0])

class Labscientist(models.Model):
	user = models.OneToOneField(User, related_name='Labscientist', on_delete=models.CASCADE)
	fname = models.CharField(max_length=45)
	sname = models.CharField(max_length=30)
	gender = models.CharField(max_length=6, blank=True)
	phone = models.CharField(max_length=12, blank=True)
	created_by = models.CharField(max_length=100, blank=True, null=True)

User.labscientistprofile = property(lambda u:Labscientist.objects.get_or_create(user=u)[0])

class Nurse(models.Model):
	user = models.OneToOneField(User, related_name='Nurse', on_delete=models.CASCADE)
	fname = models.CharField(max_length=45)
	sname = models.CharField(max_length=30)
	gender = models.CharField(max_length=6, blank=True)
	phone = models.CharField(max_length=12, blank=True)
	created_by = models.CharField(max_length=100, blank=True, null=True)

User.nurseprofile = property(lambda u:Nurse.objects.get_or_create(user=u)[0])

class Pharmacist(models.Model):
	user = models.OneToOneField(User, related_name='Pharmacist', on_delete=models.CASCADE)
	fname = models.CharField(max_length=45)
	sname = models.CharField(max_length=30)
	gender = models.CharField(max_length=6, blank=True)
	phone = models.CharField(max_length=12, blank=True)
	created_by = models.CharField(max_length=100, blank=True, null=True)

User.pharmacistprofile = property(lambda u:Pharmacist.objects.get_or_create(user=u)[0])