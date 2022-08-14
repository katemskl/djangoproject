from django.shortcuts import render

# Create your views here.
from .models import Car


def first(request):
    quaaryset = Car.objects.all()
    return render(request, 'index.html', context={'car_list': quaaryset})
