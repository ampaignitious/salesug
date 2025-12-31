from django.shortcuts import render
from . models import Task
# Create your views here.
def home(request):
    alltasks = Task.objects.all()
    context={"alltasks":alltasks}
    print(context)
    return render(request, 'tasks/home.html', context)


def detailpage(request, pk):
    return render(request, 'tasks/detail.html')