from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.school_name

    def get_absolute_url(self):
        return reverse("basic_app:detail", kwargs={'pk':self.pk})

class Student(models.Model):
    sname = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    school_name = models.ForeignKey(School, related_name='students', on_delete='Cascade')

    def __str__(self):
        return self.sname
