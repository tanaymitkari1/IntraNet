from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Placements(models.Model):
    title = models.CharField(null=True, blank=True, max_length=50)
    information = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    start_date = models.CharField(null=True, blank=True, max_length=50)
    end_date = models.CharField(null=True, blank=True, max_length=50)
    start_time = models.CharField(null=True, blank=True, max_length=50)
    end_time = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.title

    @property
    def choices(self):
        return self.choice_set.all()


class Choice(models.Model):
    placement = models.ForeignKey('placement.Placements', on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    @property
    def votes(self):
        return self.answer_set.count()


class Answer(models.Model):
    placement = models.ForeignKey(Placements, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    username = models.CharField(null=True, blank=True, max_length=50)
    firstname = models.CharField(null=True, blank=True, max_length=50)
    lastname = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cv_upload = models.FileField(upload_to='cv/', null=True, blank=True)


    def __str__(self):
        return self.user.username