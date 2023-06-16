from django import forms
from .models import SoapNotes, RequestLabtest_Lab, RequestDrugDispensing, RequestTriageNurse

# Doctor
class WriteNoteForm(forms.ModelForm):
	class Meta:
		model = SoapNotes
		fields = ['patient', 'date_of_visit', 'subjective', 'objective', 'assessment', 'plan', 
	    	'comments', 'created_by']

# Pharmacist

# Lab
# class RecordLabResultForm(forms.ModelForm):
# 	class Meta:
# 		model = RecordLabResult
# 		fields = ['patient', 'date_of_visit', 'created_by']

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
		fields = ['patient', 'date_of_visit', 'comment', 'temp', 'bp', 'temp', 'pulse', 'respiration', 
	    	'spo2', 'lmp', 'weight', 'height', 'bmi', 'medication', 'nurse_report','created_by']

# # Lab
# class RecordTestActionForm(forms.ModelForm):
# 	class Meta:
# 		model = RecordTestAction
# 		fields = ['patient', 'requestlabtest_lab', 'test_result', 'created_by']
# 		# fields = ['test_result']
# 		# fields = ['patient', 'test', 'test_result', 'created_by']