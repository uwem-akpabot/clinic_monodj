from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from patient.models import Patient
from record.models import SoapNotes, Triage, DispenseDrugs, RecordLabResult, RequestLabtest_Lab
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

@login_required
def view_dispensed(request):
	view_dispensed = DispenseDrugs.objects.all()
	return render(request,'pharmacist/view_dispensed.html', {'company':company, 'view_dispensed': view_dispensed})

# Lab Scientist
@login_required
def record_labresult(request):
	record_labresults = RequestLabtest_Lab.objects.all()
	return render(request,'lab/record_labresult.html', {'company':company, 'record_labresults': record_labresults})

# Lab Scientist
@login_required
def record_labresult_save(request):
	patients = Patient.objects.all()

	if request.method == 'POST':
		form = RecordLabResultForm(request.POST) 
		if form.is_valid():
			form_valid(request, form, 'RECORD LAB RESULT', 'Successful!')
			# additional codes here
			return redirect('record_labresult')
		else:
			form_not_valid()
	else:
		form = RecordLabResultForm() 

	pass_data = {'form': form, 'company':company, 'patients':patients}
	return render(request, 'lab/record_labresult.html', pass_data)

# Lab Scientist and Doctor
@login_required
def view_labresult(request):
	view_labresults = RecordLabResult.objects.all()
	return render(request,'lab/view_labresult.html', {'company':company, 'view_labresults': view_labresults})

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

#Lab record_test_action
@login_required
def record_test_action(request, record_lab_id):
	record_lab = RequestLabtest_Lab.objects.get(pk=record_lab_id)
	form = RequestLabtestLabForm(instance=record_lab)

	if request.method == 'POST':
		form = RequestLabtestLabForm(request.POST, instance=record_lab) #if submit is click and form method is POST

		if form.is_valid():
			form.save() #save to database

			msg_title = 'Updated!'
			msg_text = 'Lab test is saved successfully!'
			messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)
			return redirect('record_test_action')
		else:
			msg_title = 'Error!'
			msg_text = 'Record was NOT saved!'
			messages.add_message(request, messages.ERROR, msg_text, extra_tags=msg_title)
	else:
		form = RequestLabtestLabForm() #if submit is not clicked, display empty form

	return render(request, 'lab/record_test_action.html', {'form': form, 'company':company, 'record_lab': record_lab})

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

# @login_required
# def manager(request):
# 	managers = Manager.objects.all()
# 	return render(request,'manager/manager.html', {'company':company, 'managers': managers})


# #Get detail by Id
# @login_required
# def customer_detail(request, customer_id):
# 	customer = Customer.objects.get(pk=customer_id)
# 	return render(request, 'customer/customer_detail.html', {'company':company, 'customer': customer})

# @login_required
# def teller_detail(request, teller_id):
# 	teller = Teller.objects.get(pk=teller_id)
# 	return render(request, 'teller/teller_detail.html', {'company':company, 'teller': teller})

# @login_required
# def manager_detail(request, manager_id):
# 	manager = Manager.objects.get(pk=manager_id)
# 	return render(request, 'manager/manager_detail.html', {'company':company, 'manager': manager})


# #Update user record
# @login_required
# def update_customer(request, customer_id):
# 	customer = Customer.objects.get(pk=customer_id)
# 	form = AddCustomerForm(instance=customer)

# 	if request.method == 'POST':
# 		form = AddCustomerForm(request.POST, instance=customer) #if submit is click and form method is POST

# 		if form.is_valid():
# 			customer = form.save() #save to database

# 			msg_title = 'Updated!'
# 			msg_text = 'Customer is saved successfully!'
# 			messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)
# 			return redirect('customer')

# 		else:
# 			msg_title = 'Error!'
# 			msg_text = 'Record was NOT saved!'
# 			messages.add_message(request, messages.ERROR, msg_text, extra_tags=msg_title)

# 	else:
# 		form = AddCustomerForm() #if submit is not clicked, display empty form

# 	return render(request, 'customer/update_customer.html', {'form': form, 'company':company, 'customer': customer})


# @login_required
# def update_teller(request, teller_id):
# 	teller = Teller.objects.get(pk=teller_id)
# 	form = AddTellerForm(instance=teller)

# 	if request.method == 'POST':
# 		form = AddTellerForm(request.POST, instance=teller) #if submit is click and form method is POST

