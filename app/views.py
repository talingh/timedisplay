from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
# Create your views here.
def hello(request):
    print("hello from views")
    
def index(request):
    context = {
        "time": strftime ("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, 'index.html', context )