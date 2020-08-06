from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', myprofile, name="myprofile"),
    path('subject/', add_sub, name="subject_add"),
    path('credit_registration/', sub_list, name="credit_registration"),
    path('certi/', certi, name="certi"),
    path('<int:id>/delete/', del_sub, name="delete_sub"),
    path('<int:id>/certificate_delete/', certi_delete, name="certificate_delete"),
]