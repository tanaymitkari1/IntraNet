from django.contrib import admin
from django.urls import path, include
from . views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', index_bos, name="BOS"),
    path('input_bos/', input_bos, name="input_bos"),
]