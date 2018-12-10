from django.shortcuts import render

# Create your views here.

def dumb_santa_register(request):
    return render(request, 'dumb_santa_register/dumb_main.html', {})