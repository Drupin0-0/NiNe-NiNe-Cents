from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def product_register(request):
    if(request.method == 'POST'):
        pass

    return HttpResponse('<h1>API SEM ACESSO WEB</h1>')