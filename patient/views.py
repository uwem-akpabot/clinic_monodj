from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from patient.models import Patient
# from .models import Contribution, Cust_contrb, Account, Withdrawal
# from account.models import Company_account, Admin_total_funds
from .forms import AddPatientForm
from django.contrib import messages

company = "Beyond's Healthcare and Fertility Center"

@login_required
def register_patient(request):
	patients = Patient.objects.all()

	if request.method == 'POST':
		form = AddPatientForm(request.POST) 
		if form.is_valid():
			form_valid(request, form, 'Patient', 'New Record!')
			# additional codes here
			return redirect('register_patient')
		else:
			form_not_valid(request)
	else:
		form = AddPatientForm() 
		pass_data = {'form': form, 'company':company, 'patients':patients}
	return render(request, 'patient/register_patient.html', pass_data)


@login_required
def patients(request):
	patients = Patient.objects.all()
	return render(request,'patient/patients.html', {'company':company, 'patients': patients})

#Get detail by Id
@login_required
def patient_detail(request, patient_id):
	patient = Patient.objects.get(pk=patient_id)
	return render(request, 'patient/patient_detail.html', {'company':company, 'patient': patient})

#Update record
@login_required
def update_patient(request, patient_id):
	patient = Patient.objects.get(pk=patient_id)
	form = AddPatientForm(instance=patient)

	if request.method == 'POST':
		form = AddPatientForm(request.POST, instance=patient) #if submit is click and form method is POST

		if form.is_valid():
			customer = form.save() #save to database

			msg_title = 'Updated!'
			msg_text = 'Patient is saved successfully!'
			messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)
			return redirect('patients')
		else:
			msg_title = 'Error!'
			msg_text = 'Record was NOT saved!'
			messages.add_message(request, messages.ERROR, msg_text, extra_tags=msg_title)
	else:
		form = AddPatientForm() #if submit is not clicked, display empty form

	return render(request, 'patient/update_patient.html', {'form': form, 'company':company, 'patient': patient})

#Delete record
@login_required
def delete_patient(request, patient_id):
	patient = Patient.objects.get(pk=patient_id)

	if request.method == 'POST':
		patient.delete()

		msg_title = 'Deleted!'
		msg_text = 'Patient was deleted successfully!'
		messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)
		return redirect('patients')
	return render(request, 'patient/delete_patient.html', {'company':company, 'patient': patient})

# Misc function
def form_valid(request, form, subject, msg):
	form.save() 
	msg_title = msg
	msg_text = f'{subject} is saved successfully!'
	messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)

# Misc function
def form_not_valid(request):
	msg_title = 'Error!'
	msg_text = 'Record was NOT saved!'
	messages.add_message(request, messages.ERROR, msg_text, extra_tags=msg_title)

"""

@login_required
def contribution_percustomer(request, customer_id):
	contrb_percustomer = Contribution.objects.filter(customer_id=customer_id)
	customer = Customer.objects.get(pk=customer_id)
	return render(request,'contribution/contrb_percustomer.html', {'company':company, 'contrb_percustomer': contrb_percustomer, 'customer': customer})

@login_required
def contribution(request):
	contributions = Contribution.objects.all()
	customers = Customer.objects.all()
	return render(request,'contribution/contribution.html', {'company':company, 'contributions': contributions, 'customers': customers})

@login_required
def all_custcontrb_balance(request):
	custcontrb = Cust_contrb.objects.all()
	return render(request,'contribution/all_custcontrb.html', {'company':company, 'custcontrb': custcontrb})

@login_required
def update_contribution(request, contribution_id):
	customer = Customer.objects.get()
	contribution = Contribution.objects.get(pk=contribution_id)

	form = AddContributionForm(instance=contribution)

	if request.method == 'POST':
		form = AddContributionForm(request.POST, instance=contribution) #if submit is click and form method is POST

		if form.is_valid():
			contribution = form.save() #save to database
			
			msg_title = 'Updated!'
			msg_text = 'Contribution is saved successfully!'
			messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)
			return redirect('contribution')

		else:
			msg_title = 'Error!'
			msg_text = 'Record was NOT saved!'
			messages.add_message(request, messages.ERROR, msg_text, extra_tags=msg_title)

	else:
		form = AddContributionForm() #if submit is not clicked, display empty form

	return render(request, 'contribution/update_contribution.html', {'form': form, 'company':company, 'customer':customer, 'contribution': contribution})


@login_required
def contribution_detail(request, customer_id):
	customer = Customer.objects.get(pk=customer_id)
	return render(request, 'customer/customer_detail.html', {'company':company, 'customer': customer})


@login_required
def delete_contribution(request, customer_id):
	customer = Customer.objects.get(pk=customer_id)

	if request.method == 'POST':
		customer.delete()

		msg_title = 'Deleted!'
		msg_text = 'Customer was deleted successfully!'
		messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)

		return redirect('customer')

	return render(request, 'customer/delete_customer.html', {'company':company, 'customer': customer})
"""