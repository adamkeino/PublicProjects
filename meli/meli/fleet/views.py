from django.shortcuts import render
from django.http import HttpResponse
from fleet.models import Vehicle, Driver
from django.template import loader

def index(request):
    car_list = Vehicle.objects.order_by("id")
    context = {"car_list": car_list}
    return render(request, "fleet/index.html", context)

def detail(request):
    car_list = Vehicle.objects.order_by("id")
    context = {"car_list": car_list}
    return render(request, "fleet/detail.html", context)



