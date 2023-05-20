from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from patient.models import Patient
from record.models import SoapNotes, Triage
from record.forms import WriteNoteForm, RecordTriageForm
from django.contrib import messages

company = "Beyond's Healthcare and Fertility Center"

#Doctor
@login_required
def write_note_soap(request):
	patients = Patient.objects.all()

	if request.method == 'POST':
		form = WriteNoteForm(request.POST) 

		if form.is_valid():
			write_note = form.save() 
			msg_title = 'New Record!'
			msg_text = 'Note is saved successfully!'
			messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)
			return redirect('write_note_soap')
		else:
			msg_title = 'Error!'
			msg_text = 'Record was NOT saved!'
			messages.add_message(request, messages.ERROR, msg_text, extra_tags=msg_title)
	else:
		form = WriteNoteForm() 
	return render(request, 'doctor/write_note_soap.html', {'form': form, 'company':company, 'patients':patients})

@login_required
def view_notes_soap(request):
	soapnotes = SoapNotes.objects.all()
	return render(request,'doctor/view_notes_soap.html', {'company':company, 'soapnotes': soapnotes})

def form_processing(request, form_name, subject, redirect_to):
	form = form_name(request.POST) 
	if form.is_valid():
		form.save() 
		msg_title = 'New Record!'
		msg_text = f'{subject} is saved successfully!'
		messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)
		return redirect(redirect_to)
	else:
		msg_title = 'Error!'
		msg_text = 'Record was NOT saved!'
		messages.add_message(request, messages.ERROR, msg_text, extra_tags=msg_title)
		
#Nurse
@login_required
def record_triage(request):
	patients = Patient.objects.all()

	if request.method == 'POST':
		form_processing('RecordTriageForm', 'Triage', 'nurse/record_triage')
		# form = RecordTriageForm(request.POST) 
		# if form.is_valid():
		# 	print("Form is valid")
		# 	form.save() 
		# 	msg_title = 'New Record!'
		# 	msg_text = 'Triage is saved successfully!'
		# 	messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)
		# 	return redirect('record_triage')
		# else:
		# 	msg_title = 'Error!'
		# 	msg_text = 'Record was NOT saved!'
		# 	messages.add_message(request, messages.ERROR, msg_text, extra_tags=msg_title)
	else:
		form = RecordTriageForm() 

	return render(request, 'nurse/record_triage.html', {'form': form, 'company':company, 'patients':patients})

@login_required
def view_triage(request):
	triages = Triage.objects.all()
	return render(request,'nurse/view_triage.html', {'company':company, 'triages': triages})


#Lab
@login_required
def record_labresult(request):
	pass
	# patients = Patient.objects.all()

	# if request.method == 'POST':
	# 	form = LabResultForm(request.POST) 
	# 	if form.is_valid():
	# 		print("Form is valid")
	# 		form.save() 
	# 		msg_title = 'New Record!'
	# 		msg_text = 'Lab Result is saved successfully!'
	# 		messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)
	# 		return redirect('record_triage')
	# 	else:
	# 		msg_title = 'Error!'
	# 		msg_text = 'Record was NOT saved!'
	# 		messages.add_message(request, messages.ERROR, msg_text, extra_tags=msg_title)
	# else:
	# 	form = LabResultForm() 

	# return render(request, 'nurse/record_triage.html', {'form': form, 'company':company, 'patients':patients})

@login_required
def view_labresult(request):
	pass
	# labres = LabResult.objects.all()
	# return render(request,'lab/view_labresult.html', {'company':company, 'labres': labres})

#Lab
@login_required
def dispense_drugs(request):
	pass
	# patients = Patient.objects.all()

	# if request.method == 'POST':
	# 	form = LabResultForm(request.POST) 
	# 	if form.is_valid():
	# 		print("Form is valid")
	# 		form.save() 
	# 		msg_title = 'New Record!'
	# 		msg_text = 'Lab Result is saved successfully!'
	# 		messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)
	# 		return redirect('record_triage')
	# 	else:
	# 		msg_title = 'Error!'
	# 		msg_text = 'Record was NOT saved!'
	# 		messages.add_message(request, messages.ERROR, msg_text, extra_tags=msg_title)
	# else:
	# 	form = LabResultForm() 

	# return render(request, 'nurse/record_triage.html', {'form': form, 'company':company, 'patients':patients})

@login_required
def view_dispensed(request):
	pass
	# labres = LabResult.objects.all()
	# return render(request,'lab/view_labresult.html', {'company':company, 'labres': labres})

