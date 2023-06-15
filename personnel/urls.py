from django.urls import path
from . import views

urlpatterns = [
	#doctor
	path('write_note_soap/', views.write_note_soap, name='write_note_soap'),
    path('view_notes_soap/', views.view_notes_soap, name= 'view_notes_soap'),
	path('request_labtest_lab/', views.request_labtest_lab, name='request_labtest_lab'),
    path('request_drug_dispensing/', views.request_drug_dispensing, name='request_drug_dispensing'),
	path('request_triage_nurse/', views.request_triage_nurse, name='request_triage_nurse'), 

	# #lab
	path('labresult/', views.labresult, name='labresult'),
    path('update_labresult/<int:req_labtest_id>/', views.update_labresult, name='update_labresult'),
    path('view_labresult/<int:req_labtest_id>/', views.view_labresult, name='view_labresult'),

    #nurse
	path('record_triage/', views.record_triage, name='record_triage'),
    path('view_triage/', views.view_triage, name='view_triage'),
    
    # #pharm
	path('dispense_drugs/', views.dispense_drugs, name='dispense_drugs'),
    path('view_drugs/<int:req_drugs_id>/', views.view_drugs, name='view_drugs'),
    path('update_drugs/<int:req_drugs_id>/', views.update_drugs, name='update_drugs'),
]