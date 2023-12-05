from django.shortcuts import render
from django.http import HttpResponse
from .models import Operator

def index(request):
    return HttpResponse("Welcome to our R6 application")

def about(request):
    ops = Operator.objects.all()
    ops_data = []
    for op in ops:
        ops_data.append({"name":op.operator_name,"health":op.operator_health,"speed":op.operator_speed})
    return render(request,'ranked/operators.html',{'operators':ops_data})
