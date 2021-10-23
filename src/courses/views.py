from django.shortcuts import render, get_object_or_404,redirect
from django.views import View

from .forms import  CourseModelForm
from .models import Course
#BASE VIEW Class = VIEW

class CourseObjectMixin(object):
    model = Course # what ever model do you created
    #lookup = 'id' # field about object create in the model that you used

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model,id=id)
        return obj

class CourseDeleteView(CourseObjectMixin, View):
    template_name = 'courses/course_delete.html'
    # I comment below lines because I use the class up and apply inherienty
    #def get_object(self):
    #    id = self.kwargs.get('id')
    #    obj = None
    #    if id is not None:
    #        obj = get_object_or_404(Course,id=id)
    #    return obj

    def get(self, request, id=None, *args, **kargs):
        #GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kargs):
        #POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses/')
        return render(request, self.template_name, context)


class CourseUpudateView(CourseObjectMixin, View):
    template_name = 'courses/course_update.html'

    #def get_object(self):
    #    id = self.kwargs.get('id')
    #    obj = None
    #    if id is not None:
    #        obj = get_object_or_404(Course,id=id)
    #    return obj

    def get(self, request, id=None, *args, **kargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request,self.template_name, context)


    def post(self, request, id=None, *args, **kargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request,self.template_name, context)


class CourseCreateView(View):
    template_name = 'courses/course_create.html'
    
    #GET methods
    def get(self, request, *args, **kargs):
        form = CourseModelForm()
        context = {'form':form}
        return render(request, self.template_name, context)

    #POST methods
    def post(self, request, *args, **kargs):
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {'form':form}
        return render(request, self.template_name, context)


class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kargs):
        context = {'object_list':self.get_queryset()}
        return render(request, self.template_name, context)


#Used the class CourseListView how to inherirenty to filter the data
class MyListFilterView(CourseListView):
    queryset = Course.objects.filter(id=1)


class CourseView(CourseObjectMixin, View):
    template_name = 'courses/course_detail.html'
    def get(self, request, id=None, *args, **kargs):
        #GET method
        context = {'object':self.get_object()}
        # comment the lines below because I imported the clas CourseObject
        #if id is not None:
        #    obj = get_object_or_404(Course,id=id)
        #    context['object'] = obj
        return render(request, self.template_name, context)

    #def post(self, request, *args, **kargs):
    #    return render(request,'about.html',{})


#HTTP Methods
def my_fbv(request,*args,**kargs):
    print(request.method)
    return render(request,'about.html',{})