from typing import Reversible
from django.db import models
from django.urls import reverse


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(decimal_places=3,max_digits=1000)
    active = models.BooleanField(default=True)


    def get_absolute_url(self):
        return reverse('articles:article-detail',kwargs={'id': self.id})
