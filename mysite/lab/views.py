from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
# from django.shortcuts import render

from django.conf import settings
from django.shortcuts import redirect
from django.db.models import Count, Avg, Sum
# Create your views here.

from .models import Labpower
from .models import Labinfo
from .models import Teacher
from .models import Student
from .models import Labtest

from .models import PrjSpec



def labpower(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
        
    item_list = Labpower.objects.order_by('f01')[:400]
    context = {'current_user':request.user,'page_title':'Power','item_list': item_list}
    #使用ITEM005  template
    return render(request, 'lab/labpower.html', context)  
    
def labinfo(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
        
    item_list = Labinfo.objects.order_by('f01')[:400]
    context = {'current_user':request.user,'page_title':'Lab Info','item_list': item_list}
    #使用ITEM005  template
    return render(request, 'lab/labinfo.html', context)  
    
def teacher(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
        
    item_list = Teacher.objects.order_by('f01')[:400]
    context = {'current_user':request.user,'page_title':'Lab Teacher','item_list': item_list}
    #使用ITEM005  template
    return render(request, 'lab/teacher.html', context)  
    
def student(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
        
    item_list = Student.objects.order_by('f01')[:400]
    context = {'current_user':request.user,'page_title':'Lab Student','item_list': item_list}
    #使用ITEM005  template
    return render(request, 'lab/Student.html', context)  

def labtest(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
        
    item_list = Labtest.objects.order_by('f01')[:400]
    context = {'current_user':request.user,'page_title':'Lab Teacher','item_list': item_list}
    #使用ITEM005  template
    return render(request, 'lab/labtest.html', context)  
    
def prj_spec(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
        
    item_list = PrjSpec.objects.order_by('f00')[:400]
    context = {'current_user':request.user,'page_title':'Project Spec','item_list': item_list}
    #使用ITEM005  template
    return render(request, 'lab/prj_spec.html', context)  
    
    