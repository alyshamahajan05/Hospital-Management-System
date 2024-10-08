from django.urls import path
from .views import Home, About, Contact, Login, Logout_admin, Index,View_doctor,Delete_doctor,AddDoctor,View_Patient,Delete_patient,Add_Patient,Delete_appointment,View_Appointment,Add_Appointment

urlpatterns = [
    path('', Home, name='Home'), 
    path('about/', About, name='About'), 
    path('contact/', Contact, name='Contact'), 
    path('login/', Login, name='login'),
    path('logout/', Logout_admin, name='logout_admin'),  
    path('index/', Index, name='dashboard'), 
    path('view_doctor/', View_doctor, name='view_doctor'), 
    path('add_doctor/', AddDoctor, name='add_doctor'), 
    path('Delete_doctor(?p<int:pid>)/', Delete_doctor, name='delete_doctor'), 
    path('Delete_patient(?p<int:pid>)/', Delete_patient, name='delete_patient'), 
    path('Delete_appointment(?p<int:pid>)/', Delete_appointment, name='delete_appointment'), 
    path('view_patient/', View_Patient, name='view_patient'),
    path('add_patient/', Add_Patient, name='add_patient'),
    path('view_appointment/', View_Appointment, name='view_appointment'),
    path('add_appointment/', Add_Appointment, name='add_appointment'),
   
]
