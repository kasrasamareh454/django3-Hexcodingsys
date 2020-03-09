
from django.shortcuts import render , get_object_or_404

from .models import Projrcts

# Create your views here.

def projjects(request) :
    
    projects = Projrcts.objects.order_by('-date')
    
    return render(request , 'ourprojects/projectss.html' , {'projects' : projects})

def detail(request , project_id) :
    project = get_object_or_404(Projrcts , pk=project_id)
    return render(request , 'ourprojects/detail.html' , {'project' : project})