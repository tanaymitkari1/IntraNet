from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', myprofile, name="myprofile"),
    path('subject/', add_sub, name="subject_add"),
]