# 		if form.is_valid():
# 			teller = form.save() #save to database

# 			msg_title = 'Updated!'
# 			msg_text = 'Teller is saved successfully!'
# 			messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)
# 			return redirect('teller')

# 		else:
# 			msg_title = 'Error!'
# 			msg_text = 'Record was NOT saved!'
# 			messages.add_message(request, messages.ERROR, msg_text, extra_tags=msg_title)

# 	else:
# 		form = AddTellerForm() #if submit is not clicked, display empty form

# 	return render(request, 'teller/update_teller.html', {'form': form, 'company':company, 'teller': teller})


# @login_required
# def update_manager(request, manager_id):
# 	manager = Manager.objects.get(pk=manager_id)
# 	form = AddManagerForm(instance=manager)

# 	if request.method == 'POST':
# 		form = AddManagerForm(request.POST, instance=manager) #if submit is click and form method is POST

# 		if form.is_valid():
# 			manager = form.save() #save to database

# 			msg_title = 'Updated!'
# 			msg_text = 'Manager is saved successfully!'
# 			messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)
# 			return redirect('manager')

# 		else:
# 			msg_title = 'Error!'
# 			msg_text = 'Record was NOT saved!'
# 			messages.add_message(request, messages.ERROR, msg_text, extra_tags=msg_title)

# 	else:
# 		form = AddManagerForm() #if submit is not clicked, display empty form

# 	return render(request, 'manager/update_manager.html', {'form': form, 'company':company, 'manager': manager})


# #Delete user record
# @login_required
# def delete_customer(request, customer_id):
# 	customer = Customer.objects.get(pk=customer_id)

# 	if request.method == 'POST':
# 		customer.delete()

# 		msg_title = 'Deleted!'
# 		msg_text = 'Customer was deleted successfully!'
# 		messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)

# 		return redirect('customer')

# 	return render(request, 'customer/delete_customer.html', {'company':company, 'customer': customer})

# @login_required
# def delete_teller(request, teller_id):
# 	teller = Teller.objects.get(pk=teller_id)

# 	if request.method == 'POST':
# 		teller.delete()

# 		msg_title = 'Deleted!'
# 		msg_text = 'Teller was deleted successfully!'
# 		messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)

# 		return redirect('teller')

# 	return render(request, 'teller/delete_teller.html', {'company':company, 'teller': teller})

# @login_required
# def delete_manager(request, manager_id):
# 	manager = Manager.objects.get(pk=manager_id)

# 	if request.method == 'POST':
# 		manager.delete()

# 		msg_title = 'Deleted!'
# 		msg_text = 'Manager was deleted successfully!'
# 		messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)

# 		return redirect('manager')

# 	return render(request, 'manager/delete_manager.html', {'company':company, 'manager': manager})

# """
# @login_required
# def create_account(request):
# 	if request.method == 'POST':
# 		form = UserCreationForm(request.POST)

# 		if form.is_valid():
# 			user = form.save()
# 			account_type = request.POST.get('account_type', 'customer')
# 			created_by = request.POST.get('created_by')

# 			if account_type == 'mgr':
# 				userprofile = Userprofile.objects.create(user=user, is_mgr=True, created_by=created_by)
# 				userprofile.save()
# 			elif account_type == 'teller':
# 				userprofile = Userprofile.objects.create(user=user, is_teller=True, created_by=created_by)
# 				userprofile.save()
# 			else:
# 				userprofile = Userprofile.objects.create(user=user, is_cust=True, created_by=created_by)
# 				customerprofile = Customer.objects.create(user=user, created_by=created_by)
# 				userprofile.save()
# 				customerprofile.save()

# 			#login(request, user)
# 			#return redirect('index')
# 			return redirect('create_account')
# 	else:
# 		form = UserCreationForm()
# 	return render(request, 'frontend/create_account.html', {'form': form, 'company': COMPANY})




# @login_required
# def add_customer(request):
# 	if request.method == 'POST':
# 		form = AddCustomerForm(request.POST) #if submit is click and form method is POST

# 		if form.is_valid():
# 			customer = form.save() #save to database
# 			return redirect('add_customer') #take us back to index page
# 	else:
# 		form = AddCustomerForm() #if submit is not clicked, display empty form


# 	return render(request, 'customer/add_customer.html', {'company':company})
# """
