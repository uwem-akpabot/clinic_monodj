from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from patient.models import Patient
from record.models import SoapNotes, Triage, DispenseDrugs, RecordLabResult, RequestLabtest_Lab, RecordTestAction
from record.forms import WriteNoteForm, RecordTriageForm, DispenseDrugsForm, RecordLabResultForm, RequestLabtestLabForm, RequestDrugDispensingForm, RequestTriageNurseForm
from django.contrib import messages

company = "Beyond's Healthcare and Fertility Center"

#Doctor
@login_required
def write_note_soap(request):
	patients = Patient.objects.all()

	if request.method == 'POST':
		form = WriteNoteForm(request.POST) 
		if form.is_valid():
			form_valid(request, form, 'S.O.A.P. NOTE', 'Successful!')
			# additional codes here
			return redirect('write_note_soap')
		else:
			form_not_valid(request)
	else:
		form = WriteNoteForm() 
	
	pass_data = {'form': form, 'company':company, 'patients':patients}
	return render(request, 'doctor/write_note_soap.html', pass_data)
	
	
@login_required
def view_notes_soap(request):
	soapnotes = SoapNotes.objects.all()
	return render(request,'doctor/view_notes_soap.html', {'company':company, 'soapnotes': soapnotes})
		
#Nurse
@login_required
def record_triage(request):
	patients = Patient.objects.all()

	if request.method == 'POST':
		form = RecordTriageForm(request.POST) 
		if form.is_valid():
			form_valid(request, form, 'TRIAGE', 'Successful!')
			# additional codes here
			return redirect('record_triage')
		else:
			form_not_valid()
	else:
		form = RecordTriageForm() 
	
	pass_data = {'form': form, 'company':company, 'patients':patients}
	return render(request, 'nurse/record_triage.html', pass_data)

@login_required
def view_triage(request):
	triages = Triage.objects.all()
	return render(request,'nurse/view_triage.html', {'company':company, 'triages': triages})

# Pharcmacist
@login_required
def dispense_drugs(request):
	patients = Patient.objects.all()

	if request.method == 'POST':
		form = DispenseDrugsForm(request.POST) 
		if form.is_valid():
			form_valid(request, form, 'DISPENSE DRUGS', 'Successful!')
			# additional codes here
			return redirect('dispense_drugs')
		else:
			form_not_valid()
	else:
		form = DispenseDrugsForm() 

	pass_data = {'form': form, 'company':company, 'patients':patients}
	return render(request, 'pharmacist/dispense_drugs.html', pass_data)

# Doctor
@login_required
def request_drug_dispensing(request):
	patients = Patient.objects.all()

	if request.method == "POST":
		form = RequestDrugDispensingForm(request.POST)
		
		if form.is_valid():
			form.patient_id = patients
			form.drugs = request.POST.getlist('drugs')
			form_valid(request, form, 'REQUEST DRUG DISPENSING', 'Successful!')
			return redirect('request_drug_dispensing')
		else:
			form_not_valid(request)
	else:
		form = RequestDrugDispensingForm() 

	pass_data = {'form': form, 'company':company, 'patients':patients}
	return render(request, 'doctor/request_drug_dispensing.html', pass_data)

# Doctor
@login_required
def request_triage_nurse(request):
	patients = Patient.objects.all()

	if request.method == "POST":
		form = RequestTriageNurseForm(request.POST)
		
		if form.is_valid():
			form.patient_id = patients
			form_valid(request, form, 'TRIAGE REQUEST SENT', 'Successful!')
			return redirect('request_triage_nurse')
		else:
			form_not_valid(request)
	else:
		form = RequestTriageNurseForm() 

	pass_data = {'form': form, 'company':company, 'patients':patients}
	return render(request, 'doctor/request_triage_nurse.html', pass_data)

@login_required
def view_dispensed(request):
	view_dispensed = DispenseDrugs.objects.all()
	return render(request,'pharmacist/view_dispensed.html', {'company':company, 'view_dispensed': view_dispensed})

# Doctor
@login_required
def request_labtest_lab(request):
	patients = Patient.objects.all()

	if request.method == "POST":
		form = RequestLabtestLabForm(request.POST)
		
		if form.is_valid():
			form.patient_id = patients
			form.tests = request.POST.getlist('tests')
			form_valid(request, form, 'REQUEST LAB TEST', 'Successful!')
			return redirect('request_labtest_lab')
		else:
			form_not_valid(request)
	else:
		form = RequestLabtestLabForm() 

	pass_data = {'form': form, 'company':company, 'patients':patients}
	return render(request, 'doctor/request_labtest_lab.html', pass_data)

