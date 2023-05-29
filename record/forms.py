from django import forms
from .models import SoapNotes, Triage, DispenseDrugs, RecordLabResult, RequestLabtest_Lab, RequestDrugDispensing, RequestTriageNurse

# Doctor
class WriteNoteForm(forms.ModelForm):
	class Meta:
		model = SoapNotes
		fields = ['patient', 'date_of_visit', 'subjective', 'objective', 'assessment', 'plan', 
	    	'comments', 'created_by']

# Nurse
class RecordTriageForm(forms.ModelForm):
	class Meta:
		model = Triage
		fields = ['patient', 'date_of_visit', 'temp', 'bp', 'temp', 'pulse', 'respiration', 'spo2', 'lmp', 
	    	'weight', 'height', 'bmi', 'medication', 'nurse_report', 'created_by']
		
# Pharmacist
class DispenseDrugsForm(forms.ModelForm):
	class Meta:
		model = DispenseDrugs
		fields = ['patient', 'date_of_visit', 'diagnosis', 'medicine_1', 'med1_dose', 'medicine_2', 'med2_dose', 
	    	'medicine_3', 'med3_dose', 'medicine_4', 'med4_dose', 'medicine_5', 'med5_dose', 'medicine_6', 
			'med6_dose', 'created_by']

# Lab
class RecordLabResultForm(forms.ModelForm):
	class Meta:
		model = RecordLabResult
		fields = ['patient', 'date_of_visit', 'created_by']

# Doctor
class RequestLabtestLabForm(forms.ModelForm):
	class Meta:
		model = RequestLabtest_Lab
		fields = ['patient', 'date_of_visit', 'tests', 'created_by']

# Doctor
class RequestDrugDispensingForm(forms.ModelForm):
	class Meta:
		model = RequestDrugDispensing
		fields = ['patient', 'date_of_visit', 'diagnosis', 'medicine_dosage', 'created_by']

# Doctor
class RequestTriageNurseForm(forms.ModelForm):
	class Meta:
		model = RequestTriageNurse
		fields = ['patient', 'date_of_visit', 'comment', 'created_by']