from django import forms

from django.http import Http404, request
from django.shortcuts import render,get_object_or_404,redirect

from .models import Product

from .forms import ProductForm,RawProductForm


# Create your views here.

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form':form
    }

    return render(request, 'products/product_create.html', context)


def product_update_view(request, id=id):
    obj = get_object_or_404(Product,id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request,'products/product_create.html',context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list':queryset
    }
    return render(request,'products/product_list.html',context)


def product_detail_view(request, id):
    obj = get_object_or_404(Product,id=id)
    context = {
        'object':obj
    }
    return render(request,'products/product_detail.html', context)


def product_delete_view(request,id):
    obj = get_object_or_404(Product,id=id)
    #POST request
    if request.method == 'POST':
        #Confirming delete
        obj.delete()
        return redirect('../../')

    context = {
        'object':obj
    }
    return render(request,'products/product_delete.html',context)
    

def dynamic_lookup_view(request,id):
    #obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product,id=id) # this methods is prefer because less lines
    print(obj)
    # this other form to catch error when page not foud or data not found
    #obj = Product.objects.get(id=id)
    #try:
    #    obj = Product.objects.get(id=id)
    #except Product.DoesNotExist:
    #    raise Http404

    context = {
        'object':obj
    }
    print(context)
    return render(request,'products/product_detail.html',context)





