from django.http import HttpResponse
from django.shortcuts import render
from views import clculator

def calculator(request):
    return render(request, HttpResponse "calculator.html")