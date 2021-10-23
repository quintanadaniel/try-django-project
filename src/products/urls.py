"""trydjangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from products.views import (product_create_view, product_detail_view,dynamic_lookup_view, product_delete_view, product_list_view, product_update_view)

app_name = 'products'
urlpatterns = [
    path('',product_list_view,name='product-list'),
    path('create/',product_list_view,name='product-list'),
    path('<int:id>/',product_detail_view,name='product-detail'),
    path('<int:id>/update/',product_update_view,name='product-update'),
    path('<int:id>/delete/',product_delete_view,name='product-delete'),

]
