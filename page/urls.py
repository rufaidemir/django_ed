from django.contrib import admin
from django.urls import path
from .views import (corusel_create, carousel_list, carousel_update, manage, page_list,page_create, page_update, page_delete)
app_name= 'carousel'

urlpatterns = [
    path('corusel_index/', carousel_list, name='corusel_index'), 
    path('corusel_create/', corusel_create, name='corusel_create'), 
    path('corusel_update/<int:pk>/', carousel_update, name='corusel_update'), 
    #manage
    path('', manage, name='manage'), 
    
    #page
    path('page/list/', page_list, name='page_list'), 
    path('page/create/', page_create, name='page_create'), 
    path('page/update/<int:pk>/', page_update, name='page_update'), 
    path('page/delete/<int:pk>/', page_delete, name='page_delete'), 
    
]