from django.shortcuts import render
from django.contrib import messages
from . models import Task
from . forms import taskcreateform


#view all tasks
def home(request):
    alltasks = Task.objects.all()
    total =Task.objects.count()
    alldatacontext={"alltasks":alltasks,
         "total":total             
        }
    return render(request, 'tasks/home.html', alldatacontext)


#View a specific task
def detailpage(request, taskID):
    taskDetails= Task.objects.get(pk=taskID)
    context={
        "taskDetails":taskDetails
    }
    return render(request, 'tasks/detail.html', context)

#create a task 
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

#delete a task 
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

#edit a task
def edittask(request, taskID):
    if request.method =="POST":
        taskDetails= Task.objects.get(pk=taskID)
        form =taskcreateform(request.POST, instance=taskDetails)
        if form.is_valid():
            print(form)
            form.save()
            messages.success(request, f'Task edited successfully.')
            alltasks = Task.objects.all()
            total =Task.objects.count()
            alldatacontext={"alltasks":alltasks,
                            "total":total             
                            }
            return render(request, 'tasks/home.html', alldatacontext)
    else:
        taskDetails= Task.objects.get(pk=taskID)
        form =taskcreateform(instance=taskDetails)
        context={
                "taskDetails":taskDetails,
                "editform":True,
                "form":form
        }
        return render(request, 'tasks/detail.html', context)