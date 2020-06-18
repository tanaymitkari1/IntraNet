from django.db import models
from django.contrib.auth.models import User
from .models import *

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True)
    #sub = models.ManyToManyField(Subject)

    def __str__(self):
        return self.user

class Subject(models.Model):
    name = models.CharField(null=True, blank=True, max_length=50)
    credit = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name