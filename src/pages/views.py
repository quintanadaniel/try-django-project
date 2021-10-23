from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kargs):
    return render(request,'home.html',{})

def contact_view(request,*args,**kargs):
    return render(request,'contact.html',{})

def about_view(request,*args,**kargs):
    my_context = {
        'title':'abc this is a title',
        'my_text':'this is about us',
        'my_number':123,
        'my_list':[123,23,'pelota'],
        'my_html':'<h1>Hello World</h1>'
    }
        
    return render(request,'about.html', my_context)