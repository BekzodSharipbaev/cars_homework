from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest

from .models import Car

# Create your views here.
def addCar(request: HttpRequest):
    if request.method == 'POST':
        tmp = request.POST.dict()
        del tmp['csrfmiddlewaretoken']
        Car.objects.create(**tmp)
        return redirect('home')
    return render(request, 'index.html')


def carsPage(request: HttpRequest):
    context = {'cars': Car.objects.all()}
    return render(request, 'data.html', context)

