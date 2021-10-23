from django import forms

from django.http import Http404, request
from django.shortcuts import render,get_object_or_404,redirect

from .models import Product

from .forms import ProductForm,RawProductForm


# Create your views here.

# With this method initialized default values in the text box in our django application
def render_initial_data(request):
    inital_data = {
        'title':'My this awesome title'
    }
    obj = Product.objects.get(id=4)
    form =ProductForm(request.POST or None, initial='Initial data test',instance=obj)
    if form.is_valid():
        form.save()
    conext = {
        'form':form
    }
    return render(request,'products/product_create.html',conext)


#def product_create_view(request):
#    my_form = RawProductForm()
#    if request.method == 'POST':
#        my_form = RawProductForm(request.POST)
#        if my_form.is_valid():
#            print(my_form.cleaned_data)
#            Product.objects.create(**my_form.cleaned_data)
#        else:
#            print(my_form.errors)
#    context = {
#        'form':my_form
#    }
#    return render(request,'products/product_create.html', context)

# we used the methods POST and GET and how to complement with the template and how to combine with property in the html form action='web page'
#def product_create_view(request):
#    context = {}
#    return render(request,'products/product_create.html', context)


# we used easy form about the form.py
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form':form
    }

    return render(request, 'products/product_create.html', context)


def product_detail_view(request):
    obj = Product.objects.get(id=3)
    #context = {
    #    'title':obj.title,
    #    'description':obj.description,
    #    'price':obj.price,
    #    'summary':obj.summary
    #}

    context = {
        'object':obj
    }
    return render(request,'products/product_detail.html', context)


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


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list':queryset
    }
    return render(request,'products/product_list.html',context)