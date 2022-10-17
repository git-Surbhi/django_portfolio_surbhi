from django.shortcuts import render
from . import models
from django.shortcuts import get_object_or_404


def project_index(request):
    projects = models.Project.objects.all()
    return render(request, 'projects/index.html', {'project_post':projects})


def single_proj(request , id):
    project = get_object_or_404(models.Project , pk = id)
    return render(request, 'projects/pro.html',{'object':project})




