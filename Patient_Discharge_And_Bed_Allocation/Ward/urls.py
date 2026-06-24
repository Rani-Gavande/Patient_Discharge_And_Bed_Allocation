from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('add-ward/', views.add_Ward, name='add_Ward'),
    path('ward/<int:id>/', views.ward_beds, name='ward_beds'), 
]