"""
@login_required
def request_labtest_lab(request):
	patient = Patient.objects.all()

	if request.method == 'POST':
		form = RequestLabtestForm(request.POST) 

		if form.is_valid():
			patient = form.save() 
			msg_title = 'New Record!'
			msg_text = 'Patient is saved successfully!'
			messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)
			return redirect('register_patient')
		else:
			msg_title = 'Error!'
			msg_text = 'Record was NOT saved!'
			messages.add_message(request, messages.ERROR, msg_text, extra_tags=msg_title)
	else:
		form = RequestLabtestForm() 

	return render(request, 'patient/register_patient.html', {'form': form, 'company':company, 'patient':patient})


@login_required
def view_testresult_lab(request):
	patients = Patient.objects.all()
	return render(request,'patient/patients.html', {'company':company, 'patients': patients})

@login_required
def request_triage_nurse(request):
	patient = Patient.objects.all()

	if request.method == 'POST':
		form = RequestLabtestForm(request.POST) 

		if form.is_valid():
			patient = form.save() 
			msg_title = 'New Record!'
			msg_text = 'Patient is saved successfully!'
			messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)
			return redirect('register_patient')
		else:
			msg_title = 'Error!'
			msg_text = 'Record was NOT saved!'
			messages.add_message(request, messages.ERROR, msg_text, extra_tags=msg_title)
	else:
		form = RequestLabtestForm() 

	return render(request, 'patient/register_patient.html', {'form': form, 'company':company, 'patient':patient})


@login_required
def view_triage_nurse(request):
	patients = Patient.objects.all()
	return render(request,'patient/patients.html', {'company':company, 'patients': patients})


@login_required
def request_drug_pharm(request):
	patient = Patient.objects.all()

	if request.method == 'POST':
		form = RequestLabtestForm(request.POST) 

		if form.is_valid():
			patient = form.save() 
			msg_title = 'New Record!'
			msg_text = 'Patient is saved successfully!'
			messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)
			return redirect('register_patient')
		else:
			msg_title = 'Error!'
			msg_text = 'Record was NOT saved!'
			messages.add_message(request, messages.ERROR, msg_text, extra_tags=msg_title)
	else:
		form = RequestLabtestForm() 

	return render(request, 'patient/register_patient.html', {'form': form, 'company':company, 'patient':patient})

# LAB
@login_required
def record_labresult(request):
	patient = Patient.objects.all()

	if request.method == 'POST':
		form = RequestLabtestForm(request.POST) 

		if form.is_valid():
			patient = form.save() 
			msg_title = 'New Record!'
			msg_text = 'Patient is saved successfully!'
			messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)
			return redirect('register_patient')
		else:
			msg_title = 'Error!'
			msg_text = 'Record was NOT saved!'
			messages.add_message(request, messages.ERROR, msg_text, extra_tags=msg_title)
	else:
		form = RequestLabtestForm() 

	return render(request, 'patient/register_patient.html', {'form': form, 'company':company, 'patient':patient})

# NURSE
@login_required
def record_triage(request):
	patient = Patient.objects.all()

	if request.method == 'POST':
		form = RequestLabtestForm(request.POST) 

		if form.is_valid():
			patient = form.save() 
			msg_title = 'New Record!'
			msg_text = 'Patient is saved successfully!'
			messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)
			return redirect('register_patient')
		else:
			msg_title = 'Error!'
			msg_text = 'Record was NOT saved!'
			messages.add_message(request, messages.ERROR, msg_text, extra_tags=msg_title)
	else:
		form = RequestLabtestForm() 

	return render(request, 'patient/register_patient.html', {'form': form, 'company':company, 'patient':patient})

# PHARM
@login_required
def dispense_drugs(request):
	patient = Patient.objects.all()

	if request.method == 'POST':
		form = RequestLabtestForm(request.POST) 

		if form.is_valid():
			patient = form.save() 
			msg_title = 'New Record!'
			msg_text = 'Patient is saved successfully!'
			messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)
			return redirect('register_patient')
		else:
			msg_title = 'Error!'
			msg_text = 'Record was NOT saved!'
			messages.add_message(request, messages.ERROR, msg_text, extra_tags=msg_title)
	else:
		form = RequestLabtestForm() 

	return render(request, 'patient/register_patient.html', {'form': form, 'company':company, 'patient':patient})
"""

"""
write_note_soap
# view_notes_soap
request_labtest_lab
view_testresult_lab
request_triage_nurse
view_triage_nurse
request_drug_pharm 
#lab
record_labresult
#nurse
record_triage
#pharm
dispense_drugs
"""

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
