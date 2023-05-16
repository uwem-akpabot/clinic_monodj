from django import forms
from .models import Patient

class AddPatientForm(forms.ModelForm):
	class Meta:
		model = Patient
		fields = ['fname', 'sname', 'gender', 'phone', 'email', 'address', 'contact_person', 
	        'contact_person_phone', 'created_by']