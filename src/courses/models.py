from django.db import models
from django.urls import reverse


# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    credit = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    #def get_absolute_url(self):
    #    return reverse('courses:courses-detail',kwargs={'id': self.id})

    #def get_reverse_url(self):
    #    return reverse('courses:courses-detail',kwargs={'id': self.id})