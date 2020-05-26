from django.db import models
from django.conf import settings
from django import forms


# Create your models here.
class add_eca(models.Model):
    title = models.CharField(null=True, blank=True, max_length=50)
    information = models.TextField(null=True, blank=True)
    start_date = models.CharField(null=True, blank=True, max_length=50)
    end_date = models.CharField(null=True, blank=True, max_length=50)

    
    def __str__(self):
        return self.title


