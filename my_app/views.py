from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employees
def index(request):
    search  =  request.GET.get('search')
    if search:
        obj=Employees.objects.filter(name__icontains=search)
    else:
        obj=Employees.objects.all()
    context={
        'obj':obj
    }
    return render(request, 'index.html', context)

def add(request):
    return render(request, 'add.html')

def delete(request, id):
    Employees.objects.get(id=id).delete()
    return redirect('/')

def Save(request):
    x=EmployeeForm(request.GET)
    if x.is_valid():
        x.save()
        return redirect('/')
    else:
        context={'error': x}
        return render(request, 'add.html', context)

def edit(request, id):
    obj=Employees.objects.get(id=id)
    context={
        'obj':obj
    }
    return render(request, 'edit.html', context)

def update(request, id):
    obj=Employees.objects.get(id=id)
    x=EmployeeForm(request.GET, instance=obj)
    if x.is_valid():
        x.save()
        return redirect('/')
    else:
        context={'error':x, 'obj':obj}
        return render(request, 'edit.html', context)
# Create your views here.
