from django.http import HttpResponse
from django.shortcuts import render
 
def index(request):
    return render(request, 'index.html')

def runoob(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'runoob.html', context)

def hello(request):
    return HttpResponse("Hello world ! ")