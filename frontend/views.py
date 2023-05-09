from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

from userprofile.models import Userprofile
from personnel.models import Doctor, Labscientist, Nurse, Pharmacist
from patient.models import Patient
# from account.models import Company_account

COMPANY = "Beyond's Healthcare and Fertility Center"

def index(request):
	patients = Patient.objects.all()
	return render(request, 'frontend/homepage.html', {'patients': patients, 'company': COMPANY})

def dashboard(request):
	patients = Patient.objects.all()
	count_patients = Patient.objects.count()

	count_doctors = Doctor.objects.count() 
	count_labscientists = Labscientist.objects.count()
	count_nurses = Nurse.objects.count()  
	count_pharmacists = Pharmacist.objects.count() 
	count_users = count_patients.count() + count_doctors.count() + count_labscientists.count() + count_nurses.count() + count_pharmacists.count()

	# company_account = Company_account.objects.latest('id')
	# print(company_account)

	return render(request, 'frontend/dashboard.html', {'patients': patients, 'count_patients': count_patients, 
		'count_users': count_users, 'count_doctors': count_doctors, 'count_labscientists': count_labscientists, 
		'count_nurses': count_nurses, 'count_pharmacists': count_pharmacists, 'company': COMPANY})
	#return redirect('login')

@login_required
def create_account(request):
	pass
	# if request.method == 'POST':
	# 	form = UserCreationForm(request.POST)

	# 	if form.is_valid():
	# 		user = form.save()
	# 		account_type = request.POST.get('account_type', 'customer')
	# 		first_name = request.POST.get('first_name')
	# 		last_name = request.POST.get('last_name')
	# 		name = f"{first_name} {last_name}"
	# 		created_by = request.POST.get('created_by')

	# 		if account_type == 'mgr':
	# 			userprofile = Userprofile.objects.create(user=user, is_mgr=True, first_name=first_name, last_name=last_name, created_by=created_by)
	# 			managerprofile = Manager.objects.create(user=user, name=name, created_by=created_by)
	# 			userprofile.save()
	# 			managerprofile.save()
	# 		elif account_type == 'teller':
	# 			userprofile = Userprofile.objects.create(user=user, is_teller=True, first_name=first_name, last_name=last_name, created_by=created_by)
	# 			tellerprofile = Teller.objects.create(user=user, name=name, created_by=created_by)
	# 			userprofile.save()
	# 			tellerprofile.save()
	# 		else:
	# 			userprofile = Userprofile.objects.create(user=user, is_cust=True, first_name=first_name, last_name=last_name, created_by=created_by)
	# 			customerprofile = Customer.objects.create(user=user, name=name, created_by=created_by)
	# 			userprofile.save()
	# 			customerprofile.save()

	# 		msg_title = 'New Record!'
	# 		msg_text = 'User has been created successfully!'
	# 		messages.add_message(request, messages.SUCCESS, msg_text, extra_tags=msg_title)

	# 		#login(request, user)
	# 		#return redirect('index')
	# 		return redirect('create_account')

	# 	else:
	# 		msg_title = 'Error!'
	# 		msg_text = 'Record was NOT saved!'
	# 		messages.add_message(request, messages.ERROR, msg_text, extra_tags=msg_title)

	# else:
	# 	form = UserCreationForm()
	# return render(request, 'frontend/create_account.html', {'form': form, 'company': COMPANY})
