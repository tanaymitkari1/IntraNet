from django.db import models
from django.contrib.auth.models import User
from . models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.
"""
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='UserProfile', null=True, blank=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def user_is_created(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.UserProfile.save()
"""

class Subject(models.Model):
    name = models.CharField(null=True, blank=True, max_length=50)
    code = models.CharField(null=True, blank=True, max_length=50)
    credit = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default='user.png')
    price = models.FloatField(null=True, blank=True, default=12.89)


    def __str__(self):
        return self.name

class credit_reg(models.Model):
    student = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    name_subjects = models.ManyToManyField(Subject, blank=True)

    def __str__(self):
        return self.student.username


class certificates(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username