from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(decimal_places=3,max_digits=1000)
    summary = models.TextField(blank=False,null=False)
    featured= models.BooleanField(default=False)


    def get_absolute_url(self):
        return f'/products/{self.id}/'

    def get_reverse_url(self):
        return reverse('products:products-detail',kwargs={'id': self.id})