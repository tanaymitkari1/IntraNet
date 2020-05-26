from django.contrib import admin
from django.urls import path
from placement.views import *

urlpatterns = [
    path('', index, name='placement'),
    path('add_placements/', add_placement, name="add_placement"),
    path('create_placement/', create_placement, name="create_placement"),
    path('answer_backup/', answer_backup, name="backup"),
    path('add_choice/', add_choice, name="add_choice"),
    path('<int:id>/details/', details, name="placement_details"),
    path('<int:id>/answer/', answer, name="answer"),
    path('<int:id>/', single_choice, name="single_choice"),
    path('<int:id>/delete/', placement_delete, name="placement_delete"),
]
