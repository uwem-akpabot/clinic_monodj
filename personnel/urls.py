from django.urls import path
from . import views

urlpatterns = [
	#doctor
	path('write_note_soap/', views.write_note_soap, name='write_note_soap'),
    path('view_notes_soap/', views.view_notes_soap, name= 'view_notes_soap'),
	path('request_labtest_lab/', views.request_labtest_lab, name='request_labtest_lab'),
    # path('view_testresult_lab/', views.view_testresult_lab, name= 'view_testresult_lab'),
	# path('request_triage_nurse/', views.request_triage_nurse, name='request_triage_nurse'),
    # path('view_triage_nurse/', views.view_triage_nurse, name= 'view_triage_nurse'),
	# path('request_drug_pharm/', views.request_drug_pharm, name='request_drug_pharm'),  

	# #lab
	path('record_labresult/', views.record_labresult, name='record_labresult'),
    path('view_labresult/', views.view_labresult, name='view_labresult'),
    #nurse
	path('record_triage/', views.record_triage, name='record_triage'),
    path('view_triage/', views.view_triage, name='view_triage'),
    # #pharm
	path('dispense_drugs/', views.dispense_drugs, name='dispense_drugs'),
    path('view_dispensed/', views.view_dispensed, name='view_dispensed'),
	
	# path('customer/<int:customer_id>/', views.customer_detail, name='customer_detail'),
	# path('customer/update/<int:customer_id>/', views.update_customer, name='update_customer'),
	# path('customer/delete/<int:customer_id>/', views.delete_customer, name='delete_customer'),
	# #teller
	# path('teller/', views.teller, name='teller'),
	# path('teller/<int:teller_id>/', views.teller_detail, name='teller_detail'),
	# path('teller/update/<int:teller_id>/', views.update_teller, name='update_teller'),
	# path('teller/delete/<int:teller_id>/', views.delete_teller, name='delete_teller'),\
	# #manager
	# path('manager/', views.manager, name='manager'),
	# path('manager/<int:manager_id>/', views.manager_detail, name='manager_detail'),
	# path('manager/update/<int:manager_id>/', views.update_manager, name='update_manager'),
	# path('manager/delete/<int:manager_id>/', views.delete_manager, name='delete_manager'),
]