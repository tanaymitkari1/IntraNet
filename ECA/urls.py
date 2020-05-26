from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', eca, name="eca"),
    path('add_workshop/', add_workshop, name="add_workshop"),
    path('<int:id>/details/', workshop_details, name="workshop_details"),
    path('<int:id>/workshop_delete/', workshop_delete, name="workshop_delete"),
]