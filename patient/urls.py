from django.urls import path
from . import views

urlpatterns = [
	path('register_patient/', views.register_patient, name='register_patient'),
    path('', views.patients, name= 'patients'),
    path('<int:patient_id>/', views.patient_detail, name='patient_detail'),
	path('update/<int:patient_id>/', views.update_patient, name='update_patient'),
	path('delete/<int:patient_id>/', views.delete_patient, name='delete_patient'),
    
	# path('', views.contribution_mgr, name= 'contribution_mgr'),
	# path('contribution/<int:customer_id>/', views.customer_contribution, name='customer_contribution'),
	# path('withdrawal/<int:customer_id>/', views.customer_withdrawal, name='customer_withdrawal'),
	# path('contribution-record/', views.contribution_record, name='contribution_record'),
	# path('<int:customer_id>/', views.contribution_detail, name='contribution_detail'),
	# path('update/<int:customer_id>/', views.update_contribution, name='update_contribution'),
	# path('delete/<int:customer_id>/', views.delete_contribution, name='delete_contribution'),
	# path('contrb_percustomer/<int:customer_id>/', views.contribution_percustomer, name='contribution_percustomer'),
	# path('all_custcontrb_balance/', views.all_custcontrb_balance, name='all_custcontrb_balance'),
]