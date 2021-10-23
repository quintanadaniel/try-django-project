from django.contrib import admin
from django.contrib.admin.decorators import register

# Register your models here.
from .models import Product

admin.site.register(Product)