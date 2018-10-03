from django.shortcuts import render
from django.http import request

# Create your views here.
def home(request):
    return render(request, 'main.html', {})

def second(request):
    context = {
        'name': 'this name',
        'id': 'this id',
    }
    return render(request, 'second.html', context)

def contact(request):
    return render(request, 'contact.html', {})