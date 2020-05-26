from django.db import models

# Create your models here.
class adypu_data(models.Model):
    subject_name = models.CharField(null=True, blank=True, max_length=100)
    subject_code = models.CharField(null=True, blank=True, max_length=100)
    course_type = models.CharField(null=True, blank=True, max_length=100)
    year_of_coding = models.CharField(null=True, blank=True, max_length=100)
    school_name = models.CharField(null=True, blank=True, max_length=100)
    specialization = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.subject_name