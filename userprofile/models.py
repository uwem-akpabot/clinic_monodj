from django.contrib.auth.models import User
from django.db import models

class Userprofile(models.Model):
	user = models.OneToOneField(User, related_name='Userprofile', on_delete=models.CASCADE)
	is_admin = models.BooleanField(default=False)
	is_doc = models.BooleanField(default=False)
	is_lab = models.BooleanField(default=False)
	is_nurse = models.BooleanField(default=False)
	is_pharm = models.BooleanField(default=False)
	first_name = models.CharField(max_length=45, blank=True, null=True)
	last_name = models.CharField(max_length=35, blank=True, null=True)
	created_by = models.CharField(max_length=100, blank=True, null=True)

User.userprofile = property(lambda u:Userprofile.objects.get_or_create(user=u)[0])
