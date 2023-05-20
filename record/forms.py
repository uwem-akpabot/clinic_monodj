from django import forms
from .models import SoapNotes, Triage

# Doctor
class WriteNoteForm(forms.ModelForm):
	class Meta:
		model = SoapNotes
		fields = ['patient', 'date_of_visit', 'subjective', 'objective', 'assessment', 'plan', 'comments']

# Nurse
class RecordTriageForm(forms.ModelForm):
	class Meta:
		model = Triage
		fields = ['patient', 'date_of_visit']
