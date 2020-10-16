from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request,'jobsApp/index.html')

def hydjobsinfo(request):
    hydjobs_list=hydjobs.objects.order_by('date')
    my_dict={'hydjobs_list':hydjobs_list}
    return render(request,'jobsApp/hyd.html',context=my_dict)

def punejobsinfo(request):
    return render(request, 'jobsApp/pune.html')

def mumbaijobsinfo(request):
    return render(request, 'jobsApp/chnn.html')

def bangjobsinfo(request):
    return render(request, 'jobsApp/bng.html')

