from django.shortcuts import render
from django.contrib import messages
from . models import Task
from . forms import taskcreateform
# Create your views here.

def home(request):
    alltasks = Task.objects.all()
    total =Task.objects.count()
    alldatacontext={"alltasks":alltasks,
         "total":total             
        }
    return render(request, 'tasks/home.html', alldatacontext)


def detailpage(request, taskID):
    taskDetails= Task.objects.get(pk=taskID)
    context={
        "taskDetails":taskDetails
    }
    return render(request, 'tasks/detail.html', context)

def createtaskform(request):
    if request.method =="POST":
        form =taskcreateform(request.POST)
        if form.is_valid():
            taskname=form.cleaned_data.get('name')
            description=form.cleaned_data.get('description')
            taskstatus=form.cleaned_data.get('task_status')
            obj = Task.objects.create(
                name=taskname,
                description=description,
                task_status=taskstatus
            )
            obj.save()
            alltasks = Task.objects.all()
            total =Task.objects.count()
            alldatacontext={"alltasks":alltasks,
                            "total":total             
                             }
            return render(request, 'tasks/home.html', alldatacontext)
    else:
        alltasks = Task.objects.all()
        form  = taskcreateform()
        total =Task.objects.count()
        context={"alltasks":alltasks,
                "total":total,
                "form":form          
                }
        return render(request, 'tasks/taskpage.html', context)
    
def deletetask(request, taskID):
    taskDetails= Task.objects.get(pk=taskID)
    taskDetails.delete()

    messages.success(request, f'{taskDetails.name} has been deleted successfully.')
    alltasks = Task.objects.all()
    form  = taskcreateform()
    total =Task.objects.count()
    context={"alltasks":alltasks,
                "total":total,
                "form":form,         
                }
    return render(request, 'tasks/home.html', context)