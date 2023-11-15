from django.shortcuts import render
from django.http import HttpResponse
from .models import Operator

def index(request):
    return HttpResponse("Welcome to our R6 application")

def about(request):
    ops = Operator.objects.all()
    ram = ops[0]
    return HttpResponse(f"Name: {ram.operator_name}, Health: {ram.operator_health}, Speed: {ram.operator_speed}")
