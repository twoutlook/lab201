from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
# from django.shortcuts import render

from django.conf import settings
from django.shortcuts import redirect
from django.db.models import Count, Avg, Sum
# Create your views here.

from .models import Power

def power(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
        
    item_list = Power.objects.order_by('f01')[:400]
    context = {'current_user':request.user,'page_title':'Power','item_list': item_list}
    #使用ITEM005  template
    return render(request, 'lab/power.html', context)  