from django.contrib.auth.models import User
from django.db import models
#from contribution.models import Cust_contrb

class Patient(models.Model):
	fname = models.CharField(max_length=45)
	sname = models.CharField(max_length=30)
	gender = models.CharField(max_length=6)
	phone = models.CharField(max_length=12, blank=True)
	email = models.CharField(max_length=45, blank=True)
	address = models.CharField(max_length=150, blank=True)
	contact_person = models.CharField(max_length=60, blank=True, null=True)
	contact_person_phone = models.CharField(max_length=15, blank=True)
	created_by = models.CharField(max_length=100, blank=True, null=True)
	# user = models.OneToOneField(User, related_name='Patient', on_delete=models.CASCADE)
	#cust_contrb = models.ForeignKey(Cust_contrb, related_name='Customer', on_delete=models.CASCADE)

# User.patientprofile = property(lambda u:Patient.objects.get_or_create(user=u)[0])
#Cust_contrb.cust_contrbprofile = property(lambda u:Cust_contrb.objects.get_or_create(user=u)[0])