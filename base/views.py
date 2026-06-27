from django.shortcuts import render,redirect
from .models import TaskModel
from django.db.models import Q

# Create your views here.

def home(request):
    # if 'q' in request.GET:
    #     q = request.GET['q']
    #     tasks = TaskModel.objects.filter(Q(title__icontains = q),Q(completed=False),Q(is_deleted=False),Q(request.User))
    # else:    
    q = request.GET.get('q')

    tasks = TaskModel.objects.filter(
        user=request.user,
        completed=False,
            is_deleted=False
    )
    if q:
        tasks = tasks.filter(
            Q(title__icontains=q) | Q(desc__icontains=q)
        )

    return render(request, 'home.html', {'tasks': tasks})


def add(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']

        TaskModel.objects.create(
            user=request.user,
            title=title,
            desc=desc
        )

        return redirect('home')
    return render(request,'add.html')

def complete(request):
    q = request.GET.get('q')
    tasks = TaskModel.objects.filter(
        user=request.user,
        completed=True,
        is_deleted=False
    )
    if q:
        tasks = tasks.filter(
            Q(title__icontains=q) | Q(desc__icontains=q)
        )
    return render(request,'complete.html',{'tasks': tasks})

def trash(request):

    q = request.GET.get('q')

    
   
    tasks = TaskModel.objects.filter(Q(user=request.user,completed=True,is_deleted=True) | Q(user=request.user,is_deleted=True))
    if q:
        tasks = tasks.filter(
            Q(title__icontains=q) | Q(desc__icontains=q)
        )
    
    data = tasks.count()
    return render(request,'trash.html',{'tasks': tasks,'count': data,})

def about(request):
    return render(request,'about.html')


def hcompleted(request,pk):
    task = TaskModel.objects.get(id=pk, user=request.user)
    task.completed = True
    task.save()
    return redirect('home')

def hdelete(request,pk):
    task = TaskModel.objects.get(id=pk, user=request.user)
    task.is_deleted = True
    task.save()
    return redirect('home')


def cdelete(request,pk):
    task = TaskModel.objects.get(id=pk, user=request.user)
    task.is_deleted = True
    task.save()
    return redirect('complete')

def crestore(request,pk):
    task = TaskModel.objects.get(id=pk, user=request.user)
    task.completed = False
    task.save()
    return redirect('complete')

def cdelete(request,pk):
    task = TaskModel.objects.get(id=pk, user=request.user)
    task.is_deleted = True
    task.save()
    return redirect('complete')

def crestore(request,pk):
    task = TaskModel.objects.get(id=pk, user=request.user)
    task.completed = False
    task.save()
    return redirect('complete')


def ddelete(request,pk):
    task = TaskModel.objects.get(id=pk).delete()
    return redirect('trash')

def drestore(request,pk):
    task = TaskModel.objects.get(id=pk, user=request.user)
    task.is_deleted = False
    task.completed = False
    task.save()
    return redirect('trash')



def  hdelete_all(request):
    task = TaskModel.objects.all()
    for i in task:
        i.is_deleted = True
        i.save()
    return redirect('home')


def  hcomplete_all(request):
    task = TaskModel.objects.filter(user = request.user,is_deleted = False)
    for i in task:
        i.is_completed = True
        i.save()
    return redirect('home')