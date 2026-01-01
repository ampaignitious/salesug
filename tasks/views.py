from django.shortcuts import render
from . models import Task
# Create your views here.
def home(request):
    alltasks = Task.objects.all()
    total =Task.objects.count()
    context={"alltasks":alltasks,
             "total":total             
             }
    return render(request, 'tasks/home.html', context)


def detailpage(request, taskID):
    taskDetails= Task.objects.get(pk=taskID)
    context={
        "taskDetails":taskDetails
    }
    return render(request, 'tasks/detail.html', context)