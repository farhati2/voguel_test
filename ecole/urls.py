from django.contrib import admin
from django.urls import path
from . import views


urlpatterns=[
    path('', views.description_create_view, name='description'),
    path('aj/load-niveaux/', views.load_niveaux, name='ajax_load_niveaux'),
    path('aj/load-classes/', views.load_classe, name='ajax_load_classes'),
    path('list/',views.list_ligne_description, name='list_ligne_description' ),
    
    
    
   
]