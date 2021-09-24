from django.shortcuts import redirect, render,get_object_or_404
from django.views import View 
from .models import Course
from .forms import CourseModelForm
#Base VIEW class = View

class CourseObjectMixin(object):
    model = Course
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None  
        if id is not None:
            obj=get_object_or_404(self.model, id= id)
        return obj

class CourseDeleteView(CourseObjectMixin, View):
    template_name='courses/courses_delete.html'

    def get(self,request,id=None,*args,**kwargs):
        context={}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object']=obj
            context['form']= form
        return render(request,self.template_name,context)

    def post(self,request,id=None,*args,**kwargs):
        context={}
        obj=self.get_object()
        if obj is not None:
                obj.delete()
                context['object']=None
                return redirect('/courses/') 
        return render(request,self.template_name,context)

    
class CourseUpdateView(CourseObjectMixin,View):
    template_name='courses/courses_update.html'


    def get(self,request,id=None,*args,**kwargs):
        context={}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object']=obj
            context['form']= form
        return render(request,self.template_name,context)

    def post(self,request,id=None,*args,**kwargs):
        context={}
        obj=self.get_object()
        if obj is not None:
                form= CourseModelForm(request.POST, instance=obj)
                if form.is_valid():
                    form.save()
                context['object']=obj
                context['form']=form
        return render(request,self.template_name,context)    


class CourseCreateView(View):
    template_name = 'courses/courses_create.html'
    def get(self, request, id=None, *args, **kwargs):
        #GET method
        form = CourseModelForm()
        context = {"form":form}
        return render(request,self.template_name,context)
    
    def post(self, request, *args, **kwargs):
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {"form":form}
        return render(request,self.template_name,context)

class CourseListView(View):
    template_name='courses/courses_list.html'
    queryset= Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self,request,*args,**kwargs):
        context = { 'object_list':self.get_queryset()}
        return render(request,self.template_name,context)

class CourseView(CourseObjectMixin, View):
    template_name = 'courses/courses_detail.html'
    def get(self, request, id=None, *args, **kwargs):
        context = {'object': self.get_object}
        return render(request,self.template_name,context)

    # def post(request, *args, **kwargs):
    #     return render(request,'about.html',{})

#HTTP methods
def my_fbv(request, *args, **kwargs):
    return render(request,'about.html',{})