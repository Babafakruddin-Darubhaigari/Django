from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name': 'Baba'})

def add(request):
    a = int(request.GET['num1'])
    b = int(request.GET['num2'])
    result = a + b
    return render(request, 'result.html', {'result': result})