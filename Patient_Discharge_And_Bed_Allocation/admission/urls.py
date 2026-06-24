from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('add-patient/', views.add_patient, name='add_patient'),
    path('add-doctor/',views.add_doctor,name='add_doctor'), 
]
