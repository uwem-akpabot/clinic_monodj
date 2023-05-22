from django import forms
from .models import SoapNotes, Triage, DispenseDrugs, RecordLabResult, RequestLabtest_Lab

# Doctor
class WriteNoteForm(forms.ModelForm):
	class Meta:
		model = SoapNotes
		fields = ['patient', 'date_of_visit', 'subjective', 'objective', 'assessment', 'plan', 'comments']

# Nurse
class RecordTriageForm(forms.ModelForm):
	class Meta:
		model = Triage
		fields = ['patient', 'date_of_visit', 'temp', 'bp', 'temp', 'pulse', 'respiration', 'spo2', 'lmp', 'weight', 'height', 'bmi', 
	    	'medication', 'nurse_report']
		
# Pharmacist
class DispenseDrugsForm(forms.ModelForm):
	class Meta:
		model = DispenseDrugs
		fields = ['patient', 'date_of_visit', 'diagnosis', 'medicine_1', 'med1_dose', 'medicine_2', 'med2_dose', 
	    	'medicine_3', 'med3_dose', 'medicine_4', 'med4_dose', 'medicine_5', 'med5_dose', 'medicine_6', 'med6_dose',]

# Lab
class RecordLabResultForm(forms.ModelForm):
	class Meta:
		model = RecordLabResult
		fields = ['patient', 'date_of_visit']

# Doctor
class RequestLabtestLabForm(forms.ModelForm):
	class Meta:
		model = RequestLabtest_Lab
		fields = ['patient', 'date_of_visit']