# Doctor
@login_required
def view_requestlabtest_lab(request):
	view_requestlabtest_lab = RequestLabtest_Lab.objects.all()
	return render(request,'doc/view_requestlabtest_lab.html', {'company':company, 'view_requestlabtest_lab': view_requestlabtest_lab})

#Doc view_test_action
@login_required
def view_test_action(request, view_lab_id):
	view_lab = RequestLabtest_Lab.objects.get(pk=view_lab_id)
	rec_action = RecordTestAction.objects.get(pk=view_lab_id)
	return render(request, 'doctor/view_test_action.html', {'company':company, 'view_lab': view_lab, 'rec_action': rec_action})

# Lab Scientist
@login_required
def labresult(request):
	labresults = RequestLabtest_Lab.objects.all()
	return render(request,'lab/labresult.html', {'company':company, 'labresults': labresults})

# Lab record_test_action
@login_required
def update_labresult(request, req_labtest_id):
	req_labtest = RequestLabtest_Lab.objects.get(pk=req_labtest_id)
	form = RequestLabtestLabForm(instance=req_labtest)

	if request.method == "POST":
		form = RequestLabtestLabForm(request.POST, instance=req_labtest) 

		if form.is_valid():
			form.save() 

			msg_title = 'Updated!'
			msg_text = 'Test is saved successfully!'
			messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)
			return redirect('labresult')
		else:
			print(form.errors)
			msg_title = 'Error!'
			msg_text = 'Record was NOT saved!'
			messages.add_message(request, messages.ERROR, msg_text, extra_tags=msg_title)
	else:
		form = RequestLabtestLabForm() 
	return render(request, 'lab/update_labresult.html', {'form': form, 'company':company, 'req_labtest': req_labtest})

# Lab Scientist and Doctor
@login_required
def view_labresult(request, req_labtest_id):
	view_labresult = RequestLabtest_Lab.objects.get(pk=req_labtest_id)
	return render(request,'lab/view_labresult.html', {'company':company, 'view_labresult': view_labresult})

#Lab record_test_action
# @login_required
# def record_test_action(request, record_lab_id):
# 	record_lab = RequestLabtest_Lab.objects.get(pk=record_lab_id)
# 	form = RecordTestActionForm(instance=record_lab)

# 	if request.method == "POST":
# 		form = RecordTestActionForm(request.POST) 

# 		if form.is_valid():
# 			form.save() 

# 			msg_title = 'Updated!'
# 			msg_text = 'Test is saved successfully!'
# 			messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)
# 			return redirect('record_labresult')
# 		else:
# 			print(form.errors)
# 			msg_title = 'Error!'
# 			msg_text = 'Record was NOT saved!'
# 			messages.add_message(request, messages.ERROR, msg_text, extra_tags=msg_title)
# 	else:
# 		form = RecordTestActionForm() 
# 	return render(request, 'lab/record_test_action.html', {'form': form, 'company':company, 'record_lab': record_lab})

# Lab Scientist
# @login_required
# def record_labresult_save(request):
# 	patients = Patient.objects.all()

# 	if request.method == 'POST':
# 		form = RecordLabResultForm(request.POST) 
# 		if form.is_valid():
# 			form_valid(request, form, 'RECORD LAB RESULT', 'Successful!')
# 			# additional codes here
# 			return redirect('record_labresult')
# 		else:
# 			form_not_valid()
# 	else:
# 		form = RecordLabResultForm() 

# 	pass_data = {'form': form, 'company':company, 'patients':patients}
# 	return render(request, 'lab/record_labresult.html', pass_data)

# Misc function
def form_valid(request, form, subject, msg):
	form.save() 
	msg_title = msg
	msg_text = f'{subject} IS SAVED SUCCESSFULLY!'
	messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)

# Misc function
def form_not_valid(request):
	msg_title = 'Error!'
	msg_text = 'ERROR! RECORD HAS NOT BEEN SAVED!'
	messages.add_message(request, messages.INFO, msg_text, extra_tags=msg_title)
