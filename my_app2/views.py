from django.shortcuts import render, redirect
from .forms import BikeForm
from .models import Bike
def home(request):
    obj=Bike.objects.all()
    context={
        'obj': obj
    }
    return render(request, 'home.html', context)

def add(request):
    return render(request, 'new.html')

def Save(request):
    x=BikeForm(request.GET)
    if x.is_valid():
        x.save()
        return redirect('/home')
    else:
        context={'error':x}
        return render(request, 'new.html')

def delete(request, id):
    Bike.objects.get(id=id).delete()
    return redirect('/home')

def change(request, id):
    obj=Bike.objects.get(id=id)
    context={
        'obj':obj
    }
    return render(request, 'change.html', context)

def update(request, id):
    obj=Bike.objects.get(id=id)
    x=BikeForm(request.GET, instance=obj)
    if x.is_valid():
        x.save()
        return redirect('/home')
    else:
        context={'error': x, 'obj':obj}
        return render(request, 'change.html', context)

# Create your views here.
